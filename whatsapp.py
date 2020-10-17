import pywhatkit as kit
import pandas as pd
from datetime import datetime


now = datetime.now()


text='hey test'



mylist =["+919903028438 ","+919831285176"]
print (mylist)


j=0;
for i in mylist:
    hour = now.strftime("%H")
    min = now.strftime("%M")
    mini = int(min) + 2 +j
    j=0
    kit.sendwhatmsg(i, text, int(hour), mini)
    j=j+1


#kit.sendwhatmsg("+919831285176", "I love studytonight.com!",00 , )






