import requests
from bs4 import BeautifulSoup

def get_word_example(word):
    # URL for Longman dictionary search
    url = f"https://www.ldoceonline.com/dictionary/{word}"

    # Send GET request
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failedto retrieve data for {word}. HTTP Status code: {response.status_code}")
        return

    # Parsethe page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the example sentence section in the page
    examples = soup.find_all('span', class_='examp')

    if examples:
        print(f"Examples for the word '{word}':")
        for i, example in enumerate(examples, 1):
            print(f"{i}. {example.text.strip()}")
        else:
            print(f"No example sentence found for '{word}'.")

# Example usage
word = input("Enter a word to search for: ")
get_word_example(word)              
