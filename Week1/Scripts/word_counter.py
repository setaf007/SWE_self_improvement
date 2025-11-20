import re
from collections import Counter

STOPWORDS = {
    'the', 'is', 'and', 'in', 'to', 'of', 'a', 'that', 'it', 'on', 'for',
    'with', 'as', 'was', 'at', 'by', 'an', 'be', 'this', 'from', 'or', 'are',
    'but', 'not', 'have', 'they', 'you', 'we', 'his', 'her', 'their', 'its'
}

# Read the file
def read_file(filepath : str) -> str:
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
# Normalize and tokenize the text
def tokenize(text : str) -> list:
    text = text.lower()

    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuations:
        text = text.replace(char, ' ')

    words = text.split()
    return words

# tokenize and remove stopwords
def tokenize_and_filter(text : str) -> list:
    text = text.lower()

    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuations:
        text = text.replace(char, ' ')

    words = text.split()

    return [word for word in words if word not in STOPWORDS]

# word count
def count_words(words : list) -> Counter:
    return Counter(words)

# Display top N words
def display_top_words(word_counts : Counter, n : int) -> None:
    for word, count in word_counts.most_common(n):
        print(f"{word}: {count}")

def word_frequency(filepath : str, top_n : int = 10) -> None:
    text = read_file(filepath)
    words = tokenize(text)
    filtered_words = tokenize_and_filter(text)
    word_counts = count_words(words)
    filtered_word_counts = count_words(filtered_words)
    print(f"Top {top_n} words (including stopwords):")
    display_top_words(word_counts, top_n)
    print(f"\nTop {top_n} words (excluding stopwords):")
    display_top_words(filtered_word_counts, top_n)

if __name__ == "__main__":
    word_frequency('sample.txt', top_n=5)



