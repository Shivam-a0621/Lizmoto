import re
class LinkExtractor:
    def __init__(self, data_string):
        self.data_string = data_string

    def extract_links(self):
        url_pattern = r'https?://\S+?(?=\s*\])'
        links = re.findall(url_pattern, self.data_string)
        return links
    
    
    
