from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from AcntConf import *

def user_pass_inves():

	def next():

		if len(e_pass.get()) == 0 or len(e_conpass.get()) == 0:
			my_canvas.create_text(635, 435, text = "Passwords cannot be empty", font = ("Helvetica", 15), fill = "steel blue", tag = "empty")
		elif e_pass.get() != e_conpass.get():
			my_canvas.delete("empty")
			my_canvas.create_text(632, 435, text = "Both Passwords should be equal", font = ("Helvetica", 15), fill = "steel blue", tag = "Unequal")
		else:
			acnt_conf()
			top_upi.destroy()

	def back():
		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to cancel your account ? ")
		if response == 1:
			top_upi.destroy()

	global bg_upi

	top_upi = Toplevel()
	top_upi.title("Enter your Username and Password")
	top_upi.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_upi = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_upi, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_upi, anchor = "nw")
	my_canvas.create_text(635, 150, text = "Create your Credentials: ", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(425, 300, text = "Username: ", font = ("Helvetica", 15), fill = "steel blue")
	e_user = Entry(top_upi, width = 50, borderwidth = 1)
	e_user_win = my_canvas.create_window(635, 300, window = e_user)

	my_canvas.create_text(425, 350, text = "Password: ", font = ("Helvetica", 15), fill = "steel blue")
	e_pass = Entry(top_upi, show = "*", width = 50, borderwidth = 1)
	e_pass_win = my_canvas.create_window(635, 350, window = e_pass)

	my_canvas.create_text(400, 400, text = "Confirm Password: ", font = ("Helvetica", 15), fill = "steel blue")
	e_conpass = Entry(top_upi, show = "*", width = 50, borderwidth = 1)
	e_conpass_win = my_canvas.create_window(635, 400, window = e_conpass)

	next_button = Button (top_upi, text = "Next", command = next)
	next_button_win = my_canvas.create_window(750, 475, window = next_button)

	goback_button = Button (top_upi, text = "Cancel", command = back)
	goback_button_win = my_canvas.create_window(525, 475, window = goback_button)

	top_upi.grab_set()


