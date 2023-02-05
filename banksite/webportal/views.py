from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms import LogInForm

def index(request: HttpRequest) -> HttpResponse:
    # TODO: if authenticated, render index; else redirect to login
    context = { 'name': 'WhoeverYouAre' }
    return render(request, 'index.html', context)

def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            # TODO: Check password_hash from database and perform
            #       authentication via JWT and populate session with
            #       access token.
            return redirect(index)
    return render(request, 'login.html', { 'form': LogInForm() })

def register(request: HttpRequest) -> HttpResponse:
    # TODO: render registration form
    pass