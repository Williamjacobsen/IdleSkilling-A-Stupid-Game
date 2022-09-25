import win32gui
import keyboard
import pyautogui
import time
import threading
import win32api
import win32con

def getWindowFocus():
	return win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Idle Skilling"

def spamKeys():
	keys = ['1', '2', '3', '4', '5', 'q', '1', '2', '3', '4', '5', 'q']
	while True:
		for key in keys:
			if getWindowFocus():
				pyautogui.press(key)

def spamClicks():
	try:
		pyautogui.PAUSE = 0.005
	except Exception as e:
		print("\nCould not speed pyautogui up...\n")
	print("toggle clicking by pressing 'å'\n")
	click = False
	print("click status: " + str(click))
	while True:
		if getWindowFocus() and click:
			pyautogui.click()
		if keyboard.is_pressed('å'):
			click = not click
			print("click status: " + str(click))
			time.sleep(1)

if __name__ == '__main__':
	try:
		t1 = threading.Thread(target=spamKeys)
		t2 = threading.Thread(target=spamClicks)
		t1.start()
		t2.start()
	except Exception as e:
		print(e)
