from django.forms import ModelForm
from .models import Items

###############################

class AddItems(ModelForm):
    
    class Meta:
        model = Items
        fields = '__all__'






