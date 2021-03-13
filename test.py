from pynput import keyboard
import smtplib
import os
import enum
from enum import Enum
from email.message import EmailMessage
import subprocess
import re
from array import *

email = os.environ.get("EMAIL_USER")
passw = os.environ.get("EMAIL_PASS")
palabra = []
text = """sdfas dfa sdf as fdsaf michael@gmai.com
sasdfas sdfasdf
ffasdf sad fa sdf
asdf fsdf@fasdf.com.com.com
holi@gmail.edu.pecom fasdf
sdfasdf
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Nulla interdum dui sem. Pellentesque 
egestas interdum quam, quis aliquet 
est accumsan eu. Aenean non egestas 
dolor. Quisque nec odio urna.
Nulla eget tortor tincidunt, 
ultricies justo at, sagittis 
orci. Curabitur eget eros elementum,
juan@gmail.com
volutpat nulla et, scelerisque mi.
In consequat ante erat, in semper 
eros elementum auctor. Suspendisse
varius tellus feugiat augue gravida, 
faucibus ullamcorper lacus ultrices.
Cras faucibus, mi eget pellentesque
 porttitor, turpis ante hendrerit eros, nec dignissim orci velit sit amet augue. Pellentesque est turpis, ullamcorper et hendrerit vitae, dapibus non magna. Quisque non posuere ex, a commodo augue. Sed vitae varius sapien. Proin in mauris hendrerit, mollis lectus quis, imperdiet urna. Cras odio lorem, venenatis vel placerat in, porta a neque. Suspendisse consectetur eget arcu eu blandit. In pharetra eros sodales, lacinia erat et, pretium magna. Morbi iaculis, lectus et elementum dictum, elit erat sodales lorem, sed interdum nulla nibh ut nunc.
Morbi et venenatis ligula. Curabitur 
juan@cot.edu.col
imperdiet dui eget arcu facilisis 
faucibus. Nullam vitae lobortis elit,
id bibendum mauris. Etiam sit amet 
fasdf juan@cot.edu.col  asdfasdf
fsadf fasf a s diego@min.com fasdfas
fasdf@fsadf.com
h
"""
item = ""

text2 = '''hoal asdof sdf as df comos es asd fa
hola otr hola hotrla otro hola
aquí no no hola sfdasd fas df as hola'''


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


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener mp

        return False


def filter():
    result = ""
    indexes = []
    p = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = p.finditer(text)
    in_words = text.split()

    for index, single in enumerate(in_words):
        matches = p.finditer(single)
        for match in matches:
            #    print(f'{match.group(0)} {index}')
            indexes.append(index)
    print(f'las ubicaciones {indexes}')
    print(f'last ubic {len(in_words)}')
    ccs=1
    for i in indexes:
        po = i
        beg = 0 if po - 5 < 0 else po - 5
        end = (len(in_words) - 1) if (po + 6) > (len(in_words) - 1) else po + 6

        impwor = range(beg, end)
        print(impwor)
        pc = ""
        for j in impwor:
            pc += f' {in_words[j]}'
        result += f'\nPosible cuenta #{ccs}: {in_words[i]} en lo siguiente:\t' + pc
        ccs += 1
    print(result)

    print(f'último coso {in_words[204]}')

def pruebita():
    indexes = (1, 2, 2, 3, 3, 4, 5, 5, 35, 5, 6, 6, 6, 4, 5, 8, 0, 7, 1, 7)
    po = 10
    beg = 0 if po - 5 < 0 else po - 5
    end = (len(indexes) - 1) if po + 5 > len(indexes) else po + 5
    print(f'{beg}  {end}')

    print()

# impwor = range(beg, end)
# print(len(arr))


def main():
    # read()
    # filter_emails()
    filter()




# test(text)
# send(text)


if __name__ == "__main__":
    main()
