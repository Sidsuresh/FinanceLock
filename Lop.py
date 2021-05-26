from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Home_Page_User import *
from Home_Page_Inves import *
import pyrebase

def open_login():

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

	auth = firebase.auth();
	db = firebase.database();

	def click():
		top_lp.grab_set()
		if(i.get() == 1):
			try:
				auth.sign_in_with_email_and_password(e_user.get(), e_pass.get())
				people = db.child("People").child("Customer").get()
				
				for person in people.each():
					if person.val()['email'] == e_user.get():
						UCid = person.key()
						print(UCid)

				home_pg_user(UCid)
				top_lp.destroy()
			except:
				messagebox.showerror("Error", "Invalid Username or Password")

		else:
			try:

				auth.sign_in_with_email_and_password(e_user.get(), e_pass.get())
				people = db.child("People").child("Investor").get()
				
				for person in people.each():
					if person.val()['email'] == e_user.get():
						UIid = person.key()
						print(UIid)

				home_pg_inves(UIid)
				top_lp.destroy()
			except:
				messagebox.showerror("Error", "Invalid Username or Password")

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
	r1 = Radiobutton(top_lp, text = "Customer", value = 1, variable = i, background = "white")
	r2 = Radiobutton(top_lp, text = "Investor", value = 2, variable = i, background = "white")
	r1_win = my_canvas.create_window(523, 300, window = r1)
	r2_win = my_canvas.create_window(518, 330, window = r2)

	e_user = Entry(top_lp, width = 50, borderwidth = 1)
	e_user.insert(0, "Username:")
	e_user_win = my_canvas.create_window(635, 380, window = e_user)

	e_pass = Entry(top_lp, show = "*", width = 50, borderwidth = 1)
	e_pass.insert(0, "Password:")
	e_pass_win = my_canvas.create_window(635, 430, window = e_pass)

	login_button = Button (top_lp, text = "Log In", command = click, background = "white", highlightbackground = "black", highlightthickness = 2)
	login_button_win = my_canvas.create_window(620, 480, window = login_button)

	goback_button = Button (top_lp, text = "Back", command = top_lp.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(525, 480, window = goback_button)

	forpas_button = Button (top_lp, text = "Forget Password", background = "white", highlightbackground = "black", highlightthickness = 2)
	forpas_button_win = my_canvas.create_window(730, 480, window = forpas_button)

