from django.shortcuts import render, redirect 
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):

        return render(request,'index.html')




 # Create a user object
 # from register page 
def create_user(request):
        print(request.POST)
        errors = User.objects.basic_validator(request.POST)
        print(errors)
        if len(errors)>0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        

        return redirect('/home')



# from login page

def login_user(request):
      print(request.POST)
      logged_user = User.objects.filter(email=request.POST['email'])
      if len(logged_user) > 0:
           logged_user = logged_user[0]
           if logged_user.password == request.POST['password']:
              request.session['user'] = logged_user.first_name
              request.session['id'] = logged_user.id
              return redirect('/home')
      return redirect('/')



def home(request):
        if 'user' not in request.session:
            return redirect ('/')

        return render(request,'home.html')

def articles(request):
        if 'user' not in request.session:
            return redirect ('/')

        return render(request, 'articles.html')


def forum(request):
        if 'user' not in request.session:
            return redirect ('/')

        return render(request, 'forum.html')

def shop(request):
        if 'user' not in request.session:
            return redirect ('/')

        return render(request, 'shop.html')

def logout(request):
    
    request.session.flush()
    
    return redirect('/')
