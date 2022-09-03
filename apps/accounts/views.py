from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    template = 'accounts/login.html'

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                email=cd['email'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticado com sucesso')

                else:
                    return HttpResponse('Conta desativada')

            else:
                return HttpResponse('Login inválido')

    else:
        form = LoginForm()

    return render(request, template, {'form': form})
