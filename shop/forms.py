
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, Store, Product


class RegistrationForm(UserCreationForm):
    """Handle user registration with buyer and vendor role selection."""

    email = forms.EmailField(required=True)

    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('vendor', 'Vendor'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        """Define the user model and registration form fields."""

        model = User
        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2'
        ]


class ReviewForm(forms.ModelForm):
    """Allow customers to submit product ratings and reviews."""

    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Rating (1-5)"
    )

    class Meta:
        """Define the model and fields used for product reviews."""

        model = Review
        fields = ['rating', 'comment']


class StoreForm(forms.ModelForm):
    """Allow vendors to create and update their stores."""

    class Meta:
        """Define the model and fields used for store information."""

        model = Store
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    """Allow vendors to create and update products in their stores."""

    class Meta:
        """Define the model and fields used for product information."""

        model = Product
        fields = [
            'store',
            'name',
            'description',
            'price',
            'stock'
        ]

    def __init__(self, *args, **kwargs):
        """Initialize the form and limit store choices to the current vendor."""
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['store'].queryset = Store.objects.filter(
                owner=user
            )
        else:
            self.fields['store'].queryset = Store.objects.none()
