## Approach

1. **Problem Analysis:**

   - Thoroughly analyzed the problem statement to understand the deliverables and requirements.
2. **Data Understanding:**

   - Examined the input data and visited several websites from which the data needed to be extracted to comprehend the data structure and content.
3. **Planning:**

   - Formulated a plan to ensure all the required analytical statistics could be calculated in a systematic flow.
4. **Initial Implementation:**

   - Began by writing the code to extract text and calculate the necessary statistics using the Scrapy tool for web extraction.
   - The initial implementation worked successfully for extracting text from a single website.
5. **Issue with Scrapy:**

   - Encountered issues with Scrapy when performing the extraction process in a loop for multiple websites, as Scrapy's reactor does not restart easily.
6. **Switch to Selenium:**

   - Switched from Scrapy to Selenium for web extraction, which handled the loop for multiple websites more effectively.
   - Selenium provided better control and flexibility for web scraping tasks in this context.
7. **Final Output:**

   - Produced the output file as described in the problem statement, ensuring all the required statistics were accurately calculated and presented.


# Output

- Generated text analytics as a deliverable is located at: Result/Output.csv


# Set up

- Install all the required dependacies from `requirements.txt` .
- Run main.py from Scripts folder.
