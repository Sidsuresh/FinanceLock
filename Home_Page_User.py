from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from Create_Loan import *
from Loan_History_User import *
from Payment_Page import *

def home_pg_user(Uid):

	def next_but():
		if i.get() == 1:
			create_loan(Uid)
		elif i.get() == 2:
			view_det(Uid)
		else:
			payment_page()

	global bg_hpu

	root1 = Toplevel()
	root1.title("Home Page User")
	root1.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_hpu = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(root1, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_hpu, anchor = "nw")
	my_canvas.create_text(635, 150, text = "Choose your Services", font = ("Helvetica", 25, "bold"), fill = "steel blue")
	my_canvas.create_rectangle(450, 275, 830, 440, outline = "black", fill = "white")

	i = IntVar()
	i.set("1")
	r1 = Radiobutton(root1, text = "Apply for a Loan", value = 1, variable = i, background = 'white')
	r2 = Radiobutton(root1, text = "View Current or Previous Loan Details", value = 2, variable = i, background = 'white')
	r3 = Radiobutton(root1, text = "Payment Services", value = 3, variable = i, background = 'white')
	r1_win = my_canvas.create_window(515, 310, window = r1)
	r2_win = my_canvas.create_window(570, 340, window = r2)
	r3_win = my_canvas.create_window(517, 370, window = r3)

	next_button = Button (root1, text = "Next", command = next_but, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(750, 415, window = next_button)

	goback_button = Button (root1, text = "Log Out", background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	goback_button_win = my_canvas.create_window(525, 415, window = goback_button)
	root1.grab_set()

	#my_canvas.create_line(0, 400, 1300, 400, fill = "steel blue")