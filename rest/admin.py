from django.contrib import admin
from rest.models import Category,Food,Comment,Cook
# Register your models here.

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','user']
#     list_filter = ['user','title','body']
#     search_fields = ['id','title','body']
#     # prepopulated_fields = {'slug':('name',)}


admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Comment)
admin.site.register(Cook)