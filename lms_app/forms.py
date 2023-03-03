from django import forms
from .models import Book, Category
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields =  '__all__'
        fields =  [
            'title',
            'auther',
            'photo_auther',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'status',
            'category',
            ]
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }
    