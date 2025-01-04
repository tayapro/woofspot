from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    subject = "Welcome to WoofSpot!"
    email_from = "woofspot.app@gmail.com"
    recipient_list = [user.email]

    # Render email content
    context = {'user': user}
    text_content = render_to_string('event_app/emails/welcome_email.txt', context)
    html_content = render_to_string('event_app/emails/welcome_email.html', context)

    # Send the email
    email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    email.attach_alternative(html_content, "text/html")
    email.send()
