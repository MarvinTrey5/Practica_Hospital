from django import forms
class Add_pacient(forms.Form):
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField(max_length=100)
    fecha_nacimiento=forms.DateTimeField()
    sexo=forms.CharField(max_length=20)
    altura=forms.FloatField()
    medico_id = forms.IntegerField()
