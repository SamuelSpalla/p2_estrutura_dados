class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade


class PessoaInteressada:
    def __init__(self, nome, contato, especie_interesse):
        self.nome = nome
        self.contato = contato
        self.especie_interesse = especie_interesse


class Prefeitura:
    def __init__(self):
        self.animais = []
        self.pessoas_interessadas = []
        self.animais_ordenados_por_especie = {}

    def cadastrar_animal(self, tipo, idade, cor, porte, particularidade):
        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)
        self.animais_ordenados_por_especie.setdefault(tipo, []).append(animal)

    def cadastrar_pessoa(self, nome, contato, especie_interesse, tipo_preferencia, preferencia):
        pessoa = PessoaInteressada(nome, contato, especie_interesse)
        self.pessoas_interessadas.append(pessoa)

    def buscar_animais(self, busca_tipo, busca_idade, busca_cor, busca_porte):
        animais_selecionados = []
        for animal in self.animais_ordenados_por_especie[busca_tipo]:
            if busca_idade is None or animal.idade == busca_idade and \
                    busca_cor is None or animal.cor == busca_cor and \
                    busca_porte is None or animal.porte == busca_porte:
                animais_selecionados.append(animal)
        if len(animais_selecionados) > 0:
            n = 1
            for animal in animais_selecionados:
                print(f'\n\033[32m{n} Animal \033[0;0m \n'
                      f'Tipo: {animal.tipo}\n'
                      f'Idade: {animal.idade}\n'
                      f'Cor: {animal.cor}\n'
                      f'Porte: {animal.porte}\n'
                      f'Particularidade: {animal.particularidade}')
                n += 1
        else:
            print('\nNão há animais com todas as exatas caracteristicas passadas.\n'
                  'Temos os seguintes animais desse mesmo tipo:')
            n = 1
            for animal in self.animais_ordenados_por_especie[busca_tipo]:
                print(f'\n\033[32m{n} Animal \033[0;0m \n'
                      f'Tipo: {animal.tipo}\n'
                      f'Idade: {animal.idade}\n'
                      f'Cor: {animal.cor}\n'
                      f'Porte: {animal.porte}\n'
                      f'Particularidade: {animal.particularidade}')
                n += 1

    def relatorio(self):
        lista_pessoas = self.pessoas_interessadas
        for animal in self.animais:
            for pessoa in lista_pessoas:
                print(f'\n\n\033[1;34m{pessoa.nome}\033[0;0m')
                self.buscar_animais(pessoa.especie_interesse, None, None, None)
                print('------------------------------------------------')
                lista_pessoas.remove(pessoa)








