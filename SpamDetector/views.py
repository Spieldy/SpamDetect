from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import DocumentForm
import os


# Create your views here.
def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'], request.FILES['docfile'].name)
            # Redirect to the document list after POST
            return render(request, 'graph.html')
    else:
        form = DocumentForm() # A empty, unbound form
        return render(request, 'index.html', {'form': form})


def handle_uploaded_file(f, file_name):
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    destination = open(os.path.join(workpath, 'dataset/'+file_name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

