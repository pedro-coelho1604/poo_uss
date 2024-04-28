class Pais:
    def _init_(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

class Estado():
    def __init__(self, pais):
        self.nome = ""
        if pais is None:
            print("Erro")
            exit()
        else:
            self.pais = pais

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setPais(self, pais):
        if pais is None:
            print("Erro")
            exit()
        else:
            self.pais = pais

    def getNomePais(self):
        if self.pais is None:
            print("Estado sem Pais")
        else:
            return self.pais.getNome()


    def getPais(self):
        return self.pais
    

class Cidade():
    def __init__(self, estado):
        self.nome = ""
        if estado is None:
            print("Erro")
            exit()
        else:
            self.estado = estado

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setEstado(self, estado):
        if estado is None:
            print("Erro")
            exit()
        else:
            self.estado = estado

    def getNomeEstado(self):
        if self.estado is None:
            print("Cidade sem estado")
        else:
            return self.estado.getNome()

    def getEstado(self):
        return self.estado

class Endereco():
    def __init__(self, cidade):
        self.logradouro = ""
        self.numero = 0
        self.complemento = ""
        self.bairro = ""
        self.cliente = None
        if cidade is None:
            print("Erro")
            exit()
        else:
            self.cidade = cidade

    def setLogradouro(self, logradouro):
        self.logradouro = logradouro

    def getLogradouro(self):
        return self.logradouro

    def setNumero(self, numero):
        self.numero = numero

    def getNumero(self):
        return self.numero

    def setComplemento(self, complemento):
        self.complemento = complemento

    def getComplemento(self):
        return self.complemento

    def setBairro(self, bairro):
        self.bairro = bairro

    def getBairro(self):
        return self.bairro

    def setCidade(self, cidade):
        if cidade is None:
            print("Erro")
            exit()
        else:
            self.cidade = cidade

    def getNomeCidade(self):
        if self.cidade is None:
            print("Endereço sem cidade")
        else:
            return self.cidade.getNome()

    def getCidade(self):
        return self.cidade

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente

    def getNomeCliente(self):
        if self.cliente is None:
            return "Endereço sem Cliente"
        else:
            return self.cliente.getNome()

class Cliente:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    


pais = Pais()
pais.setNome("Brasil")

estado = Estado(pais)
estado.setNome("Rio")

cidade = Cidade(estado)
cidade.setNome("Vassouras")

endereco = Endereco(cidade)

cliente = Cliente()
cliente.setNome("Caio")

# print(estado.getNome())
# print(estado.getNomePais())

# print(cidade.getNome())
# print(cidade.getNomeEstado())

print(endereco.getNomeCidade())
