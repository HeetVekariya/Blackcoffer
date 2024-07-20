import os

personal_pronouns = {
    'I': 0,
    'me': 0,
    'my': 0,
    'mine': 0,
    'myself': 0,
    'we': 0,
    'us': 0,
    'our': 0,
    'ours': 0,
    'ourselves': 0,
    'you': 0,
    'your': 0,
    'yours': 0,
    'yourself': 0,
    'yourselves': 0,
    'he': 0,
    'him': 0,
    'his': 0,
    'himself': 0,
    'she': 0,
    'her': 0,
    'hers': 0,
    'herself': 0,
    'it': 0,
    'its': 0,
    'itself': 0,
    'they': 0,
    'them': 0,
    'their': 0,
    'theirs': 0,
    'themselves': 0
}

def personal_pronoun_counter(words: list[str]) -> tuple[dict[str, int], int]:
    words = [word.lower() for word in words]
    for pronoun in personal_pronouns.keys():
        if pronoun in words:
            personal_pronouns[pronoun] = words.count(pronoun)

    # Count the total number of personal pronouns
    total = sum(personal_pronouns.values())
    return (personal_pronouns, total)

def remove_stopwords(words: list) -> list:
    stop_words = []
    stop_words_folder = "Data/Stopwords"

    for file_name in os.listdir(stop_words_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(stop_words_folder, file_name)
            with open(file_path, "r") as file:
                stop_words.extend([word.lower() for word in file.read().split() if word != "|"])
    
    with open("Data/stopwords.txt", "w") as file:
        file.write("\n".join(stop_words)) 
    
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

if __name__ == "__main__":
    words = ['I', 'am', 'a', 'student', 'I', 'like', 'to', 'play', 'football']
    print(personal_pronoun_counter(words)[1])
    print("\n\n\n")
    print(remove_stopwords(words))


