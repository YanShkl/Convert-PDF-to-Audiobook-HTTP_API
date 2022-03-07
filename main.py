from gtts import gTTS
import pdfplumber
import time


#Opening PDF File
with pdfplumber.open('file.pdf') as pdf:

    #Looping through each page
    for page in pdf.pages:

        #Showing Text
        print(page.extract_text())

        #Extracting text
        extracted_text = page.extract_text()

        #Adding Space for avoiding data loss
        space = '             '

        #Setting language
        language = 'en'

        # Requesting data from Google Translate text-to-speech API
        myobj = gTTS(text=extracted_text + space, lang=language, slow=False)

        # Adding time promt for Successful data retrieval for all pages
        time.sleep(7)

        #Setting number of page
        page_number = page.page_number

        #Saving file
        myobj.save(f"book mp3s/page {page_number}.mp3")

