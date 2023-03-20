#!/usr/bin/env python

import os

import django
from django.contrib.auth import get_user_model

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'koodausblogi.settings')
    django.setup()

    username = os.environ.get('ADMIN_USER_NAME', 'admin')
    password = os.environ.get('ADMIN_USER_PASSWORD')
    email = os.environ.get('ADMIN_USER_EMAIL', '')

    users = get_user_model().objects

    if users.filter(username=username).exists():
        print(f"User {username!r} already exists")
        return

    if not password:
        raise SystemExit("ADMIN_USER_PASSWORD environment variable is needed!")

    print(f"Creating superuser {username!r}")
    users.create_superuser(username, email, password)


if __name__ == '__main__':
    main()
