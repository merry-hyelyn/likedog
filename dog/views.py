from django.shortcuts import render, redirect, get_object_or_404
from .models import Dog

# Create your views here.
def info(request):
    return render(request, 'info.html')

def home(request):
    return render(request, 'home.html')

def make_print(request):
    return render(request, 'print.html')

def print_new(request):
	return render(request, 'print_new.html')


def enroll(request):
    dog = Dog.objects.all
    return render(request,'enroll.html',{'dog':dog})

def enroll_page(request):
    title = request.GET["title"]
    dog_kind = request.GET['dog_kind']
    dog_date = request.GET['dog_date']
    body = request.GET['body']
    dog = Dog()
    dog.title = title
    dog.dog_date = dog_date
    dog.dog_kind = dog_kind
    dog.body = body
    dog.save()
    return redirect('enroll')

def delete(request, id):
    dog = get_object_or_404(Dog, pk=id)
    dog.delete()
    return redirect('enroll')

def content(request, id):
    dog = get_object_or_404(Dog, pk=id)
    return render(request, 'content.html',{'dog' : dog})