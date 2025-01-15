import requests
from django.utils.timezone import now
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import get_connection, EmailMultiAlternatives

def validate_image_url(url, timeout=5):
    """
    Validate if the given URL point to an accessible image resource.

    Parameters:
        url (str): The URL to validate.
        timeout (int): Timeout for the request in seconds.

    Returns:
        bool: True if the URL is valid and accessible, False otherwise.
    """
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200     
    except requests.RequestException as e:
        print(f"Error validating URL {url}: {e}")
        return False


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

    Args:
        user: The user object representing the recipient of the email.
        event: The event object containing event details.
        action: A string specifying the type of action triggering 
                the email (e.g., 'Event Created', 'Event Changed').

    Returns:
        None: This function sends emails and does not return any value.
    """

    # Establish a connection to the email server
    with get_connection(host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS
        ) as connection:  
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [user.email, ]

        context = {'user': user, 'event': event}

        subject = f"{action}: {event.title}"
        if action == "Event Created":
            # Event Created: Email only to the event organizer
            text_content = render_to_string('event_app/emails/event_created.txt', context)
            html_content = render_to_string('event_app/emails/event_created.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Event Changed":
            # Event Changed: Notify all attendees and organizer
            attendees = event.attendees.all()
            recipient_list = [attendee for attendee in attendees] + [event.organizer]

            for recipient in recipient_list:
                context = {
                    'user': recipient,
                    'event': event,
                }
        
                text_content = render_to_string('event_app/emails/event_changed.txt', context)
                html_content = render_to_string('event_app/emails/event_changed.html', context)

                email = EmailMultiAlternatives(subject, text_content, email_from, [recipient.email],)
                email.attach_alternative(html_content, "text/html")
                email.send()
        elif action == "Event Cancelled":
            # Event Cancelled: Notify all attendees
            attendees = event.attendees.all()
            recipient_list = [attendee.email for attendee in attendees]
            text_content = render_to_string('event_app/emails/event_cancelled.txt', context)
            html_content = render_to_string('event_app/emails/event_cancelled.html', context)
            
            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Reservation Confirmed":
            # Reservation Confirmed: Notify the user
            text_content = render_to_string('event_app/emails/reservation_confirmed.txt', context)
            html_content = render_to_string('event_app/emails/reservation_confirmed.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Reservation Cancelled":
            # Reservation Cancelled: Notify the user
            text_content = render_to_string('event_app/emails/reservation_cancelled.txt', context)
            html_content = render_to_string('event_app/emails/reservation_cancelled.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Rating Created":
            # Rating Created: Notify the user
            text_content = render_to_string('event_app/emails/rating_created.txt', context)
            html_content = render_to_string('event_app/emails/rating_created.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()