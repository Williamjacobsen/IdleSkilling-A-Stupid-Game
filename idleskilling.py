import win32gui
import keyboard
import pyautogui
import time
import threading

def myMann():
	print("""  _____    _ _         _____ _    _ _ _ _                        _   _       _     _          _    
 |_   _|  | | |       / ____| |  (_) | (_)                      | \ | |     | |   | |        | |   
   | |  __| | | ___  | (___ | | ___| | |_ _ __   __ _   ______  |  \| |_   _| |__ | |__   ___| |_  
   | | / _` | |/ _ \  \___ \| |/ / | | | | '_ \ / _` | |______| | . ` | | | | '_ \| '_ \ / _ \ __| 
  _| || (_| | |  __/  ____) |   <| | | | | | | | (_| |          | |\  | |_| | |_) | |_) |  __/ |_  
 |_____\__,_|_|\___| |_____/|_|\_\_|_|_|_|_| |_|\__, |          |_| \_|\__,_|_.__/|_.__/ \___|\__| 
                                                 __/ |                                             
                                                |___/                                              """)

def getWindowFocus():
	return win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Idle Skilling"

def spamKeys(pos):
	while True:
		# 12345q
		keys = ['1', '2', '3', '4', '5', 'q']
		for key in keys:
			if getWindowFocus():
				pyautogui.press(key)
				time.sleep(0.1)
		# 12345w12345w
		keys = ['1', '2', '3', '4', '5', 'w', '1', '2', '3', '4', '5', 'w']
		for key in keys:
			if getWindowFocus():
				pyautogui.press(key)
				time.sleep(0.1)
		# (pos) q
		for i in range(0, len(pos), 2):
			if getWindowFocus():
				pyautogui.click(pos[i], pos[i + 1])
				time.sleep(0.1)
		if getWindowFocus():
			pyautogui.press('q')
			time.sleep(0.1)

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

def getPos():
	print("Hover mouse over button to click and press 'æ'...\nPress 'ø' to finish...\n")
	pos = []
	while True:
		if keyboard.is_pressed('æ'):
			x, y = pyautogui.position()
			pos.append(x)
			pos.append(y)
			print("Clicking pos = {" + str(x) + ", " + str(y) + "}...")
			time.sleep(0.1)
		if keyboard.is_pressed('ø'):
			return pos

if __name__ == '__main__':
	myMann()
	pos = getPos()
	try:
		t1 = threading.Thread(target=spamKeys, args=(pos,))
		t2 = threading.Thread(target=spamClicks)
		t1.start()
		t2.start()
	except Exception as e:
		print(e)
