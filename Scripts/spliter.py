def splitter(text: str) -> tuple[list[str], list[str]]:
    # Split the text into sentences
    sentences = text.split('.')
    
    # Make list of individual words
    words = []
    for sentence in sentences:
        words.extend(sentence.split())

    return sentences, words

if __name__ == "__main__":
    text = "This is a sample sentence. This is another sample sentence."
    sentences, words = splitter(text)
    print(sentences)
    print(words)