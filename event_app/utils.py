import requests
from django.utils.timezone import now
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import get_connection, EmailMultiAlternatives

def validate_image_url(url, timeout=5):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200     
    except requests.RequestException:
        pass


# Return True if event date is in the past
def is_in_the_past(date):
    return date <= now().date()


def remove_leading_space(event):
    event.title.strip()
    event.description.strip()
    event.location.strip()


def send_email(user, event, action):
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
            text_content = render_to_string('event_app/emails/event_created.txt', context)
            html_content = render_to_string('event_app/emails/event_created.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Event Changed":
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
            attendees = event.attendees.all()
            recipient_list = [attendee.email for attendee in attendees]
            text_content = render_to_string('event_app/emails/event_cancelled.txt', context)
            html_content = render_to_string('event_app/emails/event_cancelled.html', context)
            
            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Reservation Confirmed":
            text_content = render_to_string('event_app/emails/reservation_confirmed.txt', context)
            html_content = render_to_string('event_app/emails/reservation_confirmed.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Reservation Cancelled":
            text_content = render_to_string('event_app/emails/reservation_cancelled.txt', context)
            html_content = render_to_string('event_app/emails/reservation_cancelled.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Rating Created":
            text_content = render_to_string('event_app/emails/rating_created.txt', context)
            html_content = render_to_string('event_app/emails/rating_created.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()