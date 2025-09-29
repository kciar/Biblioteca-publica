# biblioteca/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # herda username, first_name, last_name, email, password, is_staff, ...
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.get_full_name() or self.username


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100, blank=True, null=True)
    ano = models.PositiveIntegerField(blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} — {self.autor or 'Autor desconhecido'}"


class Emprestimo(models.Model):
    STATUS_CHOICES = (
        ('EM_ANDAMENTO', 'Em andamento'),
        ('DEVOLVIDO', 'Devolvido'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EM_ANDAMENTO')

    class Meta:
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f"Emprestimo {self.id}: {self.livro} -> {self.usuario}"
