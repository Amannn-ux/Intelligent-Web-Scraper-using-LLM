import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)  # 10 seconds timeout
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"  

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()
