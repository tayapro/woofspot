from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    """
    Sends a welcome email to the user after they successfully sign up.

    This function listens for the `user_signed_up` signal from the allauth
    package and sends a personalized welcome email to the new user. The email
    contains both plain text and HTML versions for improved compatibility
    across email clients.

    Args:
        request: The HTTP request object (passed automatically by the signal).
        user: The user who has just signed up.
        **kwargs: Additional keyword arguments that may be passed with
        the signal.

    Sends an email to the new user with the subject 'Welcome to WoofSpot!'
    and the appropriate email content. It uses a plain text version and
    an HTML version of the email, both rendered using Django's template system.
    """

    subject = "Welcome to WoofSpot!"
    email_from = "woofspot.app@gmail.com"
    recipient_list = [user.email]

    # Render email content
    context = {'user': user}
    text_content = render_to_string('event_app/emails/welcome_email.txt',
                                    context)
    html_content = render_to_string('event_app/emails/welcome_email.html',
                                    context)

    # Send the email
    email = EmailMultiAlternatives(subject, text_content, email_from,
                                   recipient_list)
    email.attach_alternative(html_content, "text/html")

    email.send()
