from unicodedata import name


class Quarto(object):

    def __init__(self, nome='', dimensoes='') -> None:
        
        self.nome = nome
        self.dimensoes = dimensoes

    def __repr__(self) -> str:
        s = self.nome + "," + self.dimensoes
        return s


class Mobilia(object):

    def __init__(self, nome='', funcao='', material='', quarto=None) -> None:

        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto

    def __repr__(self) -> str:
        s = self.nome + "," + self.funcao + "," + self.material
        if self.quarto:
            s += "," + str(self.quarto)
        return s


class Casa(object):

    def __init__(self, formato='', quartos=None):

        self.formato = formato
        self.quartos = quartos

    def __repr__(self) -> str:
        s = self.formato
        for q in self.quartos:
            s += "," + str(q)
        return s


if __name__ == "__main__":
    c1 = Casa(formato='Romana')
    print(c1)