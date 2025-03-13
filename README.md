# Sentencify: Word-to-Sentence Generator for Vocabulary Retention

**Senctencify** is a Python script designed to help non-native English speakers enhance their vocabulary retention by providing example sentences for any given word. By parsing data from the [Longman Dictionary of Contemporary English](https://www.ldoceonline.com/), the script generates sample snetences that contextualize vocabulary, helping users learn and remember words more effectively.

## Features
- **Word-to-Sentence Mapping**: For any word input, Sentencify fetches example sentences from LDOCE.
- **Contextual Learning**: The sentences retrieved help learners understand how the word is used in real-life contexts, improving memory retention.
- **Easy-to-Use** : A simple script that can be run in any python environment.

## Installation 
1. **Clone the repository**
  ```bash
  git clone https://github.com/Farzad659/Sentencify.git
  cd sentencify
  ```
2. **Install requiered dependencies**:
  sentencify requires the following python libraries:
  - `requests`: To fetch HTML content from LDOC.
  - `beautifulsoup4`: To parse the HTML and extract relevant data.
  You can install the required libraries by running:
  ```bash
  pip install requests beautifulsoup4
  ```
## Usage
1. **Run the script**:
   After installation, you can run the script from the command line. The script will prompt you to enter a word to search for. For example:
   ```bash
   pyhton generate_sentence.py
   ```
   **Example Output**:
   ```bash
   Enter a word to search for: study
   ```
   Once you enter a word (e.g., `study`), the script will fetch a sentence containing that word from the LDOCE website and display it in the terminal.
2. **Example Output**:
   after entering the word, you might seesomething like:
   ```bash
   Example sentence: "She decided to study biology at university."
   ```
## Requirements
* Python 3.x
* requests library
* beautifulsoup4 library
## Contributing
Contributions are welcome! If you'd like to improve the script, feel free to fork the repository, create a branch, and submit pull request.
   
