from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your Account has been created!! You can log in now!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })
    
def profile(request):
    return render(request, "users/profile.html")