import time
from plyer import notification
if __name__=="__main__":
    title = 'From Guts'
    app_name = 'Anime Inspiration'
    message = 'This is no different from any other war, nothing I cant handle, nothing'
    notification.notify(title= title, app_name = app_name, message= message, app_icon= None, timeout= 10, toast=False)
time.sleep(5)