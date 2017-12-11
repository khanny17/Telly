import time
import RPi.GPIO as GPIO
import thread
import sayhello 
from Tkinter import *

def main():
	thread.start_new_thread(hello, ())
	run_gui()

def hello():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while True:
		GPIO.wait_for_edge(23, GPIO.RISING)
		time.sleep(2)
		sayhello.hello()
		time.sleep(1)

def run_gui():
	root = Tk()

	root.attributes('-fullscreen', True)

	time_str = StringVar()
	time_str.set(time.strftime('%H:%M:%S'))
	w=Label(root, textvariable = time_str, compound = CENTER)
	w.config(font=("Courier", 24))
	w.pack()

	while True:
		time.sleep(0.5)
		time_str.set(time.strftime('%H:%M:%S'))
		root.update_idletasks()


if __name__ == "__main__": main()
