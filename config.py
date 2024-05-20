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

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
DEBUG = os.environ.get('DEBUG', False)

# Database configuration
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', 'my_database')

SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
