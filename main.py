from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def on_activate_i_tilde():
    print("se presionó: í")


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey_ti = keyboard.HotKey(
    keyboard.HotKey.parse("´+i"), on_activate_i_tilde()
)


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

with keyboard.GlobalHotKeys({
        '´+i': on_activate_i_tilde,
        }) as h:
    h.join()

listener.start()
