from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Blog_Post, Sponsor
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def post_list(request):
    posts = Blog_Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Blog_Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

        if is_ajax(request=request):
            term = request.GET.get('term')
            sponsors = Sponsor.objects.filter(name__icontains=term)
            response_content = list(sponsors.values())
            print(response_content)
            return JsonResponse(response_content, safe=False)

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Blog_Post, pk=pk)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save_m2m()  # Required for the many to many when the commit=False is used
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

        if is_ajax(request=request):
            term = request.GET.get('term')
            sponsors = Sponsor.objects.filter(name__icontains=term)
            response_content = list(sponsors.values())
            print(response_content)
            return JsonResponse(response_content, safe=False)

    return render(request, 'blog/post_edit.html', {'form': form})