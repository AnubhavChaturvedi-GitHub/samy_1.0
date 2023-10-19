from ear import listen
from mouth import speak
from Search import search_brain

def main():
    while True:
        text = listen()
        response = search_brain(text)
        speak(response)

if __name__ == "__main__":
    main()
