import requests
from django.utils.timezone import now

def validate_image_url(url, timeout=5):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200     
    except requests.RequestException:
        pass

# Return True if event date is in the past
def is_in_the_past(date):
    return date <= now().date()

# TODO: Move from views send_email function