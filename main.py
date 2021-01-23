from pynput import keyboard

palabra = []
text = ""
item = ""


def on_press(key):
    # palabra.append(key.char)
    global text
     #   text += str(key.char)
    if str(key) == "Key.enter":
        text+="\n"
    elif str(key) == "Key.space":
        text+=" "
    elif str(key) == "Key.backspace":
        text=text[:-1]
    elif str(key) == "Key.up":
        print("%flecha arriba%")
    elif str(key) == "Key.down":
        print("%flecha abajo%")
    elif str(key) == "Key.left":
        print("%flecha izquierda%")
    elif str(key) == "Key.right":
        print("%flecha derecha%")
    elif str(key) == "Key.esc" or str(key) == "Key.shift_r" or str(key) == "Key.shift" or str(key) == "Key.alt_gr" or str(key) == "Key.ctrl_l" :
        pass

    else:
        print(key)
        text+=key.char


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
) as listener:
    listener.join()
f = "-"

print("Al final sale:\n{0}".format(text))
