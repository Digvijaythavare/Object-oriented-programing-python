import webbrowser
import time

youtube = str(input("Enter one character:\n"))

if youtube == "y" or youtube == "youtube":
    url = "https://www.youtube.com/"
    webbrowser.open(f"https://www.youtube.com/")
else:
     time.sleep(7)
     print("no thanks")    