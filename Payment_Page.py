from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from Conf_Payment import *
import pyrebase
from tkinter import messagebox

def payment_page(Uid):

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

	def proceed():
		if float(pp_amt.get()) == 0:
			messagebox.showwarning("Error", "Payment is complete")
			top_pp.destroy()
		else:
			chkInd = record.index(click_loan.get())
			loanid = loanID[chkInd]

			try:
				acnt = db.child('Accounts').get()
				for l in acnt:
					if l.val()['loan_id'] == loanid:
						amt = l.val()['amnt']
						loankey = l.key()
						bal = l.val()['payment']
				conf_pay(Uid, loanid, loankey, amt, bal)
				top_pp.destroy()
			except:
				pass	

	def submit():
		chkInd = record.index(click_loan.get())
		loanid = loanID[chkInd]
		pp_lid.configure(state = 'normal')
		pp_lid.delete(0, END)
		pp_lid.insert(0, loanid)
		pp_lid.config(state = 'disabled')
		bal = 0

		try:
			acnt = db.child('Accounts').get()
			for l in acnt:
				if l.val()['loan_id'] == loanid:
					loankey = l.key()
					if float(l.val()['amnt']) == 0:
						bal = 0
					else:
						bal = l.val()['payment']
		except:
			pass

		#print(loankey)
		pp_amt.configure(state = 'normal')
		pp_amt.delete(0, END)
		pp_amt.insert(0, bal)
		pp_amt.config(state = 'disabled')

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

	my_canvas.create_rectangle(430, 300, 860, 490, outline = "black", fill = "white")

	apt_loan = []
	try:
		loan_apt = db.child("Loan").child("Accept").get()
		for l in loan_apt:
			if l.val()['uniqueCid'] == Uid:
				apt_loan.append(l)
	except:
		e_pass

	record = []
	loanID = []
	try:
		for l in apt_loan:
			record.append(l.key() + " - " + l.val()['type'])
			loanID.append(l.key())
	except:
		pass

	my_canvas.create_text(482, 250, text = "Choose Loan: ", font = ("Helvetica", 14), fill = "steel blue")
	click_loan = StringVar()
	e_loan = OptionMenu(top_pp, click_loan, *record)
	e_loan_win = my_canvas.create_window(700, 250, window = e_loan)

	sub_button = Button(top_pp, text = "Submit", command = submit, background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_button_win = my_canvas.create_window(885, 250, window = sub_button)

	my_canvas.create_text(482, 350, text = "Loan ID: ", font = ("Helvetica", 14), fill = "steel blue")
	pp_lid = Entry(top_pp, width = 50, borderwidth = 1, state = 'disabled')
	pp_lid_win = my_canvas.create_window(700, 350, window = pp_lid)

	my_canvas.create_text(480, 400, text = "Amount: ", font = ("Helvetica", 14), fill = "steel blue")
	pp_amt = Entry(top_pp, width = 50, borderwidth = 1, state = 'disabled')
	pp_amt_win = my_canvas.create_window(700, 400, window = pp_amt)

	next_button = Button(top_pp, text = "Proceed", command = proceed, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(750, 465, window = next_button)

	goback_button = Button(top_pp, text = "Cancel", background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	goback_button_win = my_canvas.create_window(525, 465, window = goback_button)

	
