from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs=Job.objects
    print('Jobssss',jobs)
    return render(request,'job/home.html',{'jobs':jobs})
