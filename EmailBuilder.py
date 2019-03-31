from selenium import webdriver
from time import sleep

def makingCosmetics():
    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.get('https://www.making-cosmetics.it/lista-espositori')

    nomi =browser.find_elements_by_class_name("ex_name")
    print(len(nomi))
    for k in range(96,len(nomi)):
        sleep(1)
        nomi =browser.find_elements_by_class_name("ex_name")
        for a in nomi[k].find_elements_by_tag_name("a"):
            print("LOL\t %s" %(a.text))
            cookiePrompt = browser.find_element_by_class_name("cookie-prompt")
            browser.execute_script('arguments[0].style.visibility = "hidden";',cookiePrompt)

            cookiePromptWrapper = browser.find_element_by_id("cookie-prompt-wrapper")
            browser.execute_script('arguments[0].style.visibility = "hidden";',cookiePromptWrapper)
            
            a.click()
            sleep(1)
            try:
                
                span=browser.find_elements_by_class_name("details-text")[1]
                if "@" in span.text:
                    salvaEmail(span.text)
            except IndexError:
                print("\nErrorino \n")
            sleep(1)
            browser.back()

def salvaEmail(email):
    file = open("/home/alex/Documents/igstand/espositoriMscpe.txt", "a")
    file.writelines(email+ "\n")

def mecsd():
    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.get('http://www.mecspe.com/it/catalogo-online-espositori/espositori/')

    #table =browser.find_elements_by_id("exhibitors_table")
    #nomi = table[0].find_elements_by_tag_name("a")
    #print(len(nomi))
    #looppagine
    for i in range(2,102):
    	browser.get('http://www.mecspe.com/it/catalogo-online-espositori/espositori/'+ str(i)+"/")
    	print("i= \t %s" %(str(i)))
    	for k in range(20):
        	sleep(1)
        	table =browser.find_elements_by_id("exhibitors_table")
        	print(len(table))
        	nomi = table[0].find_elements_by_tag_name("a")
       		nomi[k].click()
        	print("k:\t %s\n" %(str(k)))
        	sleep(1)
        	try:
        		li=browser.find_elements_by_tag_name("li")
        		for k in li:
					if "@" in k.text:
						salvaEmail(k.text.replace("Email: ", ""))
        	except IndexError:
        		print("\nErrorino \n")
			sleep(1)
			browser.back()
			sleep(1)

if __name__ == "__main__":
    mecsd()