import subprocess

import argparse
parser = argparse.ArgumentParser(
                    prog='Script for run server',
                    description='Run server',
                    epilog='Enjoy the script!')

parser.add_argument('what')
args = parser.parse_args()

subprocess.run("python BLTS\\manage.py runserver 192.168.0.16:8000", shell=True)