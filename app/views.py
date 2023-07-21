from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, Comments, NewPost
from .models import User,Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# main_page
def main_page(request):
    all_posts = Post.objects.all().order_by('creation_date')
    all_categories = Category.objects.all()
    return(render (request, 'app/main_page.html', {'posteos': all_posts,'categories': all_categories}))

# Post, it will return a post by his id, which will be in the url parameter, also it will get the comments related, an his category
def post(request, id):
    # Posteo
    post = Post.objects.get(id=id)
    my_categories = Category.objects.filter(postId=id)
    all_categories = Category.objects.all()
    all_comments = Comment.objects.filter(postId=id)
    comparador = post.userId.id
    owner = 300
    try: 
        owner = User.objects.get(id = comparador)
        owner = owner.id
    except:
        ValueError
    print(owner, 'current user: ', request.user.id)
    # Comentarios
    data = {
        'form': Comments()
    }

    if request.method == 'POST':
        formulario = Comments(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return(render (request, 'app/post.html', {'post': post ,'comments': all_comments,'categories': all_categories, 'categories2': my_categories, 'data': data, 'owner': owner, 'owner': owner, 'postId': id}))

# New Post
def newpost(request):
    all_categories = Category.objects.all()
    # Datos del Post
    data = {
        'form': NewPost()
    }
    if request.method == 'POST':
        formulario = NewPost(request.POST)
        if formulario.is_valid():
            print('Se guardo un nuevo formulario de user_id:', request.user)
            formulario.save()
            return redirect('nombreApp:index') #redireccionar a home
        else:
            data["form"] = formulario
    return render(request, 'app/new_post.html', {'categories': all_categories, 'data': data})

# Delete Post
def deletepost(request, id):
    post = Post.objects.get(id=id)
    try:
        post.delete()
        return redirect('nombreApp:index')
    except:
        ValueError

# Delete Comment
def deletecomment(request,id):
    comment = Comment.objects.get(id=id)
    try:
        comment.delete()
        return redirect('nombreApp:index')
    except:
        ValueError


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