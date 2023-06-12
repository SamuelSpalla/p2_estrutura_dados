from classes import *

prefeitura = Prefeitura()

prefeitura.cadastrar_animal("canino", "adulto", "marrom", "médio", "")
prefeitura.cadastrar_animal("canino", "filhote", "preto", "pequeno", "")

prefeitura.cadastrar_animal("felino", "adulto", "laranja", "médio", "")
prefeitura.cadastrar_animal("felino", "filhote", "branco", "pequeno", "cauda curta")

prefeitura.cadastrar_pessoa("João", "joao@email.com", "canino", "porte", "pequeno")
prefeitura.cadastrar_pessoa("Maria", "maria@email.com", "felino", "cor", "branco")

#------------------------------------------------------------------------------------------------------------------------

def continuar():
    print('-----------------------------------')
    input('Aperte ENTER para voltar ao menu')
    print('-----------------------------------')


def pular_linha():
    print('\n' * 10)


def confirmar(chave):
    print('\n',chave,'\n')
    v = input('Digite 1 para Manter ou 2 para alterar: ')
    if v == '1':
        return chave
    else:
        x = input('\nDigite novamente: ')
        confirmar(x)



def cadastro_animal():
    print(f'\n\nVamos efetuar o cadastro do Animal\n')

    tipo = input('\nQual o tipo do animal?\nSugestão - (canino, felino, etc)\n'
                 ': ')
    confirmar(tipo)

    idade = input('\nQual a idade aproximada do animal?\nSugestão - (filhote, adulto, idoso)\n'
                  ': ')
    confirmar(idade)

    cor = input('\nQual a cor principal do animal?\nSugestão - (branco, preto, etc)\n'
                ': ')
    confirmar(cor)

    porte = input('\nQual o porte do animal?\nSugestão - (pequeno, médio ou grande)\n'
                  ': ')
    confirmar(porte)

    parti = input('\nO animal possui alguma particularidade?\nCaso não tenha, apenas aperte Enter\n'
                  ': ')
    confirmar(parti)

    print('\nCadastro Efetuado\n')
    return prefeitura.cadastrar_animal(tipo, idade, cor, porte, parti)


def buscar_animal():
    print(f'\n\nVamos efetuar a busca do Animal\n')

    tipo = input('\nQual o tipo do animal?\nSugestão - (canino, felino, etc)\nSó preencha caso queira esse filtro\n'
                 ': ')
    confirmar(tipo)

    idade = input('\nQual a idade aproximada do animal?\nSugestão - (filhote, adulto, idoso)\nSó preencha caso queira esse filtro\n'
                  ': ')
    confirmar(idade)
    if idade == '':
        idade = None

    cor = input('\nQual a cor principal do animal?\nSugestão - (branco, preto, etc)\nSó preencha caso queira esse filtro\n'
                ': ')
    confirmar(cor)
    if cor == '':
        cor = None

    porte = input('\nQual o porte do animal?\nSugestão - (pequeno, médio ou grande)\nSó preencha caso queira esse filtro\n'
                  ': ')
    confirmar(porte)
    if porte == '':
        porte = None

    prefeitura.buscar_animais(tipo, idade, cor, porte)


def cadastro_pessoa():
    print(f'\n\nVamos efetuar o cadastro da Pessoa\n')
    nome = input('Qual o Nome?\n'
                 ': ')
    confirmar(nome)

    contato = input('Qual o contato?\nSugestão - (Email, Tel, etc)\n'
                    ': ')
    confirmar(contato)

    esp_int = input('Qual a espécie de interesse?\nSugestão - (canino, felino, etc)\n'
                    ': ')
    confirmar(esp_int)

    prefeitura.cadastrar_pessoa(nome, contato, esp_int)

def menu():
    while True:
        pular_linha()
        print('Escolha qual operação deseja fazer:\n'
              '1 - Cadastrar Animal\n'
              '2 - Cadastrar Pessoa\n'
              '3 - Buscar Animal\n'
              '4 - Gerar Relatório\n'
              '0 - sair\n')

        op = input(': ')
        if op == '0':
            break
        if op == '1':
            cadastro_animal()
            continuar()

        if op == '2':
            cadastro_pessoa()
            continuar()

        if op == '3':
           buscar_animal()
           continuar()

        if op == '4':
            prefeitura.relatorio()
            continuar()

        else:
            pass



menu()

