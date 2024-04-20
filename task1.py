import os.path
import subprocess
import time

import requests
from subprocess import Popen, DEVNULL

def download_n_save_file(url: str, path: str):
    try:
        data = {
            'id': '1IGENwFzLm8bBEboISadYSNEdxbnjz1fH',
            'export': 'download',
            'authuser': 0,
            'confirm': 't'
        }
        response = requests.get(url, params=data)
        with open(path, 'wb') as f:
            f.write(response.content)
        print('File downloaded successfully.')
    except requests.RequestException:
        print('Something went wrong while accessing the link.')
    except WindowsError:
        print('Something went wrong while saving the file.')
    except Exception:
        print('Something went wrong.')


def update_registry(reg_file_path: str):
    try:
        assert reg_file_path.endswith('.reg')
        process = Popen(f'REG IMPORT "{reg_file_path}"',
                        shell=True,
                        stdout=DEVNULL,
                        stderr=DEVNULL)

        while process.poll() is None:
            continue

        print('Registry updated successfully.' if not process.poll() else
              'Something went wrong with registry update.')
    except AssertionError:
        print('The specified file has an invalid extension for accessing the Windows registry.')


def launch_game(game_path: str):
    if not os.path.exists(game_path):
        print('Game file is not exist.')
        exit(0)
        
    process = subprocess.Popen(game_path,
                               shell=True,
                               stdout=DEVNULL,
                               stderr=DEVNULL)
    in_game = False
    while process.poll() is None:
        if not in_game:
            print('In game...')
            in_game = True

    print('Game closed.')


url = 'https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0'
filename = 'settings.reg'
game_dir_path = r'D:\SteamLibrary\steamapps\common\Goose Goose Duck'  # путь к директории с игрой

file_path = rf'{game_dir_path}\{filename}'

if not os.path.exists(file_path):
    download_n_save_file(url, file_path)
else:
    print('The settings file already exists, it will be applied.')

update_registry(file_path)

launch_game(rf'{game_dir_path}\GGDLauncher.exe')