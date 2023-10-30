#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text (str): The text to be indented.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    charss = ['.', '?', ':']
    new_textt = ""

    text_length = len(text)
    for i in range(text_length):
        if text[i] == ' ':
            if new_textt == "" or new_textt[-1] == "\n":
                continue
            new_textt += text[i]
        elif text[i] in charss:
            new_textt += text[i] + "\n\n"
        else:
            new_textt += text[i]
    print(new_textt, end="")
