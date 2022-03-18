import time
import tkinter as tk
from tkinter import messagebox
import beepy


class App:
    def __init__(self):
        self.root = tk.Tk()
        #  self.root.config(bg='#66FF66')
        self.root.geometry('300x250')
        self.root.title('timer')
        self.s, self.m, self.h = tk.StringVar(), tk.StringVar(), tk.StringVar()

        tk.Entry(self.root, textvariable=self.s, width=3, font='Helvetica 14').place(x=180, y=20)
        tk.Entry(self.root, textvariable=self.m, width=3, font='Helvetica 14').place(x=130, y=20)
        tk.Entry(self.root, textvariable=self.h, width=3, font='Helvetica 14').place(x=80, y=20)
        self.s.set('00')
        self.m.set('00')
        self.h.set('00')

        self.btn = tk.Button(self.root, text='Set Time Countdown', bd='5', command=self.submit)
        self.btn.place(x=70, y=120)

        self.stop_btn = tk.Button(self.root, text='Stop', bd='5', command=self.destroy)
        self.stop_btn.place(x=110, y=150)

    def submit(self):
        try:
            temp = int(self.h.get()) * 3600 + int(self.m.get()) * 60 + int(self.s.get())
        except:
            print("Please input the right value")
        while temp > -1:
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            self.h.set("{0:2d}".format(hours))
            self.m.set("{0:2d}".format(mins))
            self.s.set("{0:2d}".format(secs))
            self.root.update()
            time.sleep(1)

            if temp == 0:
                t = '{}:{}'.format(time.localtime().tm_hour, time.localtime().tm_min)
                print('timer finished at {}'.format(t))
                beepy.beep(sound='ping')

            temp -= 1

    def destroy(self):
        t = '{}:{}'.format(time.localtime().tm_hour, time.localtime().tm_min)
        print('I am changing root at {}'.format(t))
        self.root.destroy()
        self.__init__()
        self.run()

    def run(self):
        self.root.mainloop()


timer = App()
timer.run()
