from django.db import models

# Create your models here.

class medico(models.Model):
    ID_Medico = models.AutoField(primary_key=True) # Nuestrea primera primary key.
    Nombre = models.CharField(max_length=100) # Para el nombre del Médico.
    Apellido = models.CharField(max_length=100) # Para el apellido del Médico.
    Especialidad = models.CharField(max_length=100) # Para la especialidad del Médico.
    def __str__(self):
        return f"Nombre: {self.Nombre}. Apellido: {self.Apellido}. Especilidad: {self.Especialidad}"
class paciente(models.Model):
    ID_Paciente = models.AutoField(primary_key=True) # La primera primary key.
    Nombre = models.CharField(max_length=100) # Nombre del paciente tipo varchar con longitud de 100 carácteres.
    Apellido = models.CharField(max_length=100) # Apellido del paciente tipo varchar con longitud de 100 carácteres.
    Fecha_Nacimiento = models.DateTimeField() # Para la fecha de nacimiento será en el formato AAAA-MMMM-DDDD HHH:MMM:SS.
    Sexo = models.CharField(max_length=20) # Sexo del paciente tipo varchar con longitud de 20
    Altura  = models.FloatField() # Para la altura del paciente tipo float.
    Medico_ID = models.ForeignKey(medico, on_delete=models.CASCADE) # LLave foránea que se relaciona con el ID_Medico de la 1 tabla medico.
    def __str__(self):
        return f"I_Paciente: {self.ID_Paciente}. Nombre: {self.Nombre}. Apellido: {self.Apellido}. Fecha de Nacimiento: {self.Fecha_Nacimiento}. Sexo: {self.Sexo}. Altura: {self.Altura}. Medico ID: {self.Medico_ID}"