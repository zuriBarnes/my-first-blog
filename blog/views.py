from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'blog/post_list.html', {"posts": posts})



def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})