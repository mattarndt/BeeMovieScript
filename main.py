import pyautogui
from urllib.request import urlopen
from bs4 import BeautifulSoup
pyautogui.FAILSAFE = True

beeMovieURL = "https://web.njit.edu/~cm395/theBeeMovieScript/"
page = urlopen(beeMovieURL)
soup = BeautifulSoup(page, "html.parser")

name_box = soup.find("pre")
script = name_box.text.strip()

for word in script.split():
    pyautogui.write(word)
    pyautogui.press("enter");
