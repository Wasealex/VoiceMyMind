"""
Configures the application settings for the Sourcegraph code search and navigation tool.

This module defines the configuration options 
such as the server URL
authentication settings
and various feature flags.

The configuration is typically loaded from environment variables or a configuration file, 
and is used throughout the application to customize its behavior.
"""

import os
import secrets
import string

class Config:
    # Generate a secure random secret key
    SECRET_KEY = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))

    DEBUG = False

    # Database configuration
    DB_HOST = 'localhost'
    DB_USER = 'voicemymind'
    DB_PASSWORD = 'VoiceMyMind'
    DB_NAME = 'voice_database'

    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
