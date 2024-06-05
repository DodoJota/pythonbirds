class Pessoa:
    olhos=2

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
    tantor.olhos = 1
    print(dorian.__dict__)
    print(tantor.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(dorian.olhos)
    print(tantor.olhos)
    print(id(pessoa.olhos), id(tantor.olhos), id(dorian.olhos))

