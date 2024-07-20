import pandas as pd
from extract import extract_text
from spliter import splitter
from removeStopwords import personal_pronoun_counter, remove_stopwords
from polarity import positive_words, negative_words, polarity
from calculations import avg_sentencelength, avg_words_per_sentence, word_count, avg_word_length, subjectivity_score, complex_words, fog_index


def main(url_id, url):
    # Initialize the variables
    POSITIVE_WORDS = int(0)
    NEGATIVE_WORDS = int(0)
    POLARITY = float(0)
    SUBJECTIVITY_SCORE = float(0)
    AVG_SENTENCE_LENGTH = float(0)
    PERCENTAGE_OF_COMPLEX_WORDS = float(0)
    FOG_INDEX = float(0)
    AVG_WORDS_PER_SENTENCE = float(0)
    COMPLEX_WORDS = int(0)
    WORD_COUNT = int(0)
    SYLLABLE_PER_WORD = int(0)
    PERSONAL_PRONOUNCE_COUNT = int(0)
    AVG_WORD_LENGTH = float(0)

    # Extract the text from the website
    extract_text(url)

    # Read the extracted text
    with open('Data/Output.txt', 'r') as f:
        text = f.read()

    # Split the text into sentences and words
    sentences, words = splitter(text)

    # Count the number of personal pronouns
    personal_pronouns, PERSONAL_PRONOUNCE_COUNT = personal_pronoun_counter(words)

    # Remove the stopwords
    filtered_words = remove_stopwords(words)

    # Count the number of positive and negative words
    POSITIVE_WORDS = positive_words(filtered_words)
    NEGATIVE_WORDS = negative_words(filtered_words)

    # Calculate the polarity
    POLARITY = polarity(POSITIVE_WORDS, NEGATIVE_WORDS)

    # Calculate the average sentence length
    AVG_SENTENCE_LENGTH = avg_sentencelength(sentences)

    # Calculate the average words per sentence
    AVG_WORDS_PER_SENTENCE = avg_words_per_sentence(words, sentences)

    # Calculate the word count
    WORD_COUNT = word_count(words)

    # Calculate the average word length
    AVG_WORD_LENGTH = avg_word_length(words)

    # Calculate the subjectivity score
    SUBJECTIVITY_SCORE = subjectivity_score(POSITIVE_WORDS, NEGATIVE_WORDS, WORD_COUNT)

    # Calculate the percentage of complex words
    COMPLEX_WORDS, PERCENTAGE_OF_COMPLEX_WORDS, SYLLABLE_PER_WORD = complex_words(words)

    # Calculate the FOG index
    FOG_INDEX = fog_index(AVG_SENTENCE_LENGTH, PERCENTAGE_OF_COMPLEX_WORDS)

    return {
        'URL_ID': url_id,
        'URL': url,
        'POSITIVE SCORE': POSITIVE_WORDS,
        'NEGATIVE SCORE': NEGATIVE_WORDS,
        'POLARITY SCORE': POLARITY,
        'SUBJECTIVITY SCORE': SUBJECTIVITY_SCORE,
        'AVG SENTENCE LENGTH': AVG_SENTENCE_LENGTH,
        'PERCENTAGE OF COMPLEX WORDS': PERCENTAGE_OF_COMPLEX_WORDS,
        'FOG INDEX': FOG_INDEX,
        'AVG NUMBER OF WORDS PER SENTENCE': AVG_WORDS_PER_SENTENCE,
        'COMPLEX WORD COUNT': COMPLEX_WORDS,
        'WORD COUNT': WORD_COUNT,
        'SYLLABLE PER WORD': SYLLABLE_PER_WORD,
        'PERSONAL PRONOUNS': PERSONAL_PRONOUNCE_COUNT,
        'AVG WORD LENGTH': AVG_WORD_LENGTH
    }


if __name__ == "__main__":
    # Load the Excel file
    df = pd.read_excel('Data\Input.xlsx')

    # Create a dictionary
    url_dict = dict(zip(df['URL_ID'], df['URL']))
    
    # Create a dataframe to store the results
    columns=['URL_ID', 
             'URL', 
             'POSITIVE SCORE', 
             'NEGATIVE SCORE', 
             'POLARITY SCORE', 
             'SUBJECTIVITY SCORE', 
             'AVG SENTENCE LENGTH', 
             'PERCENTAGE OF COMPLEX WORDS', 
             'FOG INDEX', 
             'AVG NUMBER OF WORDS PER SENTENCE', 
             'COMPLEX WORD COUNT', 
             'WORD COUNT', 
             'SYLLABLE PER WORD', 
             'PERSONAL PRONOUNS', 
             'AVG WORD LENGTH'
            ]
    
    df = pd.DataFrame(columns=columns)
    
    website = 1
    for url_id, url in url_dict.items():
        temp_dict = main(url_id, url)
        df = pd.concat([df, pd.DataFrame(temp_dict, index=[0])], ignore_index=True)

        print("\n\n\n")
        print(f"Website: {website} is under process.......", "\033[92m")
        print(f"Current shape of the dataframe: {df.shape}", "\033[0m")

    # Save the results to an Excel file
    df.to_csv('Result/Output.csv', index=False)

