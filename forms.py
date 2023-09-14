from django.forms import ModelForm
from .models import Profile

gender =(
    ('M','M'),('F','F')
)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        # fields = '__all__'
    




