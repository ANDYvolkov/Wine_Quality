import os
import zipfile
import subprocess

# ��������� ���������� ����� ��� ������������� Kaggle API
os.environ['KAGGLE_USERNAME'] = "andyvolkov" # username �� json �����
os.environ['KAGGLE_KEY'] = "ee612750627ca98100ffaaf9371c8a40" # key �� json �����

# ���������� �������� � Kaggle
subprocess.run(['kaggle', 'datasets', 'download', '-d', 'rajyellow46/wine-quality'])

# ���������� ����� �� ������ � ������� .\\data
with zipfile.ZipFile('wine-quality.zip', 'r') as zip_ref:
    zip_ref.extractall('..\\data')