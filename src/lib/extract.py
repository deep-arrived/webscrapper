import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    """
    Fetch the content of a webpage and return the parsed text and links.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text from the page
        page_text = soup.get_text(separator="\n", strip=True)

        # Find all unique links on the page
        links = set(a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("https://cloud.google.com/blog/topics/threat-intelligence/"))

        return page_text, links
    except Exception as e:
        return None, set()
