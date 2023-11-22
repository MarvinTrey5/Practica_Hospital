from django import forms
class Add_pacient(forms.Form):
    nombre=forms.CharField(max_length=100) # Llave para el nombre del campo del paciente tipo varchar longitud 100 carácteres.
    apellido=forms.CharField(max_length=100) # LLave para el apellido del campo del paciente tipo varchar longitud 100 carácteres.
    fecha_nacimiento=forms.DateTimeField() # Llave para el campo de fecha_nacimiento del paciente tipo DateTimeField consta de ej: 2002-05-29 12:00:00
    sexo=forms.CharField(max_length=20) # Llave para el campo de sexo del paciente tipo varchar longitud 20 carácteres.
    altura=forms.FloatField() # Llave para el campo de altura del paciente tipo float ej: 1.84.
    medico_id = forms.IntegerField() # Llave para el camppo de medico_id que se relaciona con el campo id de la tabla medico tipo entero.
