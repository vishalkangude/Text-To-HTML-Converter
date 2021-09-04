from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from . import BoldItalicReader as BIR
from .import Indenter as I
import mimetypes
import os


# Create your views here.
def Home(request):
    return render(request, 'index.html', {'output' : 'You output is printed here'})

def Convert(request):
    if request.method == 'POST' and request.FILES['inpfile']:
        myfile = request.FILES['inpfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        BIR.BoldItalicReader(filename)
        I.Indentation()

        f = open('base.html', 'r')
        context = f.read()
        print(context)
        f.close()
        return render(request, 'index.html', {'output' : context})
    
    else:
        return HttpResponse("Error")

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'base.html'
    path = open(filename, 'r')
    mime_type, _ = mimetypes.guess_type(filename)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def Copy(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'base.html'
    path = open(filename, 'r')
    context = path.read()
    
    import pyperclip

    pyperclip.copy(context)

    return render(request, 'index.html', {'output' : context, 'alert': 'Text Copied'})