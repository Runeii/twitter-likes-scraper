import os
from pathlib import Path

current_dir = Path(__file__).parent.absolute()

def get_email():
    return os.environ.get('USER_EMAIL')


def get_password():
    return os.environ.get('USER_PASSWORD')


def get_username():
    return os.environ.get('USERUSERNAMEL')
