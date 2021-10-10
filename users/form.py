from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        label = {'first_name':'Name'}
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})