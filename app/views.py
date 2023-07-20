from django.shortcuts import render
from .models import User,Post, Comment, Category

# Index 
def index(request):
    all_posts = Post.objects.all().order_by('creation_date')
    all_categories = Category.objects.all()
    return(render (request, 'app/index.html', {'posteos': all_posts,'categories': all_categories}))

# Post, it will return a post by his id, which will be in the url parameter, also it will get the comments related, an his category
def post(request, id):
    post = Post.objects.get(id=id) 
    my_categories = Category.objects.filter(postId=id)
    all_categories = Category.objects.all()
    all_comments = Comment.objects.filter(postId=id)
    return(render (request, 'app/post.html', {'post': post ,'comments': all_comments,'categories': all_categories, 'categories2': my_categories}))

