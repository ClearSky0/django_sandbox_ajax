from django.contrib import admin
from .models import Blog_Post, Publication, Sponsor, Tag

admin.site.register(Blog_Post)
admin.site.register(Tag)
admin.site.register(Publication)
admin.site.register(Sponsor)