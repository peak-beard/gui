import tkinter as tk

window = tk.Tk()
window.title('GUI')
def clicked():

    label = tk.Label(window, text='Hello World!', font=('Arial Bold', 12)).grid(column=0, row=0)

bt = tk.Button(window, text="Enter", bg='grey', fg='white').grid(column=1, row=0)
window.geometry('350x200')
window.mainloop()
#https://www.youtube.com/watch?v=VMP1oQOxfM0