from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from core.models import Contact
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context ={'home':'active'}
    return render(request,'core/home.html',context)

# def contact(request):
#     context ={'contact':'active'}
#     return render(request,'core/contact.html',context)

# subject=subj,content=message

def contact(request):

    context={'contact':'active'}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subj=request.POST['subject']
        message=request.POST['msg']
        contact=Contact(name=name,email=email, subject=subj,content=message)
        contact.save()

    return render(request,'core/contact.html',context)




def contactus(request):
  if request.method=="POST":
    fm =UserCreationForm(request.POST)
    if fm.is_valid():
     fm.save()
  else:
    fm=UserCreationForm()
  return render(request,'core/contactus.html',{'form':fm,})
