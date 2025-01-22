import os

class Config:
    SECRET_KEY = os.getenv()
    SQLALCHEMY_DATABASE_URI = 