from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class Post(models.Model):

    class Meta:
        verbose_name_plural = "Posts"

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    topic = models.CharField(max_length=25)
    image = models.CharField(max_length=1000, null=True)
    views = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        verbose_name_plural = "Comments"

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text[:25]


class Like(models.Model):

    class Meta:
        verbose_name_plural = "Likes"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now
    )
