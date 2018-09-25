from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


class IndexView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['comments'] = Comment.objects.all()
        return context


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['comments'] = Comment.objects.all()
        return context