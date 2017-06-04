from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

def approved_comments(self):
    return self.comments.filter(approved_comment=True)
