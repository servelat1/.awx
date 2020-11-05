DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "dWZ2UFJiLjhCc21RYmVyWTp6S1VBeVlfUTVFbkRaczc5bU9fOC1jOFJ3OWk4eVlLVTpIRUltelpLMHlJUy1WWDlnbEFKb0ZYb0tWMkkyUHVxZ0Fqcy1Va0xZQXgtWE44amRSZ2REdTRfaTRXQkxndjFlWVdZeG1nbFR0UWNWb0s="
