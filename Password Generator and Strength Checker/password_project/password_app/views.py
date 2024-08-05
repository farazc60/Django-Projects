from django.shortcuts import render
from .forms import PasswordForm
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    strength = {'length': len(password) >= 12,
                'lowercase': any(c.islower() for c in password),
                'uppercase': any(c.isupper() for c in password),
                'digits': any(c.isdigit() for c in password),
                'special': any(c in string.punctuation for c in password)}
    return strength

def home(request):
    password = None
    strength = None
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            password = generate_password(length)
            strength = check_strength(password)
    else:
        form = PasswordForm()
    return render(request, 'home.html', {'form': form, 'password': password, 'strength': strength})