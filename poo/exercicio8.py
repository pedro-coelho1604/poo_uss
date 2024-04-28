class Curso:

    def _init_(self):
        self.nome = ""
        self.coordenador = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setCoordenador(self, professor):
        self.coordenador = professor

    def getCoordenador(self):
        return self.coordenador

    def getNomeCoordenador(self):
        if self.coordenador is None:
            return "Curso sem coordenador"
        else:
            return self.coordenador.getNome()

class Aluno:

    def _init_(self, curso):
        self.nome = ""
        if curso is None:
            print("Erro")
            exit()
        else:
            self.curso = curso

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCurso(self):
        return self.curso

    def getNomeCurso(self):
        if self.curso is None:
            print("Aluno sem curso")
        else:
            return self.curso.getNome()

    def setCurso(self, curso):
        if curso is None:
            print("Erro")
            exit()
        else:
            self.curso = curso

class Professor:
    def _init_(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

coordenador = Professor()
coordenador.setNome("Carlos")

curso = Curso()
curso.setNome("Eng Software")
#curso.setCoordenador(coordenador)

aluno = Aluno(curso)
aluno.setNome("Maria")
#aluno.setCurso(curso)

# print(curso.getNome())
# print(aluno.getNome())

print(aluno.getNomeCurso())
print(curso.getNomeCoordenador())