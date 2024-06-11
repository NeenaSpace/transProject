import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'af94b5bb20e04b6b2d82a2df7c2a2b6b128cd97a4c2a6a243c7ad4f8974b56a7')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'd4f9c8bc9e7e5d798c2d8e7f12d4c1a7a3f6a7b4e9c5d8f7e2a1b8c6a9d2b4e6')
    GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID', 'translatebackend-426005')
    GOOGLE_LOCATION = os.getenv('GOOGLE_LOCATION', 'global')
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', '/Users/ninawang/Desktop/transProject/sign_language_api/translatebackend-426005-5f1aac4ba929.json')