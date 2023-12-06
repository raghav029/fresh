from dotenv import load_dotenv
import os


load_dotenv()

class ApplicationConfig:
    SECRET_KEY = os.environ['SECRET_KEY']

    SQLALCHEMY_TRACT_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost:3307/event_management_app'
