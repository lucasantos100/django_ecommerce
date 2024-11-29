from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from formulario.models import Formulario

User = get_user_model()

#formulario de contato
class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu nome completo"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email"
            }
        )
    )
    numero = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu número de telefone",
                "type": "tel"
            }
        ),
        max_length=15,  # Limite de caracteres, pode ser ajustado conforme necessário
        required=False  # Deixe o campo opcional ou altere para True, se necessário
    )
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escolha a data",
                "type": "date"
            }
        )
    )
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escolha o horário",
                "type": "time"
            }
        )
    )
    servicos = forms.MultipleChoiceField(
        choices=[
            ("Apoio Administrativo e Gestão Empresarial", "Apoio Administrativo e Gestão Empresarial"),
            ("Terceirização Financeira e Gestão de Recursos", "Terceirização Financeira e Gestão de Recursos"),
            ("Planejamento e Organização Administrativa", "Planejamento e Organização Administrativa"),
            ("Consultoria em Licitações Públicas e Privadas", "Consultoria em Licitações Públicas e Privadas"),
            ("Desenvolvimento de Sistemas", "Desenvolvimento de Sistemas")
        ],
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check"}
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua mensagem"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email

#formulario de login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#formulario de registro
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse email já existe, tente outro!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("As senhas informadas devem ser iguais!")
        return data

#formulario de formulario
class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'email', 'telefone', 'data', 'horario', 'mensagem']
    
    # Personalizando o campo nome
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu nome completo"
            }
        )
    )

    # Personalizando o campo email
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email"
            }
        )
    )

    # Personalizando o campo telefone
    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu número de telefone",
                "type": "tel"
            }
        ),
        max_length=15,  # Limite de caracteres, pode ser ajustado conforme necessário
        required=False  # Deixe o campo opcional ou altere para True, se necessário
    )

    # Personalizando o campo data
    data = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escolha a data",
                "type": "date"
            }
        )
    )

    # Personalizando o campo horario
    horario = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escolha o horário",
                "type": "time"
            }
        )
    )

    # Personalizando o campo mensagem
    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua mensagem"
            }
        )
    )