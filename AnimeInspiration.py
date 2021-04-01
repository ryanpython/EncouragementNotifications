import time
import random
from plyer import notification
from tkinter import *



#Quotes that can be randomly chosen
Quotes = ('Its meaningless to just live, and its meaningless to just fight. I want to win. - Ichigo', 
'The difference in ability, what about it? Do you think I should give up just because you are stronger than me? - Ichigo'
'A dream... It is something you do for yourself, not for others - Griffith'
'You think something like that would hurt, after all I have been through? - Ken Kenaki'
'Why is it that the beautiful things are entwined more deeply with death than with life? - Ken Kenaki'
'Sanity... what would I do with a useless thing like that? - Kenpachi Zeraki'
'You idiot! There is always shadows wherever there is light! - Kenpachi Zeraaki'
'Hate is a place, where a man who cannot stand sadness, goes. - Godo'
"I'm sure you'll overcome this. You'll walk again... soon. - Guts"
"FUCK YOU. I'm human, the real deal, right down to the fuckin' marrow of my bones. - Guts"
"I'd rather fight for my life than live it. - Guts"
)


#App Title
title = 'AnimeInspired'


#Variable for random quotes to be displayed in messages
message = random.choice(Quotes)


#App Picture
app_icon = None
AppStart = notification.notify(title= title, message= message, app_icon= app_icon, timeout= 5, toast=False)

root = Tk()
root.title('AnimeInspired')
root.geometry("1200x1200")


myLabel = Label(root, text="Welcome to AnimeInspired")
myLabel.pack()

notifyMebutton = Button(root, text ="Start Notifying Me", command= AppStart)
notifyMebutton.pack()



AboutUs = Button(root, text ="About Us")
AboutUs.pack()
            





root.mainloop()
