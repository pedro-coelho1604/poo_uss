# Classes: Pessoa, Pessoa Física, Pessoa Jurídica
# Pessoa: nome, endereco
# Pessoa Física: cpf
# Pessoa Jurídica: cnpj

class Pessoa:

    def _init_(self):
        self.nome = ""
        self.email = ""
        self.telefone = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email


class Aluno(Pessoa):

    def _init_(self):
        Pessoa._init_(self)
        self.matricula = 0

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula


class Professor(Pessoa):

    def _init_(self):
        Pessoa._init_(self)
        self.titulacao = ""

    def setTitulacao(self, titulacao):
        self.titulacao = titulacao

    def getTitulacao(self):
        return self.titulacao

professor = Professor()
professor.setNome("Caio")
professor.setTitulacao("Doutorado")
print(professor.getTitulacao())
print(professor.getNome())

aluno = Aluno()
aluno.setNome("Maria")
print(aluno.getNome())

