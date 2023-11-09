from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions,generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer,  UserSerializer
from .models import Post, Comment, Category
from .forms import LoginForm, CustomUserCreationForm, Comments, NewPost


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
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('nombreApp:index')  # Cambia 'index' al nombre de tu vista principal
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Register page
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('nombreApp:index')  # Cambia 'index' al nombre de tu vista principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})



#VISTAS DESDE LA API

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)

    def perform_update(self, serializer):
        post = Post.objects.get(pk=self.kwargs['pk'])
        if post.userId == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to edit this post.")

    def perform_destroy(self, instance):
        if instance.userId == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this post.")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)

    def perform_update(self, serializer):
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        if comment.userId == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to edit this comment.")

    def perform_destroy(self, instance):
        if instance.userId == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this comment.")

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)