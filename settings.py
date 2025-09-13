from dotenv import load_dotenv
import os 


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = ('SECRET_KEY', 'django-insecure-fallback-key-for-development')

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True