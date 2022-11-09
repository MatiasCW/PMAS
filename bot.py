'''SubaBot.py'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import flask

def hello():
    return (str(hello))
print(hello())

# Start
# Get the website using the Chrome webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("start-minimize")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(webdriver, 1)
# Spell check
def spell_check(request):
    try:
        # Check if google returns spelling error
        return ("::Do you mean, " + (browser.find_element(By.XPATH, "//a[@id='fprsl']")).text)
        if response == "y" or response == "yes":
            raise Exception(" ... ")
        else:
            return ("::Sorry...I'm not sure what you mean.")
            quit()
    except:
        return text.upper()

def cite():
    try:
        link = browser.find_element(By.XPATH, "//div[@class='yuRUbf']/a").get_attribute('href')
    except:
        link = ""
    try:
        raw_name = (((browser.find_element(By.XPATH, "//cite[@class='iUh30 qLRx3b tjvcx']"))).text).split('.')
        citation = ("-  " + raw_name[1])
    except:
        citation = " - google"
    return citation
# Make calculations
'''
def calculate(request):
    if "CALORIE" in request:
        sex = str(input('::Sex (m/f):   '))
        age = int(input('::Age (num):   '))
        height = int(input('::Height (in inches):    '))
        weight = int(input('::Weight (in ibs):    '))
        if "F" or "FEMALE" in sex.upper():
            bmr = round((10*weight) + (6.25*height) - (5*age) - 161)
        else:
            bmr = round((10*weight) + (6.25*height) - (5*age) + 161)
        return ("::Daily Energy Expenditure: " + str(bmr) + " cal")
        return
    if "BMI" or "WEIGHT" in request:
        height = int(input('::Height (in inches):    '))
        weight = int(input('::Weight (in ibs):    '))
        bmi = round(((weight/(height**2)) * 703), 1)
        if bmi <= 18.5:
            bmi = ("::Your BMI is: " + str(bmi) + " (Underweight)")
        if bmi >= 18.5 and bmi <= 24.9:
            bmi = ("::Your BMI is: " + str(bmi) + " (Normal healthy weight)")
        if bmi >= 25.0 and bmi <= 29.9:
            bmi = ("::Your BMI is: " + str(bmi) + " (Overweight)")
        if bmi >= 30.0 and bmi <= 39.9:
            bmi = ("::Your BMI is: " + str(bmi) + " (Obese)")
        if bmi >= 40.0:
            bmi = ("::Your BMI is: " + str(bmi) + " (Morbidly obese)")
        return
    '''  
# Analyze user input and decide what to return
def Analyze(request):
    try:
        #Close request
        if "BYE" in request or "CLOSE" in request or "EXIT" in request:
            return ("Bye Bye")
        if "CALCULATE" in request:
            calculate(request)
            return
        if "HELLO" in request or "HI" in request:
            return ("Hello, how may I be of assistance?")
        # Crisis handling
        bad_words = ['SUICIDE', 'KILL', 'DIE', 'SUFFERING', 'DEPRESSION']
        if any(x in request for x in bad_words):
            return ("If you are in crisis, please go to your local hospital or call 911 immediately")
            
        
        # Info request handling
        info = ("No predicted result found")
        try:
            # List
            info = browser.find_element(By.XPATH, "//ul[@class='i8Z77e']").text
            if info == "":
                raise Exception()
        except:
            try:
                # General Snippet
                info = browser.find_element(By.XPATH, "//span[@class='hgKElc']").text
                if info == "":
                    raise Exception()
            except:
                try:
                    # Dictionary definition
                    info = browser.find_element(By.XPATH, "//div[@style='display:inline']/span").text
                    if info == "":
                        raise Exception()
                except:
                    info = browser.find_element(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']").text
        return info
    except:
        return ("***Something unexpected happened***")    
# Get Request
def process_request(request):
    # Get user search
    # Perform search
    browser.get('https://www.google.com/search?q=' + request)
    #Analyze(spell_check(request))
    return Analyze(request), cite()