import time
from datetime import datetime as dt
  
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1" # localhost's IP
  
# websites That you want to block
website_list = ["https://www.facebook.com/"]

while True:
  
    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day,14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,15):
        with open(hosts_path, 'r+') as file: # Open the file in both read and write mode
            content = file.read() #Read the content
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n") #Write down the websites that we wich to block
        print("Working hours.. Sorry your sites are blocked..")
    else:
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) #Set the cursor at the beginning of the file
            for line in content:
                #Applying list comprehension checks for those lines which are not in website_list and writes them in the file
                if not any(website in line for website in website_list):  
                    file.write(line)
  
            file.truncate() #Truncate the rest of the portion thus removing the lines containing website names belonging to website_list
  
        print("Fun hours.. You can access your sites")

    time.sleep(5)
