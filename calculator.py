import tkinter
import math


def analyse():
    fr = float(freq_text.get())
    fr *= (10 ** 9)
    er = float(eps_text.get())
    h = float(height_text.get())

    # Calculations
    f = (8.791 * 10 ** 9) / (fr * math.sqrt(er))
    # f = round(f, 4)
    b = (math.log(math.pi * f, math.e) - math.log(2*h, math.e))
    c = (2 * h / (math.pi * er * f))
    a = (f/math.sqrt(1 + c * (b + 1.7726)))
    print(f)

    print("Fr = {0}, er = {1}, h = {2}".format(fr, er, h))
    a_text.set(round(a, 4))


mainWindow = tkinter.Tk()

mainWindow.title("Circular Patch Calculator")
mainWindow.geometry("640x480")
mainWindow['padx'] = 5
mainWindow['pady'] = 5

# Tkinter Variables
freq_text = tkinter.StringVar()
height_text = tkinter.StringVar()
eps_text = tkinter.StringVar()
a_text = tkinter.StringVar()
box_text = tkinter.StringVar()

# Heading
tkinter.Label(mainWindow, text='Circular Patch Antenna Calculator', font=('Times New Roman', 18, 'bold')).grid(row=0, column=0, columnspan=3)

# Label
tkinter.Label(mainWindow, text='Design Frequency', anchor='w', font=('Times New Roman', 10, 'bold')).grid(row=1, column=0, sticky='ew')
tkinter.Label(mainWindow, text='Height of the Substrate', anchor='w', font=('Times New Roman', 10, 'bold')).grid(row=2, column=0, sticky='ew')
tkinter.Label(mainWindow, text='Dielectric Constant of Substrate', anchor='w' , font=('Times New Roman', 10, 'bold')).grid(row=3, column=0, sticky='ew')
tkinter.Label(mainWindow, text='Radius of Patch ', anchor='w', font=('Times New Roman', 10, 'bold')).grid(row=4, column=0, sticky='ew')

# Units Label
tkinter.Label(mainWindow, text='GHz', anchor='w').grid(row=1, column=3, sticky='e')
tkinter.Label(mainWindow, text='cm', anchor='w').grid(row=2, column=3, sticky='e')
tkinter.Label(mainWindow, text='cm', anchor='w').grid(row=4, column=3, sticky='e')

# Entry Box
tkinter.Entry(mainWindow, textvariable=freq_text, background='floral white').grid(row=1, column=1, sticky='ew')
tkinter.Entry(mainWindow, textvariable=height_text, background='floral white').grid(row=2, column=1, sticky='ew')
tkinter.Entry(mainWindow, textvariable=eps_text, background='floral white').grid(row=3, column=1, sticky='ew')
tkinter.Entry(mainWindow, textvariable=a_text, background='floral white').grid(row=4, column=1, sticky='ew')

# Buttons
Analyse_Button = tkinter.Button(mainWindow, text='Analyse', width=25, command=analyse).grid(row=5, column=0)
Close_Button = tkinter.Button(mainWindow, text='Exit', command=exit).grid(row=5, column=1, sticky='ew')

# Formula
# image1 =tkinter.PhotoImage(file='formula.png')
# image_label = tkinter.Label(mainWindow, image=image1)
# image_label.grid(row=7,column=1)

if __name__ == "__main__":
    mainWindow.mainloop()
