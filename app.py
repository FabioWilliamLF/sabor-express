import os

restaurantes = [{'nome': 'Restaurante 1', 'categoria':'Japonesa', 'ativo': True},
                {'nome': 'Restaurante 2', 'categoria':'Italiano', 'ativo': False},
                {'nome': 'Restaurante 3', 'categoria':'Brasileira', 'ativo': True}]

def exibir_nome_do_programa():
    print("""

    ╔═══╗──╔╗───────╔═══╗
    ║╔═╗║──║║───────║╔══╝
    ║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
    ╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
    ║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
    ╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
    ───────────────────────║║
    ───────────────────────╚╝
    """)

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair restaurante\n')

def finalizar_app():
    exibir_subtitulo('Finalizando aplicação...')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def voltar_menu_principal():
    input('Pressione ENTER para voltar ao menu principal... ')
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listar restaurantes')
    for index, restaurante in enumerate(restaurantes):
        status = 'ativo' if restaurante['ativo'] else 'inativo'
        print(f'{index + 1}. {restaurante['nome'].ljust(20)} - {restaurante['categoria'].ljust(20)} - {status.ljust(20)}')
    print()
    voltar_menu_principal()

def alterar_status_restaurante():
    exibir_subtitulo('Alterar status do restaurante')
    for index, restaurante in enumerate(restaurantes):
        status = 'ativo' if restaurante['ativo'] else 'inativo'
        print(f'{index + 1}. {restaurante['nome'].ljust(20)} - {restaurante['categoria'].ljust(20)} - {status.ljust(20)}')
    try:
        opcao = int(input('Escolha um restaurante para ativar: '))
        if restaurantes[opcao - 1]['ativo']:
            restaurantes[opcao - 1]['ativo'] = False
            print('Restaurante desativado com sucesso!\n')
        else:
            restaurantes[opcao - 1]['ativo'] = True
            print('Restaurante ativado com sucesso!\n')
    except:
        print('Opção inválida!\n')
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alterar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

            

    # opcao = int(input('Escolha uma opção: '))
    # print(f'Opção escolhida: {opcao}')

    # if opcao == 1:
    #     print('Cadastrar restaurante')
    # elif opcao == 2:
    #     print('Listar restaurante')
    # elif opcao == 3:
    #     print('Ativar restaurante')
    # else:
    #     finalizar_app()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
