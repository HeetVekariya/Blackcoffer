
def negative_words(words: list[str]) -> int:
    with open('Data\MasterDictionary\\negative-words.txt', 'r') as f:
        negative_words = f.read().splitlines()
    
    negative_word_count = 0
    for word in words:
        if word.lower() in negative_words:
            negative_word_count += 1

    return negative_word_count


def positive_words(words: list[str]) -> int:
    with open('Data\MasterDictionary\positive-words.txt', 'r') as f:
        positive_words = f.read().splitlines()
    
    positive_word_count = 0
    for word in words:
        if word.lower() in positive_words:
            positive_word_count += 1

    return positive_word_count


def polarity(positive_words: int, negative_words: int) -> float:
    if positive_words + negative_words == 0:
        return 0
    
    return (positive_words - negative_words) / (positive_words + negative_words)

if __name__ == "__main__":
    words = ['good', 'bad', 'good', 'bad', 'good']
    positive_word_count = positive_words(words)
    negative_word_count = negative_words(words)

    print(positive_word_count)
    print(negative_word_count)
    print(polarity(positive_word_count, negative_word_count))