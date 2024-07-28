from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import Truncator

user = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    dateposted = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateField(auto_now=True)
    likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="categories")

    def truncated_content(self):
        return Truncator(self.content).words(50, truncate="...")

    def __str__(self):
        return self.title

class Comments(models.Model):
    # Foreign key => one to many relation, means one article can have many comments
    # auto_now_add => whenever the comment is made and auto_add will be whenever it is updated
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.TextField()
    dateposted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"

