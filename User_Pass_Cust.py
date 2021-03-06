from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from AcntConf import *
import pyrebase

def user_pass_cust(email):

	firebase_config = {
		"apiKey" : "AIzaSyCvuNFssXW4k1cHifCRH_-KP6IPuxJHzqk",
	    "authDomain" : "financelock-c6ea8.firebaseapp.com",
	    "databaseURL" : "https://financelock-c6ea8-default-rtdb.firebaseio.com",
	    "projectId" : "financelock-c6ea8",
	    "storageBucket" : "financelock-c6ea8.appspot.com",
	    "messagingSenderId" : "523873568466",
	    "appId" : "1:523873568466:web:b4259e5cb0e1c85059cf0b",
	    "measurementId" : "Gender-R1R8CZD552"
	}

	firebase = pyrebase.initialize_app(firebase_config)

	auth = firebase.auth()

	def next():

		if len(e_pass.get()) == 0 or len(e_conpass.get()) == 0:
			my_canvas.delete("Unequal")
			my_canvas.delete("Exist")
			my_canvas.create_text(635, 435, text = "Passwords cannot be empty", font = ("Helvetica", 15), fill = "steel blue", tag = "Empty")
		elif e_pass.get() != e_conpass.get():
			my_canvas.delete("Empty")
			my_canvas.delete("Exist")
			my_canvas.create_text(632, 435, text = "Both Passwords should be equal", font = ("Helvetica", 15), fill = "steel blue", tag = "Unequal")
		else:
			try:
				login = auth.create_user_with_email_and_password(e_user.get(), e_pass.get())
				auth.send_email_verification(login['idToken'])
				messagebox.showinfo("Check", "Please check your email for the verification link")
				acnt_conf()
				top_upc.destroy()
			except:
				my_canvas.delete("Unequal")
				my_canvas.delete("Empty")
				my_canvas.create_text(632, 435, text = "Email already exists", font = ("Helvetica", 15), fill = "steel blue", tag = "Exist")
			

	def back():
		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to cancel your account ? ")
		if response == 1:
			top_upc.destroy()

	global bg_upc

	top_upc = Toplevel()
	top_upc.title("Enter your Username and Password")
	top_upc.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_upc = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_upc, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_upc, anchor = "nw")
	my_canvas.create_text(635, 150, text = "Create your Credentials: ", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(425, 300, text = "Username: ", font = ("Helvetica", 15), fill = "steel blue")
	e_user = Entry(top_upc, width = 50, borderwidth = 1)
	e_user.insert(0,str(email))
	e_user_win = my_canvas.create_window(635, 300, window = e_user)

	my_canvas.create_text(425, 350, text = "Password: ", font = ("Helvetica", 15), fill = "steel blue")
	e_pass = Entry(top_upc, show = "*", width = 50, borderwidth = 1)
	e_pass_win = my_canvas.create_window(635, 350, window = e_pass)

	my_canvas.create_text(400, 400, text = "Confirm Password: ", font = ("Helvetica", 15), fill = "steel blue")
	e_conpass = Entry(top_upc, show = "*", width = 50, borderwidth = 1)
	e_conpass_win = my_canvas.create_window(635, 400, window = e_conpass)

	next_button = Button (top_upc, text = "Next", command = next, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(750, 475, window = next_button)

	goback_button = Button (top_upc, text = "Cancel", command = back, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(525, 475, window = goback_button)

	top_upc.grab_set()


