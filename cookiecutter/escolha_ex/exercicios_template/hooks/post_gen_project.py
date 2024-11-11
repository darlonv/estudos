print("## Executando depois de gerar ##")

import os
import shutil
from pathlib import Path

arquivos_sempre_manter = ["__init__.py"]

def remove_files_except(directory_path, files_keep):
    # Iterate over all files in the specified directory
    for file_path in Path(directory_path).iterdir():
        # Check if the path is a file (not a directory) and if it's not in the list of files to keep
        if file_path.is_file() and file_path.name not in files_keep:
            try:
                # Delete file
                file_path.unlink()  
            except Exception as e:
                print(f"Could not delete {file_path}: {e}")

print(f'dir: {os.getcwd()}')

# Access the conditional value from the cookiecutter context
copy_directory = "{{ cookiecutter._arquivos_dir }}"  # This will be "yes" or "no"

print(f'copy_directory: {copy_directory}')

arquivos_selecionados = "{{ cookiecutter.arquivos_selecionados }}".split(",")
print(f'arquivos_selecionados: {arquivos_selecionados}')

#Remove unused python files
arquivos_selecionados_python = list(map(lambda x: f'{x}.py', arquivos_selecionados)) + arquivos_sempre_manter
print(f'arquivos_selecionados: {arquivos_selecionados_python}')
remove_files_except(copy_directory, arquivos_selecionados_python)

#Remove unused python test files
arquivos_selecionados_python_test = list(map(lambda x: f'test_{x}.py', arquivos_selecionados)) + arquivos_sempre_manter
print(f'arquivos_selecionados: {arquivos_selecionados_python_test}')
remove_files_except("tests", arquivos_selecionados_python_test)