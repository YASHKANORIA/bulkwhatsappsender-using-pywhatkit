import pywhatkit as kit
import pandas as pd
from datetime import datetime
import pandas as pd

#csv Data
data = pd.read_csv("E:\python\contact.csv")
data_dict = data.to_dict('list')
leads = data_dict['Number']
print (leads)

now = datetime.now()


text='hey test'


#by adding number here
# mylist =["+919903028438 ","+919831285176","+917003266100"]
# print (mylist)


j=0;
for i in leads:
    hour = now.strftime("%H")
    min = now.strftime("%M")
    mini = int(min) + 2 +j
    #without using csv file

    # kit.sendwhatmsg(i, text, int(hour), mini)
    #using Csv File
    kit.sendwhatmsg("+91"+str(i), text, int(hour), mini)
    j=j+1


#Yash Kanoria






