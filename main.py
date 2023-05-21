import datetime
import sys
import threading
import time
from urllib import response
import pyttsx3
import wikipedia
import webbrowser
import json
import os
from urllib.request import urlopen
from plyer import notification
from termcolor import colored
import re
from bs4 import BeautifulSoup
import requests
import imdb
import keyboard
import pyautogui
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import choose_your_own_adventure
import base_convertor
import bin_search_simulator
import bubble_sort_simulator
import selection_sort_simulator
import insertion_sort_simulator
import number_guessing_game
import quiz_game
import rock_paper_scissors
import dice_simulator
from twilio.rest import Client

# import speech_recognition

stops_thread = True
reminder = ""
sec = 0
name = ""


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        s = "Good Morning, " + name
    elif hour >= 12 and hour <= 18:
        s = "Good Afternoon, " + name
    else:
        s = "Good Evening, " + name
    speak(s)


def tell_time():
    hour = datetime.datetime.now().strftime("%H")
    minute = datetime.datetime.now().strftime("%M")
    if time_format == "24":
        s = "It's " + hour + " " + minute + " "
        s1 = hour + ":" + minute + " "
        if 0 <= int(hour) <= 11:
            s += "A.M."
            s1 += "A.M."
        else:
            s += "P.M."
            s1 += "P.M."
    else:
        hour = int(hour)
        init_hours = hour
        if hour > 12:
            hour -= 12
        hour = str(hour)
        if int(hour) < 10:
            hour = "0" + hour
        s = "It's " + hour + " " + minute + " "
        s1 = hour + ":" + minute + " "
        if 0 <= init_hours <= 11:
            s += "A.M."
            s1 += "A.M."
        else:
            s += "P.M."
            s1 += "P.M."

    print(colored(s1, "green"))
    speak(s)


def tell_date():
    d = datetime.datetime.now().strftime("%B %d, %Y")
    # s=month+" "+date+", "+year
    print(colored(d, "green"))
    d = "It's " + d
    speak(d)


def tell_day():
    day = datetime.datetime.now().strftime("%A")
    print(colored(day, "green"))
    day = "Today is " + day
    speak(day)


def describe_assitant(name):
    s = (
        "My name is "
        + name
        + ". I am here to assist you in performing different tasks. I am a computer program made using Python programming language."
    )
    speak(s)


def tell_name(name):
    s = "Your name is " + name + "!!"
    speak(s)


def set_reminder(choice):
    l = choice.split(" ")
    global reminder, sec
    reminder = " ".join(l[l.index("to") + 1 : l.index("in")])
    t1 = l[-2]
    t2 = l[-1]
    if t2 == "minutes" or t2 == "minute":
        sec = int(t1) * 60
    else:
        sec = int(t1)

    speak("Reminder Added!!")
    reminder_thread = threading.Thread(target=remind)
    reminder_thread.start()



def set_reminder1(choice):
    l = choice.split(" ")
    global reminder, sec
    reminder = " ".join(l[l.index("to") + 1 : l.index("at")])
    t1 = l[-2]
    t2 = l[-1]
    minutes = 0
    if ":" in t1:
        hours, minutes = t1.split(":")
        hours = int(hours)
        minutes = int(minutes)
    else:
        hours = int(t1)
    if t2 == "pm" and hours < 12:
        hours += 12
    # if t2 == "am" and hours == 12:
    #     hours = 0
    reminder_seconds = hours * 3600 + minutes * 60
    current_seconds = (
        int(datetime.datetime.now().strftime("%H")) * 3600
        + int(datetime.datetime.now().strftime("%M")) * 60
    )
    if reminder_seconds >= current_seconds:
        sec = reminder_seconds - current_seconds
    else:
        sec = 24 * 3600 - current_seconds + reminder_seconds

    speak("Reminder Added!!")
    reminder_thread = threading.Thread(target=remind)
    reminder_thread.start()


def remind():
    while True:
        global reminder, sec
        time.sleep(sec)
        notification.notify(title="Reminder!!", message=reminder, timeout=10)
        global stops_thread
        if stops_thread:
            break
    return


