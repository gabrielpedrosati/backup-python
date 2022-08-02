# Projeto de Compactando Arquivos .zip - Finalidade: Backup's

# Importando bibliotecas
import zipfile

# Criando função - receberá dois parâmetros: arquivos e nome do arquivo #compactado


def backupFile(file, filename='Compressed'):
    # Se for apenas um arquivo
    if len(file) == 1:
        # Nomeando o arquivo compactado
        compressedFile = zipfile.ZipFile('{}.zip'.format(filename), 'w')
        print('Compactando...')
        # Compactando o arquivo
        compressedFile.write(file[0], compress_type=zipfile.ZIP_DEFLATED)
        # Fechando o arquivo compactado
        compressedFile.close()
        print('Arquivo compactado.')
    # Se for mais de um arquivo
    elif len(file) > 1:
        # Nomeando o arquivo compactado
        compressedFile = zipfile.ZipFile(f'{filename}.zip', 'w')
        # Percorrendo a lista com os arquivos a serem compactados
        for items in file:
            print(f'Compactando {items}...')
            # Compactando o arquivo
            compressedFile.write(items, compress_type=zipfile.ZIP_DEFLATED)

        print('Arquivo compactado.')
        compressedFile.close()
    # Se não tiver arquivos
    else:
        print('Não foi possível determinar o arquivo a ser compactado.')


# Variáveis
file = []
filename = input('Digite o nome final do arquivo zip: ')

# Recebendo o nome dos arquivos
while True:
    file.append(input(
        'Digite o nome do arquivo (com extensão) que deseja compactar ou dê Enter para compactar: '))

    # Encerrando o laço while
    if file[-1] == '':
        file.pop()
        break

# Chamando a função
backupFile(file=file, filename=filename)
