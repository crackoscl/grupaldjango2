from django.shortcuts import render
import requests

# Create your views here.

def inicio(request):
    
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    return render(request, 'app/principal.html',{"todos": todos})

