from django.contrib import admin

from .models import Beer, Review, Comment, Favo

admin.site.register([Beer, Review, Comment, Favo])