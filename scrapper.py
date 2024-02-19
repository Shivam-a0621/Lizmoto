import requests
from bs4 import BeautifulSoup


        
def stripped_webpage(webpage):
        response = requests.get(webpage)
        html_content = response.text

        def strip_html_tags(html_content):
            soup = BeautifulSoup(html_content, "html.parser")
            stripped_text = soup.get_text()
            return stripped_text

        stripped_content = strip_html_tags(html_content)

        # if len(stripped_content) > 4000:
        #     stripped_content = stripped_content[:4000]
        return stripped_content
    
