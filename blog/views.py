import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from .models import Post, Comment, Like


class IndexView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'blog/blog.html'
    queryset = Post.objects.order_by('-published_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        for post in context['posts']:
            post.number_of_likes = post.like_set.all().count()
            post.number_of_comments = post.comment_set.all().count()
        context['comments'] = Comment.objects.all()
        if not self.request.user.is_anonymous:
            print("User: {}".format(self.request.user))
            context['user_likes'] = Like.objects.filter(user=self.request.user) \
                .values_list('post_id', flat=True)
        else:
            context['user_likes'] = None
        return context


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(self.get_object().pk)
        context['comments'] = Comment.objects.all()
        post = Post.objects.get(pk=self.get_object().pk)
        post.views += 1
        post.save()
        return context


@login_required
def like_post(request, pk):
    if request.method == 'POST' and request.user:
        post = Post(pk=pk)
        user = User(pk=request.user.id)
        if 'like-post-btn' in request.POST:
            if not Like.objects.filter(user=user, post=post).first():
                like = Like(user=user, post=post)
                like.save()
                print("Post LIKED!")
            else:
                print("Already liked this post!")
        elif 'unlike-post-btn' in request.POST:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            print("Post UNLIKED!")
    return redirect('blog:post_list')