def get_location():
    r = requests.get("https://get.geojs.io/")
    ip_request = requests.get("https://get.geojs.io/v1/ip.json")
    ipAdd = ip_request.json()["ip"]
    url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
    geo_request = requests.get(url)
    data = geo_request.json()
    s = (
        "City       : "
        + data["city"]
        + "\nRegion     : "
        + data["region"]
        + "\nCountry    : "
        + data["country"]
        + "\nTimezone   : "
        + data["timezone"]
    )
    print(colored(s, "green"))
    speak(s)


def open_website(url):
    webbrowser.get("microsoft-edge").open(url)
    speak("Opening desired website..")


def track_number(number):
    speak("Tracking number....")
    ch_number = phonenumbers.parse(number, "CH")
    ch_number = geocoder.description_for_number(ch_number, "en")
    service_number = phonenumbers.parse(number, "RO")
    service_number = carrier.name_for_number(service_number, "en")
    s = "Country : " + ch_number + "\nService : " + service_number
    print(colored(s, "green"))
    speak(s)


if __name__ == "__main__":
    global time_format
    global bluetooth, wifi, flight_mode
    global todo_list
    global TimeTable
    # timetable()
    todo_list = ["null"]
    wifi = "on"
    flight_mode = "off"
    bluetooth = "off"
    time_format = "24"
    os.system("cls")
    browser_path = r"C:\\Program Files\\Internet Explorer\\iexplore.exe"
    webbrowser.register(
        "microsoft-edge", None, webbrowser.BackgroundBrowser(browser_path)
    )
    print(colored("Awaiting Input........", "blue"), end="")
    msg = input()
    assistant_name = msg.split()[-1]
    assistant_name=assistant_name.lower()
    if "friday" in msg:
        assistant_name = "friday"
        engine.setProperty("voice", voices[1].id)
    name = "Shraddha"
    wishMe(name)
    s = "I am " + assistant_name + ". How may I help you?"
    speak(s)
    while True:
        print(colored("\nEnter command : ", "blue"), end="")
        choice = input()
        if "search" in choice and "file" in choice:
            pass
        else:
            choice = choice.lower()

        if choice == "exit":
            print(colored("Terminating....", "green"))
            speak("Hope to see you again!!")
            sys.exit()

        elif "how are you" in choice:
            speak("I am fine, Ma'am. How are you?")
            print(colored("Write Here : ", "green"), end="")
            inp = input()
            if "fine" or "good" in inp:
                speak("Good to here that, Ma'am...")
            else:
                pass

        elif choice in ["what's the time?", "time"]:
            tell_time()

        elif choice in ["change time format"]:
            if time_format == "24":
                speak("Changing time format to 12-hour")
                time_format = "12"
            else:
                speak("Changing time format to 24-hour")
                time_format = "24"

        elif choice in [
            "what's the date today?",
            "tell today's date",
            "what's the date?",
            "date",
        ]:
            tell_date()

        elif choice in [
            "what's the day today?",
            "tell today's day",
            "what day is it today?",
            "what's the day?",
            "day",
        ]:
            tell_day()

        elif choice in ["who are you?", "describe yourself", "Tell me about yourself"]:
            describe_assitant(assistant_name)

        elif choice in ["what's my name?", "tell my name", "who am i?"]:
            tell_name(name)

       


        elif choice in ["change my name"]:
            speak("Enter your name : ")
            print(colored("Enter your name : ", "green"), end="")
            name = input()
            wishMe(name)

        elif "remind" in choice:
            if "am" in choice or "pm" in choice:
                set_reminder1(choice)
            else:
                set_reminder(choice)

        elif "open wikipedia" in choice:
            webbrowser.get("microsoft-edge").open("wikipedia.com")
            speak("Opening wikipedia.com")

        elif "wikipedia" in choice:
            speak("Searching Wikipedia...")
            choice = choice.replace("wikipedia", "")
            try:
                results = wikipedia.summary(choice, sentences=2)
                speak("According to Wikipedia")
                print(colored(results, "green"))
                speak(results)
            except Exception as e:
                print(e)
                speak(e)

        elif "open youtube" in choice or "open yt" in choice:
            webbrowser.get("microsoft-edge").open("youtube.com")
            speak("Opening youtube.com")

        elif "open facebook" in choice or 'open fb' in choice:
            webbrowser.get("microsoft-edge").open("facebook.com")
            speak("Opening facebook.com")

        elif "open instagram" in choice or 'open insta' in choice:
            webbrowser.get("microsoft-edge").open("instagram.com")
            speak("Opening instagram.com")

        elif "open linkedin" in choice:
            webbrowser.get("microsoft-edge").open("linkedin.com")
            speak("Opening linkedin.com")

        elif "open stackoverflow" in choice:
            webbrowser.get("microsoft-edge").open("stackoverflow.com")
            speak("Opening stackoverflow.com")

        elif "open github" in choice:
            webbrowser.get("microsoft-edge").open("github.com")
            speak("Opening github.com")

        elif "open discord" in choice:
            webbrowser.get("microsoft-edge").open("https://discord.com/channels/@me")
            speak("Opening Discord")

        elif "open google classroom" in choice:
            webbrowser.get("microsoft-edge").open("classroom.google.com/u/0/")
            speak("Opening google classroom")

        elif "open gmail" in choice:
            webbrowser.get("microsoft-edge").open("mail.google.com/mail/u/0/")
            speak("Opening gmail.com") 

        elif choice in ['open google maps', 'gmaps', 'google maps']:
            webbrowser.get("microsoft-edge").open("maps.google.com")
            speak("Opening google maps")

        elif 'locate' in choice or 'google maps' in choice:
            l=choice.split()
            if 'locate' in l:
                l[l.index('locate')]=''
            elif 'google maps' in choice:
                l[l.index('google')]=''
                l[l.index('maps')]=''
            place=' '.join(l)
            speak("Locating place....")
            url='https://www.google.co.in/maps/place/'+place
            webbrowser.get('microsoft-edge').open(url)

        elif choice in ["google earth", "open google earth"]:
            webbrowser.get("microsoft-edge").open("earth.google.com")
            speak("Opening google earth")

        elif "google earth" in choice:
            l = choice.split()
            l[l.index("google")] = ""
            l[l.index("earth")] = ""
            query = " ".join(l)
            speak("Locating place....")
            url = "https://earth.google.com/web/search/" + query
            webbrowser.get("microsoft-edge").open(url)

        elif choice in ["open google meet", "open gmeet", "gmeet"]:
            webbrowser.get("microsoft-edge").open("meet.google.com")
            speak("Opening google meet")

        elif "open google" in choice:
            webbrowser.get("microsoft-edge").open("google.com")
            speak("Opening google.com")

        elif "google" in choice:
            speak("Searching Google...")
            choice = choice.replace("google", "")
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
            print(colored("Showing search results...", "green"))
            s = "Showing results for " + choice
            speak(s)
            results = []
            i = 1
            for j in search(choice, tld="co.in", num=10, stop=10, pause=2):
                s1 = str(i) + ". " + j
                print(colored(s1, "green"))
                results.append(j)
                i += 1
            speak("Do you want to visit a website?")
            print(colored("\nWrite yes/no : ", "green"), end="")
            ch = input()
            if "yes" in ch:
                print(colored("Enter site number : ", "green"), end="")
                num = int(input())
                open_website(results[num - 1])
            else:
                continue

        # elif choice in ["tell my location", "location"]:
        #     speak("Fetching location...")
        #     get_location()

        elif "play a song" in choice:
            webbrowser.get("microsoft-edge").open("music.amazon.in")
            speak("Opening amazon music")

        elif "speedtest" in choice:
            webbrowser.get("microsoft-edge").open("speedtest.net")
            speak("Opening speedtest.net")

        elif choice in ["open code", "open vsc", "vsc", "open vs code"]:
            codePath = "C:\\Users\\Mhsn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Starting vs code...")

        elif choice in ["open webex", "webex"]:
            path = "C:\\Users\\Mhsn\\AppData\\Local\\CiscoSparkLauncher\\CiscoCollabHost.exe"
            os.startfile(path)
            speak("Starting Webex...")

        elif choice in ["open android studio", "android studio", "as"]:
            path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(path)
            speak("Starting Android Studio...")

        elif choice in ["open bluej", "bluej"]:
            path = "C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(path)
            speak("Starting BlueJ...")


        elif choice in [
            "open excel",
            "xlsx",
            "excel",
            "open xlsx",
            "open ms excel",
            "ms excel",
        ]:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path)
            speak("Opening MS Excel...")


        elif choice in ["open git bash", "git bash", "git"]:
            path = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(path)
            speak("Starting Git Bash...")

        elif choice in ["open chrome", "chrome"]:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            speak("Opening Google Chrome...")

        elif choice in ["open microsoft edge", "open edge", "microsoft edge", "edge"]:
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(path)
            speak("Opening Microsoft Edge...")

        elif choice in ["open nodejs", "nodejs", "node", "open node"]:
            path = "C:\\Program Files\\nodejs\\node.exe"
            os.startfile(path)
            speak("Starting Node JS...")

       

        elif choice in ["open ppt", "open powerpoint", "powerpoint", "ppt"]:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)
            speak("Opening PowerPoint...")

        elif choice in ["open word", "word", "open ms word", "ms word"]:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)
            speak("Opening MS Word...")



        
        
        
        elif choice in ["open amazon"]:
            webbrowser.get("microsoft-edge").open("https://www.amazon.in/")
            speak("Opening amazon.in")

        elif choice in ["open amazon music", "amazon music"]:
            webbrowser.get("microsoft-edge").open("music.amazon.in")
            speak("Opening Amazon Music...")

        elif choice in [
            "open prime video",
            "prime video",
            "opening amazon prime",
            "amazon prime",
        ]:
            webbrowser.get("microsoft-edge").open(
                "https://www.primevideo.com/storefront/home/ref=atv_dp_mv_c_9zZ8D2_1_1"
            )
            speak("Opening Amazon Prime...")

        elif choice in ["open hotstar", "hotstar"]:
            webbrowser.get("microsoft-edge").open("https://www.hotstar.com/in")
            speak("Opening Hotstar...")

        elif choice in ["open college website", "college website", "iiitl website"]:
            webbrowser.get("microsoft-edge").open("iiitl.ac.in")
            speak("Opening IIIT Lucknow's website...")

        elif "top" in choice and "movies" in choice:
            speak("Executing Query...")
            num = ""
            for ch in choice:
                if ch in "0123456789":
                    num += ch
            num = int(num)
            url = "http://www.imdb.com/chart/top"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            movies = soup.select("td.titleColumn")
            crew = [a.attrs.get("title") for a in soup.select("td.titleColumn a")]
            ratings = [
                b.attrs.get("data-value")
                for b in soup.select("td.posterColumn span[name=ir]")
            ]
            top_movies = []
            for index in range(0, len(movies)):
                movie_string = movies[index].get_text()
                movie = " ".join(movie_string.split()).replace(".", "")
                movie_title = movie[len(str(index)) + 1 : -7]
                year = re.search("\((.*?)\)", movie_string).group(1)
                place = movie[: len(str(index)) - len(movie)]
                data = {
                    "place": place,
                    "movie_title": movie_title,
                    "rating": ratings[index],
                    "year": year,
                    "star_cast": crew[index],
                }
                top_movies.append(data)
            s = "Top " + str(num) + " movies :"
            print(colored(s, "green"))
            s = "Top " + str(num) + " movies according to IMDB...."
            speak(s)
            i = 1
            for movie in top_movies:
                if i <= num:
                    s = (
                        movie["place"]
                        + " - "
                        + movie["movie_title"]
                        + " ("
                        + movie["year"]
                        + ") "
                        + "Starring: "
                        + movie["star_cast"]
                        + " "
                        + movie["rating"]
                    )
                    print(colored(s, "green"))
                    i += 1
                else:
                    break

        elif ("search" in choice or "open" in choice) and "file" in choice:
            l = choice.split()
            file_name = " ".join(l[l.index("file") + 1 :])
            listing = os.walk("C:\\Users\\Mhsn\\Documents\\")
            paths = []

            print(colored("Searching file...", "green"))
            speak("Searching file...")

            for root_path, directories, files in listing:
                # if file_name in files:
                #     paths.append(os.path.join(root_path, file_name))
                for file in files:
                    f = file
                    f1 = file_name
                    f = f.lower()
                    f1 = f1.lower()
                    if f1 in f:
                        paths.append(os.path.join(root_path, file))

            if paths == []:
                s = file_name + " doesn't exist!"
                print(colored(s, "green"))
                speak(s)
                continue

            s = file_name + " found at : "
            s1 = file_name + " found at..."
            print(colored(s, "green"))
            speak(s1)
            for i in range(len(paths)):
                s = str(i + 1) + ". " + paths[i]
                print(colored(s, "green"))

            speak("Which file do you wish to open?")
            print(colored("\nSpecify path number : ", "green"), end="")
            num = int(input())
            speak("Opening desired file...")
            os.startfile(paths[num - 1])

        elif "search" in choice and "movie" in choice:
            l = choice.split()
            movie_name = " ".join(l[l.index("movie") + 1 :])
            moviesDB = imdb.IMDb()
            s = "Searching Movie...."
            speak(s)
            movies = moviesDB.search_movie(movie_name)
            if movies == []:
                print(colored("No such movie...", "green"))
                speak("No movie found with this name...")
                continue

            print(colored("Showing search results...", "green"))
            s = "Showing search results for " + movie_name
            speak(s)
            j = 1
            for i in range(len(movies)):
                try:
                    s = (
                        str(j)
                        + ". "
                        + movies[i]["title"]
                        + " - "
                        + str(movies[i]["year"])
                    )
                except Exception as e:
                    s = str(j) + ". " + movies[i]["title"]
                print(colored(s, "green"))
                j += 1
            speak("For which movie do you want information?")
            print(colored("\nSpecify movie number : ", "green"), end="")
            num = int(input())
            speak("Getting movie information...")
            id = movies[num - 1].getID()
            movie = moviesDB.get_movie(id)
            title = movie["title"]
            year = movie["year"]
            try:
                rating = movie["rating"]
            except Exception as e:
                rating = "Not yet Rated"
            directors = movie["directors"]
            casting = movie["cast"]
            plot = movie["plot"]
            print(colored("\nMovie Information : ", "green"))
            # directors = list(map(str, directors))
            directors = ", ".join(map(str, directors))
            # actors = list(map(str, casting))
            actors = ", ".join(map(str, casting))
            actors = actors.split(", ")
            if len(actors) > 10:
                actors = actors[:10]
            plot = plot[0]
            actors = ", ".join(actors)
            s = (
                "Title : "
                + title
                + "\nYear of Release : "
                + str(year)
                + "\nRating : "
                + str(rating)
                + "\nDirectors : "
                + directors
                + "\nActors : "
                + actors
                + "\nPlot : "
                + plot
            )
            print(colored(s, "green"))
            speak(s)

        elif choice in ["book movie tickets", "movie tickets"]:
            webbrowser.get("microsoft-edge").open(
                "https://in.bookmyshow.com/explore/movies-lucknow"
            )
            speak("Opening BookMyShow.com....")

        elif choice in ["turn on bluetooth", "switch on bluetooth"]:
            if bluetooth == "off":
                speak("Turning on bluetooth...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1625, y=462)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                bluetooth = "on"
            else:
                speak("Bluetooth is already on...")

        elif choice in ["turn off bluetooth", "switch off bluetooth"]:
            if bluetooth == "on":
                speak("Turning off bluetooth...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1625, y=462)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                bluetooth = "off"
            else:
                speak("Bluetooth is already off...")

        elif choice in ["turn on wifi", "switch on wifi"]:
            if wifi == "off":
                speak("Turning on wifi...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1424, y=465)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                wifi = "on"
            else:
                speak("Wifi is already on...")

        elif choice in ["turn off wifi", "switch off wifi"]:
            if wifi == "on":
                speak("Turning off wifi...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1424, y=465)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                wifi = "off"
            else:
                speak("Wifi is already off...")

        elif choice in [
            "turn on airplane mode",
            "switch on airplane mode",
            "turn on flight mode",
            "switch on flight mode",
        ]:
            if flight_mode == "off":
                speak("Turning on Flight mode...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1789, y=476)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                flight_mode = "on"
                # bluetooth = "off"
                # wifi = "off"
            else:
                speak("Flight mode is already on...")

        elif choice in [
            "turn off airplane mode",
            "switch off airplane mode",
            "turn off flight mode",
            "switch off flight mode",
        ]:
            if flight_mode == "on":
                speak("Turning off Flight mode...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1789, y=476)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                flight_mode = "off"
            else:
                speak("Flight mode is already off...")

        elif choice in ["show available wifi devices"]:
            if wifi == "off":
                speak("Turning on wifi...")
                keyboard.press_and_release("windows+a")
                time.sleep(1)
                pyautogui.click(x=1424, y=465)
                time.sleep(1.5)
                keyboard.press_and_release("windows+a")
                wifi = "on"
            speak("Showing available wifi devices...")
            keyboard.press_and_release("windows+a")
            time.sleep(1)
            pyautogui.click(x=1504, y=470)

        elif choice in ["project screen"]:
            speak("Opening Screen Projection....")
            keyboard.press_and_release("windows+p")

        elif choice in ["switch screens"]:
            speak("Switching between screens....")
            keyboard.press("alt+tab")
            time.sleep(3)
            keyboard.release("alt+tab")

        elif "convertor" in choice:
            speak("Starting Base Convertor....")
            base_convertor.execute_base_convertor()

            time.sleep(2)
            os.system("cls")

        elif "binary search simulator" in choice:
            speak("Starting Binary Search Simulator....")
            bin_search_simulator.execute_bin_search_simulator()

            time.sleep(2)
            os.system("cls")

        elif "bubble sort simulator" in choice:
            speak("Starting Bubble Sort Simulator....")
            bubble_sort_simulator.execute_bubble_sort_simulator()

            time.sleep(2)
            os.system("cls")

        elif "selection sort simulator" in choice:
            speak("Starting Selection Sort Simulator....")
            selection_sort_simulator.execute_selection_sort_simulator()

            time.sleep(2)
            os.system("cls")

        elif "insertion sort simulator" in choice:
            speak("Starting Insertion Sort Simulator....")
            insertion_sort_simulator.execute_insertion_sort_simulator()

            time.sleep(2)
            os.system("cls")


        elif "choose your own adventure" in choice:
            speak("Loading Choose your own Adventure....")
            choose_your_own_adventure.execute_choose_your_own_adventure()

            time.sleep(2)
            os.system("cls")

        elif "dice simulator" in choice:
            speak("Loading Dice simulator....")
            dice_simulator.execute_dice_simulator()

            time.sleep(2)
            os.system("cls")

        elif "number guessing game" in choice:
            speak("Loading Number Guessing game....")
            number_guessing_game.execute_number_guessing_game()

            time.sleep(2)
            os.system("cls")

        elif "quiz" in choice:
            speak("Loading Quiz....")
            quiz_game.execute_quiz_game()

            time.sleep(2)
            os.system("cls")

        elif "rock paper scissors" in choice:
            speak("Loading Rock, Paper and Scissors....")
            rock_paper_scissors.execute_rock_paper_scissors()

            time.sleep(2)
            os.system("cls")

        elif "play a game" in choice:
            speak("Displaying list of games....")
            s = "1. Snake and Ladder\n2. Chess\n3. Choose your own adventure...\n4. Number Guessing game\n5. Quiz...\n6. Rock Paper and Scissors"
            print(colored(s, "green"))
            speak("Which game would you like to play, Ma'am?")
            print(colored("\nEnter game number : ", "green"), end="")
            num = int(input())
            
            if num == 3:
                speak("Loading Choose your own Adventure....")
                choose_your_own_adventure.execute_choose_your_own_adventure()

                time.sleep(2)
                os.system("cls")
            elif num == 4:
                speak("Loading Number Guessing game....")
                number_guessing_game.execute_number_guessing_game()

                time.sleep(2)
                os.system("cls")
            elif num == 5:
                speak("Loading Quiz....")
                quiz_game.execute_quiz_game()

                time.sleep(2)
                os.system("cls")
            elif num == 6:
                speak("Loading Rock, Paper and Scissors....")
                rock_paper_scissors.execute_rock_paper_scissors()

                time.sleep(2)

        elif "to do list" in choice:
            if "add" in choice:
                l = choice.split()
                task = " ".join(l[l.index("add") + 1 : l.index("in")])
                todo_list.append(task)
                speak("Task added...")
            elif "display" in choice:
                if len(todo_list) == 1:
                    speak("To-do List is empty....")
                    continue
                print(colored("To-do List", "green"))
                speak("Displaying To-do list....")
                for i in range(1, len(todo_list)):
                    s = "Task " + str(i) + " --> " + todo_list[i]
                    print(colored(s, "green"))
            elif "delete" in choice:
                l = choice.split()
                if "task" in l:
                    num = int(l[l.index("task") + 1])
                else:
                    task = " ".join(l[l.index("delete") + 1 : l.index("from")])
                    num = todo_list.index(task)
                del todo_list[num]
                speak("Task deleted....")

        

        elif "shutdown" in choice:
            speak("Shutting down PC....")
            os.system("shutdown /s")

        elif "restart" in choice:
            speak("Restarting PC....")
            os.system("shutdown /r")

        elif "track" in choice and "number" in choice:
            l = choice.split()
            track_number(l[-1])

        elif choice in [
            "open whatsapp",
            "open wa",
            "whatsapp",
            "wa",
            "open whatsapp web",
            "whatsapp web",
            "wa web",
            "open wa web",
        ]:
            webbrowser.get("microsoft-edge").open("web.whatsapp.com")
            speak("Opening Whatsapp Web")

        elif "open folder" in choice:
            l = choice.split()
            folder_name = " ".join(l[l.index("folder") + 1 :])


        elif (
            "search youtube" in choice
            or "search yt" in choice
            or "youtube" in choice
            or "yt" in choice
        ):
            l = choice.split()
            if "search youtube" in choice:
                l[l.index("search")] = ""
                l[l.index("youtube")] = ""
            elif "search yt" in choice:
                l[l.index("search")] = ""
                l[l.index("yt")] = ""
            elif "youtube" in choice:
                l[l.index("youtube")] = ""
            elif "yt" in choice:
                l[l.index("yt")] = ""
            query = " ".join(l)
            speak("Searching YouTube....")
            url = "https://www.youtube.com/results?search_query=" + query
            webbrowser.get("microsoft-edge").open(url)

        elif choice in ['top headlines', 'news today', 'news', "today's top headlines"]:
            speak("Showing today's top headlines....")
            api_key='ddbca564138b4fe58b124b68fc74270d'
            url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='+api_key
            news = requests.get(url).json()
            articles = news['articles']
            news_article=[]
            for article in articles:
                news_article.append(article['title'])
            for i in range(len(news_article)):
                print(colored(news_article[i],"green"))
                
        elif choice in ['our project ppt']:
            speak("Opening Byte PPT")
            url = 'https://docs.google.com/presentation/d/1gAPA6cOToMf8D-02tajIePFKGmZl8gRH7TxsG1A8c-0/edit?usp=sharing'
            webbrowser.get("microsoft-edge").open(url)
        
        elif choice in ['call']:
            account_sid = 'AC88620b526d75aff90332d5824aa89a83'
            auth_token = '2471d8bfe836eafc8f7c3ba3654e295e'
            client = Client(account_sid, auth_token)
            call = client.calls.create(
                to=input(),  
                from_='+917704059089', 
                url='http://demo.twilio.com/docs/voice.xml'  
            )

            print(call.sid) 
