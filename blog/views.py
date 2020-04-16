from django.shortcuts import render,get_object_or_404
from .models import Blog

def blog(request):
    blog_ = Blog.objects
    return render(request,'blog_folder/blog.html',{'blog_':blog_})

# Create your views here.
def details(request,blogid):

    blog_details=get_object_or_404(Blog,pk=blogid)
    return render(request,'blog_folder/details.html',{'b_details':blog_details})
