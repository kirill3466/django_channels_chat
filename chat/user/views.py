from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
