from django.db import models

# Create your models here.
ESTADOS_CHOICES = (
    ('SP','São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('MG', 'Minas Gerais'),
    ('PR', 'Paraná'),
    ('RS','Rio Grande do Sul')
)
class Clube(models.Model):
    nome = models.CharField(max_length=30)
    estado = models.CharField(choices=ESTADOS_CHOICES, max_length=120, null=True)
    cores = models.CharField(max_length=80, blank=True, null=True)
    ano_fundacao = models.PositiveBigIntegerField(default=0)
    tem_mundial = models.BooleanField(default=False)

def __str__(self):
    return self.nome
