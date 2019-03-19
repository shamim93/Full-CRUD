from django.contrib import admin
from .models import BookList

# Register your models here.
# admin.site.register(BookList)
@admin.register(BookList)
class BookListAdmin(admin.ModelAdmin):
    list_display = ('title','price','author')


