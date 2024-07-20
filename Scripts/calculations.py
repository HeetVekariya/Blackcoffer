import nltk
from nltk.corpus import cmudict

# Check if the CMU Pronouncing Dictionary is already downloaded
try:
    cmudict.dict()
except LookupError:
    print("Downloading cmudict...")
    nltk.download('cmudict')

def avg_sentencelength(sentences: list[str]) -> float:
    total_length = 0

    for sentence in sentences:
        total_length += len(sentence)

    if len(sentences) == 0:
        return 0
    
    return total_length / len(sentences)

def avg_words_per_sentence( sentences: list[str]) -> float:
    total_words = 0

    for sentence in sentences:
        total_words += len(sentence.split())

    if len(sentences) == 0:
        return 0
    
    return total_words / len(sentences)

def word_count(words: list[str]) -> int:
    return len(words)

def avg_word_length(words: list[str]) -> float:
    total_length = 0

    for word in words:
        total_length += len(word)

    if len(words) == 0:
        return 0
    
    return total_length / len(words)

def subjectivity_score(positive_words: int, negative_words: int, total_words: int) -> float:
    if total_words == 0:
        return 0
    
    return (positive_words + negative_words) / float(total_words)

def complex_words(words: list[str]) -> tuple[int, float, float]:
    # Load the CMU Pronouncing Dictionary
    d = cmudict.dict()

    def count_syllables(word):
        """
        Count the syllables in a word using the CMU Pronouncing Dictionary.
        """
        if word.lower() in d:
            return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
        else:
            return 0  # Words not found in the dictionary are treated as having 0 syllables

    complex_words = []
    total_syllables = 0

    for word in words:
        syllables = count_syllables(word)
        total_syllables += syllables

        if syllables >= 3:
            complex_words.append(word)

    # Calculate the percentage of complex words
    if len(words) == 0:
        percentage_of_complex_words = 0
    percentage_of_complex_words = len(complex_words) / len(words)

    # Calculate the average syllables per word
    if len(words) == 0:
        avg_syllables_per_word = 0
    avg_syllables_per_word = total_syllables / len(words)

    return len(complex_words), percentage_of_complex_words, avg_syllables_per_word

def fog_index(avg_sentence_length: float, percentage_of_complex_words: float) -> float:
    return 0.4 * (avg_sentence_length + percentage_of_complex_words)