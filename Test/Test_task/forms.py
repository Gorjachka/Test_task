from django import forms
from .models import Users #Groups


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'created', 'group']  # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'created': forms.DateField(),
                   'group': forms.TextInput(attrs={'class': 'form-control'})#change to textselect
                   }


# class GroupsForm(forms.ModelForm):
#     class Meta:
#         model = Groups
#         fields = ['Name', 'Descriptions']  # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
#         widgets = {'Name': forms.TextInput(attrs={'class': 'form-control'}),
#                    'Descriptions': forms.TextInput(attrs={'class': 'form-control'}),
#                    }
