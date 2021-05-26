from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pyrebase


def create_loan(Uid):

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

	db = firebase.database()

	def submit():

		if(len(cr_type.get()) == 0 or len(cr_amt.get()) == 0 or len(cr_coll.get()) == 0):
			messagebox.showwarning("Warning", "All the details must be submitted")

		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to submit your application? ")
		if response == 1:
			for r in record:
				if(r.val()['name'] == click_inv.get()):
					UIid = r.key()
			data_good = {'type': cr_type.get(),'amt': cr_amt.get(), 'collateral': cr_coll.get(), 'date': cr_date.get(), 'uniqueCid': Uid, 'uniqueIid': UIid, 'status': "Processing"}
			db.child("Loan").child("Request").push(data_good)

			data = {'uniqueInvid': UIid, 'uniqueCid': Uid}
			db.child("CustandInv").push(data)
			top_cr_l.destroy()

	def back():
		response = messagebox.askyesno("Are You Sure?", "Are you sure you want to cancel your application? ")
		if response == 1:
			top_cr_l.destroy()

	global bg_cr_l

	top_cr_l = Toplevel()
	top_cr_l.title("Submit Your Loan Application")
	top_cr_l.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_cr_l.grab_set()

	bg_cr_l = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_cr_l, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_cr_l, anchor = "nw")
	my_canvas.create_text(635, 150, text = "Enter your Loan Details", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(430, 250, 860, 570, outline = "black", fill = "white")

	my_canvas.create_text(470, 300, text = "Type: ", font = ("Helvetica", 14), fill = "steel blue")
	cr_type = Entry(top_cr_l, width = 50, borderwidth = 1)
	cr_type_win = my_canvas.create_window(700, 300, window = cr_type)

	my_canvas.create_text(480, 350, text = "Amount: ", font = ("Helvetica", 14), fill = "steel blue")
	cr_amt = Entry(top_cr_l, width = 50, borderwidth = 1)
	cr_amt_win = my_canvas.create_window(700, 350, window = cr_amt)

	my_canvas.create_text(485, 400, text = "Collateral: ", font = ("Helvetica", 14), fill = "steel blue")
	cr_coll = Entry(top_cr_l, width = 50, borderwidth = 1)
	cr_coll_win = my_canvas.create_window(700, 400, window = cr_coll)

	my_canvas.create_text(470, 450, text = "Date: ", font = ("Helvetica", 14), fill = "steel blue")
	cr_date = Entry(top_cr_l, width = 50, borderwidth = 1)
	cr_date_win = my_canvas.create_window(700, 450, window = cr_date)

	my_canvas.create_text(485, 500, text = "Investor: ", font = ("Helvetica", 14), fill = "steel blue")
	#cr_date = Entry(top_cr_l, width = 50, borderwidth = 1)
	#cr_date_win = my_canvas.create_window(700, 450, window = cr_date)
	record = db.child("People").child("Investor").get()
	investor = []
	for r in record:
		investor.append(r.val()['name'])
	click_inv = StringVar()
	click_inv.set(investor[0])
	e_inv = OptionMenu(top_cr_l, click_inv, *investor)
	e_inv_win = my_canvas.create_window(625, 500, window = e_inv)

	submit_button = Button (top_cr_l, text = "Submit", command = submit, background = "white", highlightbackground = "black", highlightthickness = 2)
	submit_button_win = my_canvas.create_window(750, 550, window = submit_button)

	goback_button = Button (top_cr_l, text = "Cancel", command = back, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(550, 550, window = goback_button)
	top_cr_l.grab_set()