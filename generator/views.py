from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 10))

    chars = string.ascii_lowercase

    if request.GET.get('uppercase'):
        chars += string.ascii_uppercase

    if request.GET.get('numbers'):
        chars += string.digits

    if request.GET.get('symbols'):
        chars += string.punctuation

    pwd = ''.join(random.choice(chars) for _ in range(length))

    return render(request, 'generator/home.html', {'password': pwd})
