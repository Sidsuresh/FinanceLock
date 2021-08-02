from tkinter import *
from Lop import *
from Choose_Create import *
from CAA_User import *
from PIL import ImageTk, Image
from tkinter import font

root = Tk()
root.title("Financelock")
root.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

bg = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))


my_canvas = Canvas(root, width = 1300, height = 733)
my_canvas.pack(fill = "both", expand = True)

my_canvas.create_image(0, 0, image = bg, anchor = "nw")

myfont = font.Font(family='Helvetica', size = 25, weight="bold")

my_canvas.create_text(635, 150, text = "Welcome to Financelock", font = myfont, fill = "steel blue")

logo = ImageTk.PhotoImage(Image.open("BG/logore.jpeg"))
my_canvas.create_image(100, 25, image = logo)

my_canvas.create_rectangle(275, 275, 525, 375, outline = "black", fill = "white")

my_canvas.create_text(400, 300, text = "For New Users...", font = ("Helvetica", 20), fill = "steel blue")
caa_button = Button (root, text = "Create an Account", command = chk_caa, background = "white", highlightbackground = "black", highlightthickness = 2)
caa_button_win = my_canvas.create_window(400, 350, window = caa_button)

my_canvas.create_rectangle(750, 275, 1050, 375, outline = "black", fill = "white")

my_canvas.create_text(900, 300, text = "For Existing Users...", font = ("Helvetica", 20), fill = "steel blue")
log_button = Button (root, text = "Log In", command = open_login, background = "white", highlightbackground = "black", highlightthickness = 2)
log_button_win = my_canvas.create_window(900, 350, window = log_button)

root.mainloop()