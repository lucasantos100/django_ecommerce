from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ContactForm, LoginForm, RegisterForm, FormularioForm, ForgotPasswordForm

from formulario.models import Formulario

from Contatos.models import Contato


def home_page(request):
    context = {
                    "title": "KGB SA",
                    "content": "Atendimento original e personalizado voltado para modalidade de licitações.",
              }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
                    "title": "About Page",
                    "content": "Bem vindo a About Page"
              }
    return render(request, "about/view.html", context)

def contact_page(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Salva o formulário no banco de dados
            contact_form.save()
            # Se o formulário for válido, redireciona para uma página de sucesso ou exibe uma mensagem
            return redirect('formulario_sucesso_contact')  # Você pode substituir 'success' com o nome da URL que deseja redirecionar após o sucesso
    else:
        contact_form = ContactForm()

    context = {
        "title": "Contato - KGB Solutions",
        "content": "Bem-Vindo à Página de Contato",
        "form": contact_form,
    }

    return render(request, "contact/view.html", context)
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
    print("User logged in")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        print(user)
        #print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "auth/login.html", context)


def logout_page(request):
    logout(request)
    request.session['logout_message'] = "Você foi deslogado com sucesso!"
    return redirect("/login")

def clear_logout_message(request):
    request.session.pop('logout_message', None)
    return JsonResponse({'status': 'ok'})


User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect('/login')
    
    context = {
                    "form": form
              }
    return render(request, "auth/register.html", context)

def lista_formularios(request):
    formularios = Formulario.objects.all()  # Recupera todos os formulários
    return render(request, 'formularios/lista.html', {'formularios': formularios})

def mostrar_formulario(request):
    if request.method == 'POST':  # Verificando se o formulário foi enviado
        form = FormularioForm(request.POST)  # Criando um formulário com os dados recebidos
        if form.is_valid():  # Verificando se o formulário é válido
            form.save()  # Salvando os dados no banco
            return redirect('formulario_sucesso')  # Redirecionando para uma página de sucesso
    else:
        form = FormularioForm()  # Criando um formulário vazio para exibir
    return render(request, 'formularios/formulario.html', {'form': form})

# View de sucesso (após o formulário ser enviado com sucesso)
def formulario_sucesso(request):
    return render(request, 'formularios/sucesso.html')

def formulario_sucesso_contato(request):
    return render(request, 'contact/sucesso.html')

#formulario de mudar senha herdado do proprio django
@login_required
def mudar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # Atualiza a senha do usuário
            form.save()
            # Atualiza a sessão para que o usuário não precise fazer login novamente
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('/login')  # Redireciona para a página de login ou qualquer página desejada
        else:
            messages.error(request, 'Erro ao alterar a senha. Por favor, tente novamente.')
    else:
        # Exibe o formulário para mudança de senha
        form = PasswordChangeForm(user=request.user)

    return render(request, 'auth/mudarsenha.html', {'form': form})

@login_required
def user_profile(request):
    user = request.user  # Obtém o usuário logado
    return render(request, 'auth/perfil.html', {'user': user})

#pagina de servicos (totalmente html funcional, gerados por lucas KAUAN DOS ANJOS)

def servico_1(request):
    return render(request, "servicos/servico_1.html")

def servico_2(request):
    return render(request, "servicos/servico_2.html")

def servico_3(request):
    return render(request, "servicos/servico_3.html")

def servico_4(request):
    return render(request, "servicos/servico_4.html")

def servico_5(request):
    return render(request, "servicos/servico_5.html")

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                password = user.password  # Aviso: a senha é armazenada criptografada no banco de dados
                return JsonResponse({'status': 'success', 'message': f'Sua senha é: {password}'})
            except User.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'E-mail não encontrado.'})
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})