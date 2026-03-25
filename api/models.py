from django.db import models

class Estudantes(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    quant_semestres = models.IntegerField()
    vagas = models.IntegerField()

    def __str__(self):
        return self.nome

class Matriculas(models.Model):
    estudante = models.ForeignKey(Estudantes, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.estudante.nome} e {self.curso.nome}'
