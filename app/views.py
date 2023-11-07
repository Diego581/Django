from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, Comments, NewPost
from .models import User,Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import User, Post, Comment, Category
from .serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


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
    # Comentarios
    data = {
        'form': Comments()
    }
    owner = Post.objects.filter(userId = id)
    print(owner)
    if request.method == 'POST':
        formulario = Comments(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return(render (request, 'app/post.html', {'post': post ,'comments': all_comments,'categories': all_categories, 'categories2': my_categories, 'data': data, 'myId': id}))

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


def deletepost(request, id):
    posteo = get_object_or_404(Post, id=id)
    posteo.delete()
    return redirect(to="index")

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

#view set de user
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#view set de post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#view set de comment
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#view set de category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#Autenticacion
class PostViewSet(viewsets.ModelViewSet):
    ...
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, ]
        return super(PostViewSet, self).get_permissions()

