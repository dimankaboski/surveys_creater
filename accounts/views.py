from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, FormView
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from accounts.models import User
from .forms import RegisterForm


class Login(TemplateView):
    template_name = 'accounts/login.html'
    http_method_names = ['get', 'post']

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('surveys:index')
        else:
            return render(
                request,
                'authentication/login.html',
                {
                    'error': 'Неправильный Email или пароль',
                    'email': email,
                })

    def dispatch(self, request):
        if request.user.is_authenticated:
            return redirect('surveys:index')
        return super().dispatch(request)


class Register(FormView):
    template_name = 'accounts/register.html'
    http_method_names = ['get', 'post']
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        return redirect('auth:login')


@require_http_methods(['GET'])
def logout_view(request):
    logout(request)
    return redirect('/')