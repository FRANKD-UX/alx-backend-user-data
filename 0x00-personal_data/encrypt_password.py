#!/usr/bin/env python3
"""
Module for secure password hashing and validation using bcrypt.

This module provides functions to safely hash passwords with salt and validate
passwords against their hashed versions, following security best practices
for password storage and authentication.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a salt using bcrypt for secure storage.

    Args:
        password: Plain text password to be hashed

    Returns:
        Salted hash of the password as bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against its hashed version.

    Args:
        hashed_password: Previously hashed password as bytes
        password: Plain text password to validate

    Returns:
        True if password matches the hash, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
