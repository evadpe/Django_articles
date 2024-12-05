from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

# Liste des articles du blog
def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Détails d'un article de blog
def post_detail(request, pk):
    # Tente de récupérer l'article avec l'ID spécifié
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
# Créer un article de blog
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# Modifier un article de blog
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

# Ajouter un commentaire
def add_comment(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

# Modifier un commentaire
def edit_comment(request, pk, comment_pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'post': post, 'comment': comment})

# Supprimer un article de blog
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/delete_post.html', {'post': post})

# Supprimer un commentaire
def delete_comment(request, pk, comment_pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        comment.delete()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/delete_comment.html', {'post': post, 'comment': comment})
