from django.contrib import admin
from . models import *



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'is_published', 'created_at')
#     list_display_links = ('id','name') 
#     list_filter = ('price',)
#     list_editable = ('is_published',)
#     search_fields = ('name', 'price')
#     ordering = ('price',)
    

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Sale)

admin.site.register(Cart)
admin.site.register(Favourite)
 




