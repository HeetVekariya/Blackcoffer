import pandas as pd
import scrapy
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
import re

# Load the Excel file
df = pd.read_excel('Data\Input.xlsx')

# Create a dictionary
url_dict = dict(zip(df['URL_ID'], df['URL']))

url = url_dict['bctech2011']
print(url)
# Load the Excel file
df = pd.read_excel('Data\Input.xlsx')

# Create a dictionary
url_dict = dict(zip(df['URL_ID'], df['URL']))

url = url_dict['bctech2011']
print(url)

class MySpider(scrapy.Spider):
    name = 'my_spider'

    def start_requests(self):
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # Extract the desired text from the website
        extracted_text = response.xpath('//*[@id="post-5312"]/div[2]/div/div[1]/div//text()').getall()

        # Store only the text from extracted_text
        text_only = ' '.join(extracted_text).strip()

        text = text_only.split('Summarize')[0]
        
        # Save the extracted text to a text file
        with open('Data/Output1.txt', 'w') as f:
            f.write(text)

        # Remove numbers and . char if it is exactly next to a digit
        text = ''.join(c for i, c in enumerate(text) if not (c.isdigit() or (c == '.' and i > 0 and text[i-1].isdigit())))
        
        # Remove non-alphabetic characters
        text = ''.join(c for c in text if c.isalpha() or c.isspace() or c == '.')

        # Replace multiple newlines with a single newline
        text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())

        # Save the extracted text to a text file
        with open('Data/Output.txt', 'w') as f:
            f.write(text)


# Run the spider
if __name__ == "__main__":

    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()


