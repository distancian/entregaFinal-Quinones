from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar
from .models import Productos


class MensajeForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

class UserEditForm(UserChangeForm):

    password = forms.CharField(

        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_password(self):
        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]  
        password2 = self.cleaned_data["password2"]   

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ("imagen",)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['bodega', 'etiqueta', 'precio', 'imagen']        

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Ingrese su nombre.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Ingrese su apellido.')

    class Meta:
        model = User  # Reemplaza 'YourUserModel' con el modelo de usuario que estás utilizando
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')