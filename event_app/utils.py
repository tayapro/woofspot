import os
import re
from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import now


import re

def convert_email_subject(text):
    """
    Convert a snake_case string into a capitalized title-like 
    format suitable for email subjects.

    Parameters:
        text (str): The input string in snake_case format.

    Returns:
        str: The formatted string with spaces instead of 
        underscores and the first letter capitalized.

    Example:
        >>> convert_email_subject("event_created")
        'Event created'
    """
    text_with_spaces = re.sub(r'_', ' ', text)

    return text_with_spaces.capitalize()


def get_event_image(request, event):
    if event.image and event.image.url:
        image_url = event.image.url
    else:
        image_url = os.environ.get("DEFAULT_IMAGE")

    return image_url


def is_in_the_past(date):
    """
    Check if a given date is in the past or today.

    Parameters:
        date (datetime.date): The date to check.

    Returns:
        bool: True if the date is in the past or today, False otherwise.
    """
    return date <= now().date()


def remove_leading_space(event):
    """
    Remove leading spaces from the title, description, and location 
    attributes of a given event object.

    Parameters:
        event (WoofspotEvent): The event object whose fields need trimming.

    Returns:
        None: Modifies the event object in place.
    """
    event.title.strip()
    event.description.strip()
    event.location.strip()


def send_email(user, event, action):
    """
    Sends email notifications based on the specified action.

    Parameters:
        user: The user object representing the recipient of the email.
        event: The event object containing event details.
        action: A string specifying the type of action triggering 
                the email (e.g., 'event_created', 'event_changed').

    Returns:
        None: This function sends emails and does not return any value.
    """

    # Establish a connection to the email server
    with get_connection(host = settings.EMAIL_HOST, 
            port = settings.EMAIL_PORT,  
            username = settings.EMAIL_HOST_USER, 
            password = settings.EMAIL_HOST_PASSWORD, 
            use_tls = settings.EMAIL_USE_TLS
        ) as connection:  
        email_from = settings.EMAIL_HOST_USER
        context = {'user': user, 'event': event} 
        subject = f"{convert_email_subject(action)}: {event.title}"        
        recipient_list = [user.email, ]   

        if action == "event_changed" or action == "event_cancelled":
            attendees = event.attendees.all()
            recipient_list = [attendee for attendee in attendees] + [event.organizer]

            for recipient in recipient_list:
                context = {
                    'user': recipient,
                    'event': event,
                }
        
                text_content = render_to_string(f'event_app/emails/{action}.txt', context)
                html_content = render_to_string(f'event_app/emails/{action}.html', context)

                email = EmailMultiAlternatives(subject, text_content, email_from, [recipient.email],)
                email.attach_alternative(html_content, "text/html")
                email.send()
        
        else:
            text_content = render_to_string(f'event_app/emails/{action}.txt', context)
            html_content = render_to_string(f'event_app/emails/{action}.html', context)  
            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()


def send_contact_us_email(name, email_from, comment):
    """
    Sends an email to the Woofspot team when the contact form is submitted.
    
    Parameters:
        :param name: The name of the user submitting the form.
        :param email_from: The email address of the user.
        :param comment: The comment/message submitted by the user.
    """
        # Establish a connection to the email server
    with get_connection(
        host = settings.EMAIL_HOST,
        port = settings.EMAIL_PORT,
        username = settings.EMAIL_HOST_USER,
        password = settings.EMAIL_HOST_PASSWORD,
        use_tls = settings.EMAIL_USE_TLS,
    ) as connection:
        # Define recipient list and subject
        recipient_list = ["woofspot.app@gmail.com"]
        subject = f"Contact Form Submission from {name}"

        # Prepare email content
        context = {"name": name, "email_from": email_from, "comment": comment}
        text_content = render_to_string("event_app/emails/contact_us_submitted.txt", context)
        html_content = render_to_string("event_app/emails/contact_us_submitted.html", context)

        # Create and send email
        email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()
