from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import BLog,Referance
data={
}

def index(request):
    context={
        "blogs":BLog.objects.filter(is_home=True)
    }
    return render(request,"blog/index.html",context)

def blog(request):
    context={
        "blogs":BLog.objects.filter(is_active=True)
    }
    return render(request,"blog/blogs.html",context)

def blog_details(request,slug_field):
    blog = BLog.objects.get(slug_field=slug_field)
    # selectedBLog = None # [e for e in blogs if e["id"] == id]
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBLog = blog
    # selectedBLog = [blog for blog in blogs if blog["id"]==id][0]
    return render(request,"blog/blog-details.html",{"blog" : blog})
    #return HttpResponse("blog details" + str(id))

def referance(request):
    refern = Referance.objects.all()
    return render(request,"blog/referance.html",{"referance":refern})