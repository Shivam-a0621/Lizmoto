#  OverView

***Following are the overview of the above codebase***
```
--The above codes will provide the insights of an company and thier market situation
--At first user have to provide an input and area of information rquired.
--The user input is then fed to a langchain agent here  I have used duckduckgo web search
--Then the agent will find the relevent answer to the user input along with the websites
from where it have  gathered the informations.
--Then using re library  all the links present in that optput strings is extracted and stored into a list
--Now here a web scraping fucntion and tool is used to ectract the text information from list of urls provided
--Then that text are saved into an csv formtate for further processing
--Also the text is embedded and  saved into a VECTOR STORE for fast retrival
--Now we can give prompt input and querry information from the data stored.

```


**Dependencies and Libraries**
```
Python
nltk re
bs4 as Beautiful Soup
Also tried selenium
DuckduckGo web search tool
Langchain
Faiss for vector strore (other can also be integrated)
OpenAi 
```

# Sample images 
# LINKS
![LINKS ](https://github.com/Shivam-a0621/Lizmoto/blob/main/images/Screenshot%202024-02-19%20200756.png)https://github.com/Shivam-a0621/Lizmoto/blob/main/images/Screenshot%202024-02-19%20200756.png)


## Response
![LINKS ](https://github.com/Shivam-a0621/Lizmoto/blob/main/images/Screenshot%202024-02-19%20205351.png)https://github.com/Shivam-a0621/Lizmoto/blob/main/images/Screenshot%202024-02-19%20205351.png)

# Raw data
![LINKS ](https://github.com/Shivam-a0621/Lizmoto/blob/main/images/Screenshot%202024-02-19%20200908.png)https://github.com/Shivam-a0621/Lizmoto/blob/main/images/Screenshot%202024-02-19%20200908.png)









