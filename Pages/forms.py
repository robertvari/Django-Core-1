from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'text_field', "placeholder":"Subject"}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'text_field', "placeholder":"Email"}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'text_field', "placeholder":"Message"}), required=True)