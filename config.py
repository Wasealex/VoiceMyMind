# Generate a secure random secret key
DEBUG = False

    # Database configuration
DB_HOST = 'localhost'
DB_USER = 'voicemymind'
DB_PASSWORD = 'VoiceMyMind'
DB_NAME = 'voice_database'

SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
