from django.contrib import admin
from .models import Experience,Supply,Rating,Cartypes,ProductAttribute,Category,Transmission

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','supply','rate','id')  


    
admin.site.register(Experience,ArticleAdmin)
admin.site.register(Supply,SupplyAdmin)
admin.site.register(Rating,CommentAdmin) 
admin.site.register(Cartypes)
admin.site.register(Transmission)  
admin.site.register(ProductAttribute) 

admin.site.register(Category)
