from tkinter import *
from PIL import ImageTk, Image


def create_loan():

	def submit():
		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to submit your application? ")
		if response == 1:
			top_cr_l.destroy()

	def back():
		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to cancel your application? ")
		if response == 1:
			top_cr_l.destroy()

	global bg_cr_l

	top_cr_l = Toplevel()
	top_cr_l.title("Submit Your Loan Application")
	top_cr_l.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	#top_ca.attributes('-topmost', 'true')

	bg_cr_l = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_cr_l, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_cr_l, anchor = "nw")
	my_canvas.create_text(635, 100, text = "Enter your Loan Details", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(450, 300, text = "Type: ", font = ("Helvetica", 15), fill = "steel blue")
	cr_type = Entry(top_cr_l, width = 50, borderwidth = 1)
	cr_type_win = my_canvas.create_window(665, 300, window = cr_type)

	my_canvas.create_text(450, 350, text = "Amount: ", font = ("Helvetica", 15), fill = "steel blue")
	cr_amt = Entry(top_cr_l, show = "*", width = 50, borderwidth = 1)
	cr_amt_win = my_canvas.create_window(665, 350, window = cr_amt)

	my_canvas.create_text(450, 400, text = "Collateral: ", font = ("Helvetica", 15), fill = "steel blue")
	cr_coll = Entry(top_cr_l, show = "*", width = 50, borderwidth = 1)
	cr_coll_win = my_canvas.create_window(665, 400, window = cr_coll)

	submit_button = Button (top_cr_l, text = "Submit", command = next)
	submit_button_win = my_canvas.create_window(750, 475, window = submit_button)

	goback_button = Button (top_cr_l, text = "Cancel", command = back)
	goback_button_win = my_canvas.create_window(550, 475, window = goback_button)