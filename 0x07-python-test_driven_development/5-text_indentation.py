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
    lines = formatted_text.split('\n')
    for i, line in enumerate(lines):
        if line.strip():  # Check if line has non-whitespace characters
            print(line.strip(), end='')
            if i < len(lines) - 1 and lines[i + 1].strip() and lines[i + 1][0] in split_characters:
                print()  # Print a newline only if the next line starts with a split character
        else:
            if i < len(lines) - 1 and lines[i + 1].strip() and lines[i + 1][0] in split_characters:
                print()  # Print a newline only if the next line starts with a split character
            else:
                pass  # Do not print anything if the line is blank and not followed by a split character
