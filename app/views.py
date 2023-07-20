from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User,Post, Comment, Category
from django.contrib.auth.models import User

# main_page
def main_page(request):
    all_posts = Post.objects.all().order_by('creation_date')
    all_categories = Category.objects.all()
    return(render (request, 'app/main_page.html', {'posteos': all_posts,'categories': all_categories}))

# Post, it will return a post by his id, which will be in the url parameter, also it will get the comments related, an his category
def post(request, id):
    post = Post.objects.get(id=id) 
    my_categories = Category.objects.filter(postId=id)
    all_categories = Category.objects.all()
    all_comments = Comment.objects.filter(postId=id)
    return(render (request, 'app/post.html', {'post': post ,'comments': all_comments,'categories': all_categories, 'categories2': my_categories}))
def newpost(request, userId, categoryId):
    return render(request, 'app/new_post.html', {'userId': userId, 'categoryId': categoryId})

# Login page
def login(request):

    data = {
        'form': LoginForm()
    }

    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('nombreApp:index') #redireccionar a home
        else:
            data["form"] = formulario
    return render(request, 'app/registration/login.html', data)

def register(request):

    data = {
        'form': RegisterForm()
    }
    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            username = request.POST['username']
            email = request.POST['user_email']
            password = request.POST['password']
            try:
                User.objects.create_user(username,email,password)
                formulario.save()
                return redirect('/accounts/login') #redireccionar a home
            except:
                ValueError
                data["mensaje"] = "Usuario ya existente!"
        else:
            data["form"] = formulario
    return render(request, 'app/register.html', data)