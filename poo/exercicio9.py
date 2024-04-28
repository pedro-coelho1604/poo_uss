class Departamento:
    def __init__(self):
        self.nome = ""
        self.gestor = None

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setGestor(self, gestor):
        self.gestor = gestor

    def getGestor(self):
        return self.gestor

    def getNomeGestor(self):
        if self.gestor is None:
            return "Departamento sem gestor"
        else:
            return self.gestor.getNome()


class Funcionario():
    def __init__(self, departamento):
        self.nome = ""
        if departamento is None:
            print("Erro")
            exit()
        else:
            self.departamento = departamento
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setDepartamento(self, departamento):
        if departamento is None:
            print("Erro")
            exit()
        else:
            self.departamento = departamento

    def getNomeDepartamento(self):
        if self.departamento is None:
            print("Funcionario sem departamento")
        else:
            return self.departamento.getNome()


    def getDepartamento(self):
        return self.departamento

class Gestor():
    def _init_(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


gestor = Gestor()
gestor.setNome("Carlos")


departamento = Departamento()
departamento.setNome("Gestao")
departamento.setGestor(gestor)


funcionario = Funcionario(departamento)
funcionario.setNome("Marco")
print(funcionario.getNomeDepartamento())
print(departamento.getNomeGestor())