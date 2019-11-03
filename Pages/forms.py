from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"text_field", "placeholder":"Name"}), 
    max_length=200, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"text_field", "placeholder":"Email"}), required=True)

    message = forms.CharField(widget=forms.Textarea(
        attrs={"class":"text_field", "placeholder":"Message"}), 
        required=True)