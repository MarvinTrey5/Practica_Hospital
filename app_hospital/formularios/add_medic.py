from django import forms
class Add_medic(forms.Form):
    nombre=forms.CharField(max_length=100) # LLave para el campo del médico tipo varchar longitud 100 carácteres.
    apellido=forms.CharField(max_length=100) # LLave para el campo de apellido del médico tipo varchar longitud 100 carácteres.
    especialidad=forms.CharField(max_length=100) # Llave para el campo de especialidad del médico tipo varchar longitud 100 carácteres.