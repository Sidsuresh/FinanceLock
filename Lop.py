from tkinter import *
from PIL import ImageTk, Image
from Create_Loan import *

def open_login():
	
	global bg_lp

	top_lp = Toplevel()
	top_lp.title('Log - in')
	top_lp.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_lp = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_lp, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_lp, anchor = "nw")
	my_canvas.create_text(635, 150, text = "Sign - in", font = ("Helvetica", 25), fill = "steel blue")

	#my_canvas.create_text(550, 250, text = "Username: ", font = ("Helvetica", 15), fill = "white")
	'''
	lp_frame = Frame(top_lp, pady = 5, fg = "white")
	lp_frame_win = my_canvas.create_window(650, 400, window = lp_frame)
	'''

	my_canvas.create_rectangle(450, 225, 835, 505, outline = "black", fill = "white")

	my_canvas.create_text(643, 250, text = "Select your Account Type: ", font = ("Helvetica", 20), fill = "steel blue")

	i = IntVar()
	r1 = Radiobutton(top_lp, text = "Customer", value = 1, variable = i)
	r2 = Radiobutton(top_lp, text = "Investor", value = 2, variable = i)
	r1_win = my_canvas.create_window(523, 300, window = r1)
	r2_win = my_canvas.create_window(518, 330, window = r2)

	e_user = Entry(top_lp, width = 50, borderwidth = 1)
	e_user.insert(0, "Username: ")
	e_user_win = my_canvas.create_window(635, 380, window = e_user)

	e_pass = Entry(top_lp, show = "*", width = 50, borderwidth = 1)
	e_pass.insert(0, "Password: ")
	e_pass_win = my_canvas.create_window(635, 430, window = e_pass)

	login_button = Button (top_lp, text = "Log In", command = create_loan)
	login_button_win = my_canvas.create_window(620, 480, window = login_button)

	goback_button = Button (top_lp, text = "Back", command = top_lp.destroy)
	goback_button_win = my_canvas.create_window(525, 480, window = goback_button)

	forpas_button = Button (top_lp, text = "Forget Password")
	forpas_button_win = my_canvas.create_window(730, 480, window = forpas_button)

