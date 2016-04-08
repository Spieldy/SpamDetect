from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from SpamDetector.forms import UploadFileForm
from SpamDetector.function import Normalizer
from django.core.files.uploadhandler import FileUploadHandler


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            FileUploadHandler.receive_data_chunk(request.FILES, 0)
        return render(request, 'graph.html')
    else:
        form = UploadFileForm()
        return render(request, 'index.html', {'form': form})
