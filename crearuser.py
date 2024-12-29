import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webfarma.settings')
django.setup()

if not django.apps.apps.ready:
    raise Exception("El registro de aplicaciones no ha sido cargado aún.")

from django.core.management import call_command
from django.contrib.auth.models import User
from django.db import IntegrityError



def create_superuser():
    try:
        user = User.objects.create_superuser('Farm4weB2024', 'teovazqueze@gmail.com', '1G5e6WU7d')
        print("Superusuario creado:", user.username)
    except IntegrityError:
        print("El superusuario ya existe.")

if __name__ == "__main__":
    create_superuser()
