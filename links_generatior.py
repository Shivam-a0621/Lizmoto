from langchain.tools import DuckDuckGoSearchResults
from extracter import LinkExtractor


search = DuckDuckGoSearchResults()

class get_links:
    def __init__(self,query):
        self.query=query
    
    def links_generator(self):
        self.data=search.run(self.query)
        extract= LinkExtractor(data_string=self.data)
        return extract.extract_links()
            