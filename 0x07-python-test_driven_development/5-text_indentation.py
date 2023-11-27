#!/usr/bin/python3

def text_indentation(text):
    """
    Prints text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
    text (str): Text string to be processed and printed.

    Returns:
    None

    Raises:
    TypeError: If text is not a string.
    """

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters to split text on
    split_characters = ['.', '?', ':']

    # Initialize an empty string to store formatted text
    formatted_text = ""

    # Iterate through each character in the text
    for char in text:
        formatted_text += char

        # If the character is one of the split characters, add two new lines
        if char in split_characters:
            formatted_text += "\n\n"

    # Split the formatted text into lines and print each line without leading or trailing spaces
    for line in formatted_text.split('\n'):
        print(line.strip())
