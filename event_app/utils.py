import requests

def validate_image_url(url, timeout=5):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200     
    except requests.RequestException:
        pass

# TODO: Move from views send_email function