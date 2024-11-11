print("## Executando antes de gerar ##")

import os
import shutil

print(f'dir: {os.getcwd()}')

# Caminho do diretório onde estão os arquivos disponíveis
origem_diretorio = os.path.join(os.getcwd(), "../arquivos")
print(origem_diretorio)

# Caminho do diretório de destino no projeto gerado
destino_diretorio = os.path.join("{{cookiecutter.nome_projeto}}", "exercicios")
print(destino_diretorio)

# Lê a lista de arquivos selecionados pelo usuário
arquivos_selecionados = '{{ cookiecutter.arquivos_selecionados }}'
arquivos = [arquivo.strip() for arquivo in arquivos_selecionados.split(',')]
print(f'Arquivos selecionados: {arquivos_selecionados}')
print(f'Arquivos: {arquivos}')

# Lista para os novos nomes dos arquivos
novos_nomes = ["x1.py", "x2.py", "x3.py"]

# Verifica se a quantidade de arquivos selecionados é igual ao número de novos nomes disponíveis
if len(arquivos) != len(novos_nomes):
    raise ValueError(f"Por favor, selecione exatamente {len(novos_nomes)} arquivos.")


# Copia e renomeia os arquivos selecionados para o diretório de destino
for arquivo, novo_nome in zip(arquivos, novos_nomes):
    arquivo_origem = os.path.join(origem_diretorio, arquivo)
    arquivo_destino = os.path.join(destino_diretorio, novo_nome)
    print(f'arquivo: {arquivo}')
    print(f'arquivo_origem: {arquivo_origem}')
    print(f'arquivo_destino: {arquivo_destino}')
    
    # Verifica se o arquivo existe antes de copiar
    if not os.path.exists(arquivo_origem):
        raise FileNotFoundError(f"O arquivo {arquivo} não existe no diretório de origem.")
    
    # Copia e renomeia o arquivo
    shutil.copyfile(arquivo_origem, arquivo_destino)

print(f"Arquivos selecionados e renomeados com sucesso: {novos_nomes}")
