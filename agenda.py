AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        print('\nSegue lista de contatos na agenda:')
        for contato in AGENDA:
            print(f'-{contato}')
        print('')

    else:
        print('Não foi encontrado nenhum contato na agenda!\n')


def buscar_contato(contato):
    try:
        contato = input(
            'Informe o nome do contato que deseja os dados ou digite "SAIR" para encerrar a busca: ')

        if contato != 'SAIR':
            print('------------------------------------')
            print(f'Nome: {contato}')
            print('Telefone:', AGENDA[contato]['Telefone'])
            print('Email:', AGENDA[contato]['Email'])
            print('Endereco:', AGENDA[contato]['Endereco'])
            print('------------------------------------')

        elif contato == 'SAIR':
            print('Não será feito a busca busca!')
            print('------------------------------------')

    except KeyError as error:
        print('Não foi encontrado o contato na agenda!')
        print('------------------------------------')


def incluir_editar_contato(incluir_editar, Telefone, Email, Endereco):

    incluir_editar = input(
        'Informe o nome do contato que deseja incluir/editar ou digite "SAIR" para não incluir/editar contato: ')
    if incluir_editar == 'SAIR':
        print('Por enquanto não será incluso/editado nenhum contato!')
        print('------------------------------------')

    else:
        print('Seguindo com a solicitação:\n')
        try:
            AGENDA[incluir_editar]
            print('O contato já existe, você esta no modo de edição!')
            opcap_edicao = input(
                'Caso deseje editar este contato, tecle ENTER, caso não deseje editar digite "SAIR": ')
            if opcap_edicao == 'SAIR':
                print('------------------------------------')

            else:
                print()
                nome = incluir_editar
                editar_incluir_dados(nome, Telefone, Email, Endereco)

        except:
            print('O contato não existe, você esta no modo de inclusão!')
            opcap_inclusao = input(
                'Caso deseje incluir este contato, tecle ENTER, caso não deseje incluir digite "SAIR": ')
            if opcap_inclusao == 'SAIR':
                print('------------------------------------')

            else:
                print()
                nome = incluir_editar
                editar_incluir_dados(nome, Telefone, Email, Endereco)


def editar_incluir_dados(nome, Telefone, Email, Endereco):

    nome
    Telefone
    Email
    Endereco
    AGENDA[nome] = {
        'Telefone': Telefone,
        'Email': Email,
        'Endereco': Endereco,
    }
    salvar_agenda()
    print(f'Contato {nome} incluído/alterado com sucesso!')


def excluir_contato(excluir):

    try:
        if AGENDA:
            excluir = input(
                'Informe o nome do contato que deseja excluir ou digite "SAIR" para não excluir contato: ')

            if excluir != 'SAIR':
                AGENDA.pop(f'{excluir}')
                print(f'Contato: {excluir} excluido com sucesso!')
                salvar_agenda()
                print('------------------------------------')

            else:
                print(
                    'Por enquanto não será excluido nenhum contato!')
                print('------------------------------------')

        else:
            print('Não tem contato na agenda!')

    except KeyError as error:
        print('Não foi possivel excluir contato, contato não encontrado!')
        print('------------------------------------')

    except Exception as error:
        print('Erro inesperado ocorreu!')
        print('------------------------------------')


def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                Telefone = AGENDA[contato]['Telefone']
                Email = AGENDA[contato]['Email']
                Endereco = AGENDA[contato]['Endereco']
                arquivo.write(
                    f'{contato},{Telefone},{ Email},{Endereco}\n')
        print('Agenda exportada/salva com sucesso!')

    except:
        print('Algum erro ocorreu ao exportar!')
        print('------------------------------------')


def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            contatos = arquivo.readlines()
            for linha in contatos:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                editar_incluir_dados(
                    nome, telefone, email, endereco)
        print('Agenda importada/carregada com sucesso!')

    except FileNotFoundError:
        print('Arquivo não encontrado!')
        print('------------------------------------')

    except Exception as error:
        print('Algum erro ocorreu ao importar!')
        print(error)
        print('------------------------------------')


def salvar_agenda():
    exportar_contatos('database.csv')
    print('Database salvo com sucesso!')


def carregar_agenda():
    try:
        with open('database.csv', 'r') as arquivo:
            contatos = arquivo.readlines()
            for linha in contatos:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'Telefone': telefone,
                    'Email': email,
                    'Endereco': endereco,
                }
        print('Database carregado com sucesso!')
        print(f'contatos carregados: {len(AGENDA)}')

    except FileNotFoundError:
        print('Arquivo não encontrado!')
        print('------------------------------------')

    except Exception as error:
        print('Algum erro ocorreu ao importar!')
        print(error)
        print('------------------------------------')


def imprimir_menu():
    print('\nOpções:')
    print('------------------------------------')
    print('1 - Mostrar contatos')
    print('2 - detalhes de um contato')
    print('3 - Incluir/editar contato')
    print('4 - Excluir contato')
    print('5 - Exportar agenda para CSV')
    print('6 - Importar CSV para Agenda')
    print('0 - Fechar agenda')
    print('------------------------------------')


def imprimir_menu_opcao(opcao):
    carregar_agenda()
    while True:
        opcao = (input('Escolha uma opção: '))
        print('------------------------------------')
        if opcao == '1':
            mostrar_contatos()
        elif opcao == '2':
            buscar_contato('')
        elif opcao == '3':
            print('Informe os dados, logo em seguida o nome do contato:')
            Telefone = input('Informe o numero de telefone: ')
            Email = input('Informe o Email: ')
            Endereco = input('Informe o Endereço: ')
            incluir_editar_contato('', Telefone, Email, Endereco)
        elif opcao == '4':
            excluir_contato('')
        elif opcao == '5':
            nome_arquivo = input('Digite o nome do arquivo: ')
            print('Arquivo foi exportado!')
            exportar_contatos(nome_arquivo.strip().split())

        elif opcao == '6':
            nome_arquivo = input('Digite o nome do arquivo: ')
            print('Arquivo foi importado!')
            importar_contatos(nome_arquivo)

        elif opcao == '0':
            print('O programa foi encerrado!')
            print('Obrigado pelo uso!')
            break
        else:
            print('Opção invalida!')


imprimir_menu()
imprimir_menu_opcao('')
