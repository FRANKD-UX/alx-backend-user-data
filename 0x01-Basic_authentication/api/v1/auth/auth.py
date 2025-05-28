#!/usr/bin/env python3
"""
Auth class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Template for all authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of strings excluded_paths
        """
        if path is None:
            return True
        
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        
        # Make path slash tolerant
        if not path.endswith('/'):
            path += '/'
        
        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'
            if path == excluded_path:
                return False
        
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the header request Authorization
        """
        if request is None:
            return None
        
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object"""
        return None
