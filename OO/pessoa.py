class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    tantor = Pessoa(nome='tantor')
    dorian = Pessoa(tantor, nome='Dorian')
    print(dorian.cumprimentar())
    print(dorian.nome)
    print(dorian.idade)
    for filho in dorian.filhos:
        print(filho.nome)
    dorian.sobrenome = 'Sampaio'
    del dorian.filhos
    print(dorian.__dict__)
    print(tantor.__dict__)