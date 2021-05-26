from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from Conf_Payment import *

def payment_page():
	global bg_pp

	top_pp = Toplevel()
	top_pp.title("Payment Page")
	top_pp.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_pp.grab_set()

	bg_pp = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_pp, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_pp, anchor = "nw")
	my_canvas.create_text(635, 125, text = "Payment Page", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(430, 250, 860, 440, outline = "black", fill = "white")

	my_canvas.create_text(482, 300, text = "Loan ID: ", font = ("Helvetica", 14), fill = "steel blue")
	pp_lid = Entry(top_pp, width = 50, borderwidth = 1)
	pp_lid_win = my_canvas.create_window(700, 300, window = pp_lid)

	my_canvas.create_text(480, 350, text = "Amount: ", font = ("Helvetica", 14), fill = "steel blue")
	pp_amt = Entry(top_pp, width = 50, borderwidth = 1)
	pp_amt_win = my_canvas.create_window(700, 350, window = pp_amt)

	next_button = Button(top_pp, text = "Proceed", command = conf_pay, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(750, 415, window = next_button)

	goback_button = Button(top_pp, text = "Cancel", background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	goback_button_win = my_canvas.create_window(525, 415, window = goback_button)

	
