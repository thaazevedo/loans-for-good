from django.db import models
from .options_campos import Option

# Modelo usado para definir campos de proposta:
class CamposProposta(models.Model):
  
    fields_type_choice = [
      ('text', 'Texto'),
      ('textarea', 'Texto longo'),
      ('number', 'Valor'),
      ('date', 'Data'),
      ('email', 'E-mail'),
      ('radio', 'Seleção única'),
    ]

    name = models.CharField(verbose_name="nome", max_length=70)
    tipo = models.CharField(verbose_name="tipo", max_length=20, choices=fields_type_choice)
    options = models.ManyToManyField(Option, blank=True, help_text = "Utilizado para campos do tipo Checkbox/Seleção Única")

    def __str__(self):
      return f"Campo: {self.name}. Tipo: {self.tipo}"