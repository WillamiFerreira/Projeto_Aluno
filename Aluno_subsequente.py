from aluno import Aluno

class Aluno_Subsequente(Aluno):
    def __init__(self, matricula, nome) -> None:
        super().__init__(matricula, nome)
    
    def get_resultado(self):
        if (self.media >= 6):
            return "Aprovado"
        return "Reprovado"

        
        