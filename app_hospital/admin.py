from django.contrib import admin
from .models import medico, paciente
# Register your models here.
admin.site.register(medico) #Para añadir en pgAdmin desde el login para médico.
admin.site.register(paciente) #Para añadir en pgAdmin desde el login para médico.