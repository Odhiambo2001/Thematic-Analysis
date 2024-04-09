import re

def preprocess_text(text):
    """
    Preprocesses the text data by removing speaker names, timestamps, and non-essential punctuation.
    
    Args:
    text (str): The input text data.
    
    Returns:
    str: The preprocessed text data.
    """
    # Remove speaker names
    text = re.sub(r'[A-Za-z]+\s[A-Za-z]+:', '', text)
    
    # Remove timestamps
    text = re.sub(r'\d+:\d+', '', text)
    
    # Remove non-essential punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

def analyze_themes(text):
    """
    Analyzes the themes or topics in the conversation transcript.
    
    Args:
    text (str): The preprocessed text data.
    
    Returns:
    list: A list of themes or topics identified in the conversation.
    """
    # Split the text into individual utterances
    utterances = text.split('\n')
    
    # Initialize a dictionary to store themes and their frequencies
    themes = {}
    
    # Iterate through each utterance
    for utterance in utterances:
        # Tokenize the utterance
        words = utterance.split()
        
        # Iterate through each word in the utterance
        for word in words:
            # Check if the word is a theme
            if len(word) > 3:  # Filter out short words
                # Increment the frequency count for the theme
                themes[word] = themes.get(word, 0) + 1
    
    # Sort themes by frequency in descending order
    sorted_themes = sorted(themes.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_themes

def main():
    # Read the conversation transcript from a file
    with open('conversation_transcript.txt', 'r') as file:
        conversation_text = file.read()
    
    # Preprocess the text data
    preprocessed_text = preprocess_text(conversation_text)
    
    # Analyze themes in the conversation
    themes = analyze_themes(preprocessed_text)
    
    # Print the top themes
    print("Top themes in the conversation:")
    for theme, frequency in themes[:100]:  # Display top 100 themes
        print(f"{theme}: {frequency} mentions")

if __name__ == "__main__":
    main()
