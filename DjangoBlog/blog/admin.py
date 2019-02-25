from django.contrib import admin
from blog.models import User,Article,Category

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(User)
# Register your models here.
