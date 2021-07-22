import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("say something")

        audio = r.listen(source)

        try:
            print("you have said : \n " + r.recognize_google(audio))

            f = open("text1.txt", "w")
            f.write(r.recognize_google(audio))
            f.close()

        except Exception as e:
            print("error : " + str(e))


if __name__ == "__main__":
    main()
