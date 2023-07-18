


from googletrans import Translator
import pyttsx3
gap = pyttsx3.init()
gap.say("salom")
gap.runAndWait()


print("Bizning Tarjima Qiluvchi Proyektimizga Hush Kelibsiz")
while True:
        translator = Translator()
        tarjima = input("So'z Kiriting : ")
        tarjimon = translator.translate(tarjima, dest="en", )
        google = translator.translate(tarjima, dest="uz")
        again = (input("Qaysi Tilni Tanlaysiz(en/uz): "))
        if again =='en':
              print(tarjimon.text)
        elif again =='uz':
              print(google.text)
        a = int(input("Yana Kiritishni Hohlaysizmi(1/2): "))
        if a ==2:
            break
