import keyboard as ky
from pynput import keyboard
from spellchecker2 import SpellChecker2


def on_press(key):
    try:
        global recorded_string
        recorded_string += key.char
    except AttributeError:
        pass
    if key == keyboard.Key.space:
        return False


# create a spell checker object
spell = SpellChecker2()
spell.load_dictionary("dict.txt")
print(spell.known_words)

recorded_string = ""
while True:
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

    corrected_word = spell.generate_suggestions(recorded_string)
    # print("corrected: ",corrected_word)

    # Correcting...
    # Delete the misspelled word and replace it with the correction
    if corrected_word != [] and corrected_word[0] != recorded_string.strip():
        ky.press('ctrl')
        ky.press_and_release('backspace')
        ky.release('ctrl')
        ky.write(corrected_word[0])
        ky.write(" ")

    recorded_string = ""
