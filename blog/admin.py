from django.contrib import admin

# Register your models here.
from .models import Author,Category, Post,Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    prepopulated_fields = {'slug': ('title',)}
class CatAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}  
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'post', 'created', 'active') 
    list_filter = ('active', 'created', 'updated') 
    search_fields = ('name', 'email', 'body') 

admin.site.register(Author)

admin.site.register(Category,CatAdmin)

admin.site.register(Post,ArticleAdmin)
