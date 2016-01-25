from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.files import File
from django.http import HttpResponse
from django import forms
from django_ace import AceWidget
import subprocess
import os
from os.path import join
import zmcnell_malloy_project

class EditorForm(forms.Form):
    text = forms.CharField(widget=AceWidget(mode='c_cpp', theme='clouds', showprintmargin=False))
    #text = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'css'}))

def index(request):
    context = RequestContext(request)
    terminal_output = '$ '

    if request.method=='POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            text = cd.get('text')
	    if 'compile' in request.POST:
                #print("COMPILING...\n" + a + "\n")
		with open('media/myprogram.cpp', 'w+') as fd:
		    myfile = File(fd)
                    myfile.write(text)
                myfile.closed
                fd.closed
                proc = subprocess.Popen(['g++', 'media/myprogram.cpp', '-o', 'media/myprogram'], stderr=subprocess.PIPE)
		terminal_output += "g++ myprogram.cpp\n"
                terminal_output += proc.stderr.read()
		#print("OUTPUT...\n" + terminal_output)
            elif 'execute' in request.POST:
                #print("EXECUTING..." + a + "\n")
		proc = subprocess.Popen('./media/myprogram', stdout=subprocess.PIPE)
		terminal_output += "./media/myprogram\n"
                terminal_output += proc.stdout.read()
                #print("OUTPUT...\n" + terminal_output)

    else:
        form = EditorForm()

    context_dict = {'form': form, 'terminal_output': terminal_output}

    return render_to_response('c_compiler/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)

    context_dict = {'boldmessage': "YAY!"}

    return render_to_response('c_compiler/about.html', context_dict, context)

