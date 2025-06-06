#!/usr/bin/env python3
"""
BasicAuth class
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None:
            return None
        
        if not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith('Basic '):
            return None
        
        return authorization_header[6:]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        
        if not isinstance(base64_authorization_header, str):
            return None
        
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
    
    def extract_user_credentials
