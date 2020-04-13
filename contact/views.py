from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from .forms import ContactForm
from django.conf import settings

def contact(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_voornaam = request.POST.get(
                'contact_voornaam'
            , '')
            contact_achternaam = request.POST.get(
                'contact_achternaam'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_voornaam': contact_voornaam,
                'contact_achternaam': contact_achternaam,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                contact_voornaam + ' heeft een vraag',
                content,
                settings.EMAIL_HOST_USER,
                ['gastrogoos@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })