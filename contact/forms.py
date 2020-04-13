from django import forms
#from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    contact_voornaam = forms.CharField(required=True)
    contact_achternaam = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
#    contact_telefoon = PhoneNumberField(null=False, blank=False, unique=True,required=True)
    content = forms.CharField(
            required=True,
            widget=forms.Textarea
            )
        # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_voornaam'].label = "Voornaam:"
        self.fields['contact_achternaam'].label = "Achternaam"        
        self.fields['contact_email'].label = "E-mail:"
        self.fields['content'].label = "Wat wilt u vertellen?"
        