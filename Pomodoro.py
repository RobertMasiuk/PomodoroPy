import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound

timeNow = dt.datetime.now()
timeSesion = 25*60
timeDelta = dt.timedelta(0, timeSesion)
timeFuture = timeNow + timeDelta
timeBrake = 5*60
timeFinal = timeNow + dt.timedelta(0, timeSesion+timeBrake)

root = tkinter.Tk()
root.windraw()

messagebox.showinfo("tomato timer started!, \n It is now" + timeNow.strftime("%H:%M") + " hrs. \nSesion time equal 25min." )

total_pomodoro = 0
brakes = 0

while True:
    if(timeNow < timeFuture):
        print("pomodoro")
    elif(timeFuture <= timeNow <= timeFinal):
        print("in brake")
        if brakes == 0:
            print("if brake")
            for i in range(5):
                winsound.Beep((i+100), 700)
            print(('Brake time'))
            brakes +=1
        else:
            print('finished')
            brakes = 0
            for i in range(10):
                winsound.Beep((i+100), 500)

            usr_ans = messagebox.askyesno("tomato timer stop! Would you like start again?")
            total_pomodoro +=1
            if usr_ans == True:
                timeNow = dt.datetime.now()
                timeFuture = timeNow + dt.datetime(0, timeSesion)
                timeFuture = timeNow + dt.datetime(0, timeSesion + timeDelta)
            elif usr_ans == False:
                messagebox.showinfo("tomato timer finished")
                brakes
    print("sleeping")
    time.sleep(20)
    timeNow = dt.datetime.now()
    timenow = timeNow.strftime("%H:%M")