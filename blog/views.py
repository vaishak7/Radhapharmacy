from django.shortcuts import render, redirect
from .forms import PostForm
from django.shortcuts import HttpResponse
import requests



def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>') 
def home(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        form = PostForm()

    context = {
        'forms':form
    }

    return render(request, 'blog/base.html', context)
