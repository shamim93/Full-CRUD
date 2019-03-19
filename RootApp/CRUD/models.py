from django.db import models
# from django.urls import reverse

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('book_edit', kwargs={'pk':self.pk})
