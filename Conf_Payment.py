from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox

def conf_pay():

	def back_but():
		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to cancel your payment? ")
		if response == 1:
			top_cp.destroy()
		else:
			top_cp.grab_set()

	global bg_cp, top_cp

	top_cp = Toplevel()
	top_cp.title("Enter Payment Method")
	top_cp.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_cp.grab_set()

	bg_cp = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_cp, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_cp, anchor = "nw")
	my_canvas.create_text(635, 125, text = "Payment Method", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(400, 250, 900, 530, outline = "black", fill = "white")

	my_canvas.create_text(450, 300, text = "Bank: ", font = ("Helvetica", 14), fill = "steel blue")
	click_gen = StringVar()
	click_gen.set("Federal Bank")
	e_gen = OptionMenu(top_cp, click_gen, "Federal Bank", "HDFC", "SBI", "SBT", "Bank of Baroda", "PNB")
	e_gen_win = my_canvas.create_window(600, 300, window = e_gen)

	my_canvas.create_text(482, 350, text = "Card Number: ", font = ("Helvetica", 14), fill = "steel blue")
	cp_cn = Entry(top_cp, width = 50, borderwidth = 1)
	cp_cn_win = my_canvas.create_window(700, 350, window = cp_cn)

	my_canvas.create_text(460, 400, text = "Valid till: ", font = ("Helvetica", 14), fill = "steel blue")
	cp_vd = Entry(top_cp, width = 50, borderwidth = 1)
	cp_vd_win = my_canvas.create_window(700, 400, window = cp_vd)

	my_canvas.create_text(450, 450, text = "CVV: ", font = ("Helvetica", 14), fill = "steel blue")
	cp_cvv = Entry(top_cp, show = "*", width = 50, borderwidth = 1)
	cp_cvv_win = my_canvas.create_window(700, 450, window = cp_cvv)	

	next_button = Button(top_cp, text = "Confirm", background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(775, 500, window = next_button)

	goback_button = Button(top_cp, text = "Cancel", command = back_but, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(525, 500, window = goback_button)