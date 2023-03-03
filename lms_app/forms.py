from django import forms
from .models import Book, Category
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields =  '__all__'
        fields =  [
            'title',
            'auther',
            'photo_book',
            'photo_auther',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'status',
            'category',
            ]
        widgets = {
            'title' : forms.TextInput(
                attrs={
                'class' : 'form-control'
            }),
            'auther' : forms.TextInput(
                attrs={
                'class' : 'form-control'
            }),
            'photo_auther' : forms.FileInput(
                attrs={
                'class' : 'form-control'
            }),
            'photo_book' : forms.FileInput(
                attrs={
                'class' : 'form-control'
            }),
            'pages' : forms.NumberInput(
                attrs={
                'class' : 'form-control'
            }),
            'price' : forms.NumberInput(
                attrs={
                'class' : 'form-control'
            }),
            'retal_price_day' : forms.NumberInput(
                attrs={
                'class' : 'form-control'
            }),
            'retal_period' : forms.NumberInput (
                attrs={
                'class' : 'form-control'
            }),
            'status' : forms.Select(
                attrs={
                'class' : 'form-control'
            }),
            'category' : forms.Select(
                attrs={
                'class' : 'form-control'
            }),
        }
    