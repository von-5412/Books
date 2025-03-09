from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Book

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'required': True,
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'required': True,
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'required': True,
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
            'required': True,
        })
        
        # Remove help text
        for field in self.fields:
            self.fields[field].help_text = None

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'required': True,
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'required': True,
        })

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pdf', 'public']  # Include the public field

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get user from view
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        book = super().save(commit=False)
        if self.user:
            book.user = self.user  # Assign logged-in user
        if commit:
            book.save()
        return book
