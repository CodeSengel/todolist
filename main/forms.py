from django import forms


class CreateNewList(forms.Form):
    name=forms.CharField(label="Name", max_length=200)
    delet=forms.BooleanField(label='',required=False,widget=forms.CheckboxInput(attrs={'class': 'hidden'}), initial = False)  
  
class CreateTasks(forms.Form):
    text=forms.CharField(label="Text", max_length=200)
    owner=forms.CharField(label="Owner", max_length=200)
    complete=forms.BooleanField(label='',required=False,widget=forms.CheckboxInput(attrs={'class': 'hidden'}))
    delet=forms.BooleanField(label='',required=False,widget=forms.CheckboxInput(attrs={'class': 'hidden'}), initial = True)



    
# widgets = [
            # forms.Select(attrs=attrs, choices=days),
            # forms.Select(attrs=attrs, choices=months),
            # forms.Select(attrs=attrs, choices=years),
        # ]    forms.HiddenInput()