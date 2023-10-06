import tkinter
# aplikacje okieniowe

class MyGui:
    def __init__(self): # konskutor
        self.main_window = tkinter.Tk()


        self.label3 = tkinter.Label(self.main_window, text='Napisalem wlasny program, w okienku')
        self.label4 = tkinter.Label(self.main_window, text='narazie nic on nie robi')
        self.label5 = tkinter.Label(self.main_window, text='poza tym, ze sie wyswietla')
        self.label1 = tkinter.Label(self.main_window, text='HALO')
        self.label2 = tkinter.Label(self.main_window, text='Witajcie')


        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='top')
        self.label4.pack(side='bottom')
        self.label5.pack(side='right')


        tkinter.mainloop()

my_gui = MyGui()