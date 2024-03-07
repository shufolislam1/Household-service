from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    # def save(self, commit= True):
    #     user =  super().save(commit=False)
    #     if commit == True:
    #         user.save() # user model a data save hobe
             
    #         UserAccountModel.objects.create(
    #             user = user,
    #             account_no = 1000000 + user.id
    #         ) 
    #     return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
            
            
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']