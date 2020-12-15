import PyPDF2
from gtts import gTTS
import playsound
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

print('\033[2J')
pdfFileName = input(Fore.BLUE + "What is the path to the PDF file? ")
rangeNum1 = int(input(Fore.BLUE + "What will be the first page number? "))
rangeNum2 = int(input(Fore.BLUE + "What will be the second page number? "))
print(Fore.RED + "Processing...")
rangeNum2 += 1

pdfFile = PyPDF2.PdfFileReader(pdfFileName)

str = ""

for item in range(rangeNum1, rangeNum2):
    str += pdfFile.getPage(item).extractText()

def text_to_speech(text):
    tts = gTTS(text=text)
    filename = "AudioBook.mp3"
    tts.save(filename)

text_to_speech(str)

choiceUser = input(Fore.BLUE + "The AudioBook has been made. Would you like to listen to it right away?(Y/N) ").capitalize()

if choiceUser == "Y":
    print("Okay")
    playsound.playsound("AudioBook.mp3")
elif choiceUser == "N": 
    print(Fore.YELLOW + "Okay, see you later!")
else:
    print(Fore.RED + "Invalid command! Try again.")