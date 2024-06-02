import os

import argparse
from colorama import init, Fore, Back

init(autoreset=True)

parser = argparse.ArgumentParser(
                    prog='Script for run server',
                    description='Run server',
                    epilog='Enjoy the script!')

parser.add_argument('ip', type=str, help='ip', default='0.0.0.0')
parser.add_argument('port', type=str, help='port', default='80')
args = parser.parse_args()

print(Fore.BLUE+'Старт сервера...')

os.system("python manage.py makemigrations")
os.system("python manage.py makemigrations account")
os.system("python manage.py makemigrations main")
os.system("python manage.py makemigrations session")
os.system("python manage.py makemigrations tests")
os.system("python manage.py migrate")

print(Fore.GREEN+'Сервер запущен! Откройте в браузере http://{}:{}. Нажмите Ctrl+C для выхода. Good job!'.format(args.ip, args.port))
print(Fore.YELLOW+'Внимание! Чтобы создать суперпользователя для админ панели выполните команду: python manage.py createsuperuser')
os.system(f"python manage.py runserver {args.ip}:{args.port}")
