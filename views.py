from django.shortcuts import render, redirect
from .utils import get_user_by_username, create_user
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = get_user_by_username(username)
        if user and user['password'] == password:
            request.session['user'] = username
            return redirect('home')
        messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if create_user(username, password):
            messages.success(request, 'Usuario registrado con éxito. Inicia sesión.')
            return redirect('login')
        messages.error(request, 'El usuario ya existe.')
    return render(request, 'register.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def home_view(request):
    if 'user' not in request.session:
        return redirect('login')
    return render(request, 'home.html', {'user': request.session['user']})
