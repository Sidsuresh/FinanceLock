from tkinter import *
from PIL import ImageTk, Image


def acnt_conf():
	
	global bg_accnf

	top_accnf = Toplevel()
	top_accnf.title("Confirmation Page")
	top_accnf.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_accnf = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_accnf, width = 800, height = 547)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_accnf, anchor = "nw")
	my_canvas.create_text(400, 250, text = "Your Account has been successfully created", font = ("Helvetica", 25, "bold"), fill = "steel blue")
	top_accnf.grab_set()

	close_button = Button (top_accnf, text = "Close", command = top_accnf.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	close_button_win = my_canvas.create_window(400, 350, window = close_button)
