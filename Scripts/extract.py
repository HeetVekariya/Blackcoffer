from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extract_text(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)  # wait for the page to load

    # Example of extracting text from a specific element
    text = driver.find_element(By.XPATH, '/html/body/div[6]/article/div[2]/div/div[1]/div/div[2]').text
    driver.quit()

    text = text.split('Summarize')[0]

    # Remove numbers and . char if it is exactly next to a digit
    text = ''.join(c for i, c in enumerate(text) if not (c.isdigit() or (c == '.' and i > 0 and text[i-1].isdigit())))

    # Remove non-alphabetic characters
    text = ''.join(c for c in text if c.isalpha() or c.isspace() or c == '.')

    # Replace multiple newlines with a single newline
    text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())

    # Save the extracted text to a text file
    with open('Data/Output.txt', 'w') as f:
        f.write(text)
        