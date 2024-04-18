#pip install pytttsx3
#pip install PyPDF2
#NOTE: ONLY USE THIS IF YOU HAVENT INSTALL IT . YOU CAN INSTALL IT IN TERMINAL OR CONSOLE DIRECTLY

#imoorting pytttsx3 and PyPDF2
import pyttsx3
import PyPDF2

#EXCEPTION HANDLER

try:
    #OPENING pythin.pdf file in binary read mode bcuz it is appropriate for pdf files
    with open('python.pdf', 'rb') as read:
    #PdfReader: This is a class provided by the PyPDF2 module. which allows us to read contents of pdf files
    #stores the contents of pdf files in reading
        reading = PyPDF2.PdfReader(read)
        #calculate the no of pages in pdf file
        page = len(reading.pages)
        #prints the number of pages
        #pages is a attribute of pdfreader 
        print(f"THE TOTAL NO OF PAGE IS {page}")

        print(' ')
        #reminding user to enter the pages correctly
        print('REMEMBER IT DOES NOT FOLLOW ACTUAL PAGE NO INSTEAD FOLLOW INDEX\n SO IF YOU WANT TO READ PAGE 1 ENTER 0')
        #While all condition are satisfied
        while True:
            #Asking the user to input the page they want to read
            n = int(input("ENTER THE PAGE YOU WANT TO USE: "))
            #Checking if the page entered is between 0 and the total no of pages
            if 0 < n < page:
                #if condition are satisfies move to the next step
                break
            else:
                #if not reasking the user
                print(f"ERROR: PLEASE ENTER THE PAGE NO BETWEEN {0} TO {page-1}")

        #initialize the pyttsx3 
        speak = pyttsx3.init()
        #select the page from reading
        choose = reading.pages[n]
        #extract the content from selected page
        text = choose.extract_text()
        #instruct pyttsx3 to convert the text into speacg
        speak.say(text)
        #run the speach and wait until it is done
        speak.runAndWait()
        
#expectin handler cases
except FileNotFoundError:
    print("FILE NOT FOUND")
except PyPDF2.utils.PdfReaderError:
    print("FILE IS NOT A PDF")
except IndexError:
    print("PAGE NOT FOUND")
except Exception as e:
    print(e)

