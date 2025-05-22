# Personal Data Protection Project

This project implements secure logging and password management practices for handling personally identifiable information (PII) in Python applications.

## Overview

The project consists of two main modules that provide comprehensive data protection capabilities:

### filtered_logger.py
A logging system that automatically redacts sensitive personal data from log messages to prevent PII exposure. Features include:

- **Data Obfuscation**: Uses regex patterns to identify and redact sensitive fields in log messages
- **Custom Log Formatter**: Automatically filters PII fields before logging
- **Secure Database Connection**: Connects to MySQL databases using environment variables for credentials
- **Compliance Ready**: Implements industry standards for PII protection in logging systems

### encrypt_password.py
A secure password management system using bcrypt for hashing and validation:

- **Salt-based Hashing**: Uses bcrypt to generate salted password hashes
- **Password Validation**: Securely validates passwords against stored hashes
- **Industry Standard**: Implements bcrypt best practices for password security

## Key Features

### PII Protection
The system identifies and protects five critical PII fields:
- Name
- Email address  
- Phone number
- Social Security Number (SSN)
- Password

### Security Compliance
- Passwords are never stored in plain text
- Database credentials are managed through environment variables
- All logging redacts sensitive information automatically
- Uses industry-standard bcrypt for password hashing

### Type Safety
All functions include comprehensive type annotations for better code reliability and development experience.

## Usage

### Environment Variables
Set these environment variables for database connectivity:
- `PERSONAL_DATA_DB_USERNAME` (default: "root")
- `PERSONAL_DATA_DB_PASSWORD` (default: "")
- `PERSONAL_DATA_DB_HOST` (default: "localhost")  
- `PERSONAL_DATA_DB_NAME` (required)

### Running the Logger
Execute the filtered_logger module directly to connect to the database and display user records with PII redaction:

```bash
./filtered_logger.py
```

### Password Management
Use the encrypt_password module functions to hash and validate passwords:

```python
from encrypt_password import hash_password, is_valid

# Hash a password
hashed = hash_password("mypassword")

# Validate a password
valid = is_valid(hashed, "mypassword")
```

## Requirements

- Python 3.7+
- Ubuntu 18.04 LTS
- MySQL database
- Required packages: mysql-connector-python, bcrypt

## Code Standards

- Follows pycodestyle (version 2.5) formatting
- All functions include comprehensive docstrings
- Type annotations on all function signatures
- Executable file permissions required
- Proper shebang line for Python 3
