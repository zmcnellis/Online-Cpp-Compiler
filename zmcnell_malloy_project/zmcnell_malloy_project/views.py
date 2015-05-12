from django.shortcuts import render
from django.http import HttpResponse

def home(request):

        context_dict = {'boldmessage': "I am bold font from the context"}


        return render(request, 'home.html', context_dict)
