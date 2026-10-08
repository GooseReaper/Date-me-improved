
from socket import socket
import time
import urllib.parse
import webbrowser
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # just to resolve local IP
        return s.getsockname()[0]
    finally:
        s.close()


def open_answer_draft(answers):
    recipient = "your_email@example.com"
    subject = "My answers"
    body = "\n".join(f"{question}: {answer}" for question, answer in answers.items())

    url = (
        f"mailto:{recipient}"
        f"?subject={urllib.parse.quote(subject)}"
        f"&body={urllib.parse.quote(body)}"
    )
    webbrowser.open(url)

def yes_or_no():
        choice = input("Will you date me? (yes/no): ").lower()
        if choice == "yes":
            yes_i_will()
        elif choice == "no":
            reject()
        else:
            print("Please enter 'yes' or 'no'.")
            yes_or_no()


def ip_puller():
    return get_local_ip()

def yes_i_will():
    print("Perfect!")
    user_input = input("Please give your awnsers: ")
    fav_flower = input("What is your favorite flower? ")
    fav_color = input("What is your favorite color? ")
    fav_animal = input("What is your favorite animal? ")
    fav_food = input("What is your favorite food? ")
    fav_drink = input("What is your favorite drink? ")
    fav_book = input("What is your favorite book? ")
    fav_movie = input("What is your favorite movie? ")
    fav_language = input("What is your favorite programming language? ")
    fav_os = input("What is your favorite operating system? ")
    fav_song = input("What is your favorite song? ")
    print("Here are your answers:")
    print(f"Favorite flower: {fav_flower}")
    print(f"Favorite color: {fav_color}")
    print(f"Favorite animal: {fav_animal}")
    print(f"Favorite food: {fav_food}")
    print(f"Favorite drink: {fav_drink}")
    print(f"Favorite book: {fav_book}")
    print(f"Favorite movie: {fav_movie}")
    print(f"Favorite programming language: {fav_language}")
    print(f"Favorite operating system: {fav_os}")
    print(f"Favorite song: {fav_song}")
    awnsers = [fav_flower, fav_color, fav_animal, fav_food, fav_drink, fav_book, fav_movie, fav_language, fav_os, fav_song]
    open_answer_draft({
        "Favorite flower": fav_flower,
        "Favorite color": fav_color,
        "Favorite animal": fav_animal,
        "Favorite food": fav_food,
        "Favorite drink": fav_drink,
        "Favorite book": fav_book,
        "Favorite movie": fav_movie,
        "Favorite programming language": fav_language,
        "Favorite operating system": fav_os,
        "Favorite song": fav_song
    })
    return False

def reject():
    print("You have chosen to reject me.")
    ip = ip_puller()
    print(f"Your local IP address is: {ip}")
    time.sleep(2)
    print("Im just JOKING its okay :( ")
    return 

yes_or_no()
