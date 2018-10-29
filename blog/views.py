import logging
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