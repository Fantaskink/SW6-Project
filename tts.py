from gtts import gTTS
from pydub import AudioSegment
import simpleaudio as sa
import os
import re
import pygame


def pronounce_letters(text):
    # Insert spaces between each character
    # spaced_text = ' '.join(text)

    new_text = replace_chars_with_string(text)
    new_text = replace_with_phonetic_spelling(new_text)
    #print(new_text)
    # Create a gTTS object for the modified text
    tts = gTTS(new_text)
    # Save the audio as a temporary file
    tts.save("temp/tts.mp3")
    try:
        # Initialize pygame mixer
        pygame.mixer.init()
        # Load the audio file
        pygame.mixer.music.load("temp/tts.mp3")
        # Play the audio
        pygame.mixer.music.play()
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    finally:
        # Remove the temporary file
        if os.path.exists("temp/tts.mp3"):
            os.remove("temp/tts.mp3")


def get_string_from_char(char):
    binary_dict = {
        " ": ".",
        "{": "left curly bracket",
        "}": "right curly bracket",
        "(": "left parenthesis",
        ")": "right parenthesis",
        "[": "left square bracket",
        "]": "right square bracket",
        "<": "left angle bracket",
        ">": "right angle bracket",
        ",": "comma",
        ".": "period",
        ":": "colon",
        ";": "semicolon",
        "!": "exclamation mark",
        "?": "question mark",
        "\"": "quotation mark",
        "'": "apostrophe",
        "*": "asterisk",
        "-": "dash",
        "/": "forward slash",
        "\\": "backslash",
        "|": "pipe",
    }
    if char in binary_dict:
        return binary_dict[char]
    else:
        return False


def replace_chars_with_string(string):
    new_string = ""
    for char in string:
        if get_string_from_char(char):
            new_string += " " + get_string_from_char(char) + " "
        else:
            new_string += char
    return new_string


def replace_with_phonetic_spelling(string):
    # Replace "a" with "ay"
    string = re.sub(r" a ", " ay ", string)
    return string


if __name__ == "__main__":
    pass
