from django import forms
from .models import docinfo

class chk(forms.ModelForm):
    class Meta:
        model = docinfo
        fields = ('chk_list','status','comments')
