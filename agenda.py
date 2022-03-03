AGENDA = {}  # abertura de variavel global / dicionario


# metodo / mostrar os contatos salvos na AGENDA/dicionario
def mostrar_contatos():
    if AGENDA:  # se tem contato na agenda
        print('\nSegue lista de contatos na agenda:')
        for contato in AGENDA:  # para cada contato na agenda, monstrar os contatos
            print(f'-{contato}')
        print('')

    else:  # senão:
        print('Não foi encontrado nenhum contato na agenda!\n')


# metodo / busca detalhada na AGENDA, através do nome do contato
def buscar_contato(contato):
    try:
        contato = input(
            'Informe o nome do contato que deseja os dados ou digite "SAIR" para encerrar a busca: ')

        if contato != 'SAIR':  # se a opção "contato" foi igual a sair, não buscar contato
            print('------------------------------------')
            print(f'Nome: {contato}')
            print('Telefone:', AGENDA[contato]['Telefone'])
            print('Email:', AGENDA[contato]['Email'])
            print('Endereco:', AGENDA[contato]['Endereco'])
            print('------------------------------------')

        elif contato == 'SAIR':  # se a opção for sair o metodo irá se encerrar
            print('Não será feito a busca busca!')
            print('------------------------------------')

    except KeyError as error:
        print('Não foi encontrado o contato na agenda!')
        print('------------------------------------')


# metodo de inclusão de contato, se o contato já existir os dados serão alterados
# este metodo serve para dar a opção ao usuário
def incluir_editar_contato(incluir_editar, Telefone, Email, Endereco):

    incluir_editar = input(
        'Informe o nome do contato que deseja incluir/editar ou digite "SAIR" para não incluir/editar contato: ')  # pergunta se deve SAIR
    if incluir_editar == 'SAIR':  # se a escolha for "SAIR" não continuar com a inclusão/edição
        print('Por enquanto não será incluso/editado nenhum contato!')
        print('------------------------------------')

    else:
        print('Seguindo com a solicitação:\n')
        try:  # primeiro será feito esta tentativa de validação, para verificar se o nome ja existe
            # se a AGENDA ja tiver o nome escolhido, o mesmo irá para o metodo de edição
            AGENDA[incluir_editar]
            print('O contato já existe, você esta no modo de edição!')
            opcap_edicao = input(
                'Caso deseje editar este contato, tecle ENTER, caso não deseje editar digite "SAIR": ')  # novamente, pergunta se deve SAIR
            if opcap_edicao == 'SAIR':  # se opção for "SAIR", programa se encerra
                print('------------------------------------')

            else:  # senão:
                print()
                nome = incluir_editar  # opção incluída em variável "nome"
                # dados escolhidos serão enviados para o metodo abaixo em que será feito a alteração
                editar_incluir_dados(nome, Telefone, Email, Endereco)

        except:  # caso a tentativa "try" seja Falsa, será dado inicio a inclusão de um novo contato
            print('O contato não existe, você esta no modo de inclusão!')
            opcap_inclusao = input(
                'Caso deseje incluir este contato, tecle ENTER, caso não deseje incluir digite "SAIR": ')  # novamente, pergunta se deve SAIR
            if opcap_inclusao == 'SAIR':  # se opção for "SAIR", programa se encerra
                print('------------------------------------')

            else:  # senão:
                print()
                nome = incluir_editar  # opção incluída em variável "nome"
                # dados escolhidos serão enviados para o metodo abaixo em que será feito a alteração
                editar_incluir_dados(nome, Telefone, Email, Endereco)


# este metodo irá complementar o metodo acima, caso seja feito a escolha de editar/incluir, será armazenado os dados
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
    # irá salvar alteração conforme metodo criado abaixo
    salvar_agenda()
    print(f'Contato {nome} incluído/alterado com sucesso!')


