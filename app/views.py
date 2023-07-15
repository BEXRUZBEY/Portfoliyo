from django.shortcuts import render, redirect

from app.form import ContactForm
from app.models import Skill, Blog


def index_view(request):
    blogs = Blog.objects.order_by('-id')[:3]
    skills = Skill.objects.all()
    return render(request=request,
                  template_name='app/index.html',
                  context={"skills":skills,
                           "blogs":blogs})


def blog_list(request):
    blogs = Blog.objects.order_by('-id')
    return render(request=request,
                  template_name='app/blog_list.html',
                  context={"blogs": blogs}
                  )


def blog_details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request=request,
                  template_name='app/blog_detayls.html',
                  context={"blog":blog})


def contact_view(request):
    if request.method == "POST":
       form = ContactForm(data=request.POST)
       if form.is_valid():
           form.save()
           return redirect('index')
       form = ContactForm()
       return render(request=request,
                     template_name='app/index.html',
                     context={"form":form})
