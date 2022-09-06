from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    email = models.CharField(max_length=100, verbose_name='Correo electronico')
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de eviado')

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering = ['-created']

    def __str__(self):
        return self.name
