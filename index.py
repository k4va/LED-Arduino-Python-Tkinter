from tkinter import *
from tkinter import ttk
from com import *

class interfaz:
    def __init__(self, window):

        def closeInt():
            arduino.close()
            self.wind.destroy()

        self.wind = window
        self.wind.title('Arduino - Python')

        #Create Container
        frame = LabelFrame(self.wind, text = 'Enceder LED en Arduino con Python')
        frame.grid(row = 0, column = 0, pady = 20)

        #Button ON
        ttk.Button(frame, text = 'Encender', command = encenderLED).grid(row = 1, column = 0)

        #Button OFF
        ttk.Button(frame, text = 'Apagar', command = apagarLED).grid(row = 1, column = 2)

        #Button EXIT
        ttk.Button(frame, text = 'Exit', command = closeInt).grid(row = 2, column = 1)


if __name__ == '__main__':
    window = Tk()
    application = interfaz(window)
    window.mainloop()
        