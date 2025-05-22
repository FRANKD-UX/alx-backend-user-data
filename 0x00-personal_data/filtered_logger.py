#!/usr/bin/env python3
"""
Module for filtering and logging personal data with redaction capabilities.

This module provides functionality to obfuscate sensitive information in log
messages, create secure loggers, and connect to databases while maintaining
data privacy standards.
"""
import re
import logging
import os
from typing import List
import mysql.connector
from mysql.connector import connection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscate specified fields in a log message using regex substitution.

    Args:
        fields: List of field names to obfuscate
        redaction: String to replace field values with
        message: Log message containing field=value pairs
        separator: Character separating fields in the message

    Returns:
        The log message with specified fields obfuscated
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}",
                  message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for filtering sensitive data in log records.

    This formatter automatically redacts specified PII fields from log messages
    before they are output, ensuring sensitive information is not exposed in logs.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with specified fields to redact.

        Args:
            fields: List of field names that should be redacted in log messages
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record by redacting sensitive fields.

        Args:
            record: The log record to format

        Returns:
            Formatted log message with sensitive fields redacted
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data with PII redaction.

    Returns:
        Configured logger instance that redacts PII fields
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


def get_db() -> connection.MySQLConnection:
    """
    Create a secure connection to the personal data database.

    Uses environment variables for database credentials to maintain security.
    Default values: username='root', password='', host='localhost'

    Returns:
        MySQL database connection object
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    """
    Main function to retrieve and display user data with PII redaction.

    Connects to the database, retrieves all user records, and logs them
    with sensitive fields properly redacted for security compliance.
    """
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = "; ".join([f"{field}={value}" for field, value in 
                           zip(cursor.column_names, row)]) + ";"
        logger.info(message)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
