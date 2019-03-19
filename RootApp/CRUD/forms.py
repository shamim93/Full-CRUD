from django import  forms
from CRUD.models import BookList


class BookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields  = "__all__"
