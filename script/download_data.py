import os
import zipfile
import subprocess

# Установка переменных среды для использования Kaggle API
os.environ['KAGGLE_USERNAME'] = "andyvolkov" # username из json файла
os.environ['KAGGLE_KEY'] = "ee612750627ca98100ffaaf9371c8a40" # key из json файла

# Скачивание датасета с Kaggle
subprocess.run(['kaggle', 'datasets', 'download', '-d', 'rajyellow46/wine-quality'])

# Распаковка файла из архива в каталог .\\data
with zipfile.ZipFile('wine-quality.zip', 'r') as zip_ref:
    zip_ref.extractall('..\\data')