# metodo de exclusão do contato na AGENDA
def excluir_contato(excluir):

    try:
        if AGENDA:  # se o contato existe na agenda
            excluir = input(
                'Informe o nome do contato que deseja excluir ou digite "SAIR" para não excluir contato: ')

            if excluir != 'SAIR':
                # contato será excluido utilizando o metodo AGENDA.pop()
                AGENDA.pop(f'{excluir}')
                print(f'Contato: {excluir} excluido com sucesso!')
                salvar_agenda()  # será salvo a alteração no arquivo
                print('------------------------------------')

            else:  # se a opção for igual a "SAIR", o programa se encerra
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


# metodo de exportação de dados:
def exportar_contatos(nome_arquivo):
    try:
        # será criado um novo arquivo utilizando o metodo write == escrita
        with open(nome_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                Telefone = AGENDA[contato]['Telefone']
                Email = AGENDA[contato]['Email']
                Endereco = AGENDA[contato]['Endereco']
                arquivo.write(
                    f'{contato},{Telefone},{ Email},{Endereco}\n')  # exportado os dados acima para o arquivo
        print('Agenda exportada/salva com sucesso!')

    except:
        print('Algum erro ocorreu ao exportar!')
        print('------------------------------------')


# metodo de importação de dados:
def importar_contatos(nome_arquivo):
    try:
        # será carregado o arquivo utilizando o metodo read == ler
        with open(nome_arquivo, 'r') as arquivo:
            contatos = arquivo.readlines()  # leitura do arquivo foi colocada em uma variável
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


# metodo que irá salvar a AGENDA utilizando o metodo de "exportar" acima
def salvar_agenda():
    exportar_contatos('database.csv')  # formato do arquivo.csv
    print('Database salvo com sucesso!')


# metodo que irá carregar a AGENDA utilizando o metodo de "importar" acima
def carregar_agenda():
    try:
        with open('database.csv', 'r') as arquivo:  # irá retornar a leitura do arquivo.csv
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
        # mostra quantos contatos foram "carregados"
        print(f'contatos carregados: {len(AGENDA)}')

    except FileNotFoundError:
        print('Arquivo não encontrado!')
        print('------------------------------------')

    except Exception as error:
        print('Algum erro ocorreu ao importar!')
        print(error)
        print('------------------------------------')


def imprimir_menu():  # menu de opções que irá aparecer ao iniciar o programa
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


def imprimir_menu_opcao(opcao):  # escolha de opções apresentadas no menu
    carregar_agenda()
    while True:  # enquanto o loop for verdadeiro o programa continua rodando
        # cada opção irá retornar um dos metodos definidos acima
        opcao = (input('Escolha uma opção: '))
        print('------------------------------------')
        if opcao == '1':
            mostrar_contatos()
        elif opcao == '2':
            buscar_contato('')
        elif opcao == '3':
            # irá pegar os dados primeiro e depois o nome do contato
            print('Informe os dados, logo em seguida o nome do contato:')
            Telefone = input('Informe o numero de telefone: ')
            Email = input('Informe o Email: ')
            Endereco = input('Informe o Endereço: ')
            # irá chamar o metodo já com os dados salvos acima
            incluir_editar_contato('', Telefone, Email, Endereco)
        elif opcao == '4':
            excluir_contato('')
        elif opcao == '5':
            # exportar arquivo manualmente
            nome_arquivo = input('Digite o nome do arquivo: ')
            print('Arquivo foi exportado!')
            exportar_contatos(nome_arquivo.strip().split())

        elif opcao == '6':
            # importar arquivo manualmente
            nome_arquivo = input('Digite o nome do arquivo: ')
            print('Arquivo foi importado!')
            importar_contatos(nome_arquivo)

        elif opcao == '0':
            print('O programa foi encerrado!')  # Irá encerrar o programa
            print('Obrigado pelo uso!')
            break  # irá encerrar o loop do while
        else:
            # caso não seja escolhido nenhum opção acima, o programa continua...
            print('Opção invalida!')


# O programa irá se "iniciar" aqui:
imprimir_menu()  # primeiro será apresentado o menu
imprimir_menu_opcao('')  # segundo será aberto o "loop" de opções
