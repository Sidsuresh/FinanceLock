from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox
import pyrebase

def view_det(Uid):

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
		chkind = record.index(click_loan.get())
		loanno = loanID[chkind]
		loansts = status[chkind]

		if loansts == "Accepted":
			aptloan = db.child("Loan").child("Accept").get()
			for l in aptloan:
				if l.key() == loanno:
					loan = l.val()
		elif loansts == "Rejected":
			rejloan = db.child("Loan").child("Reject").get()
			for l in rejloan:
				if l.key() == loanno:
					loan = l.val()
		else:
			reqloan = db.child("Loan").child("Request").get()
			for l in reqloan:
				if l.key() == loanno:
					loan = l.val()

		inv = db.child("People").child("Investor").get()
		for i in inv:
			if i.key() == loan['uniqueIid']:
				inv = i.val()['name']

		lhu_type.configure(state = 'normal')
		lhu_amt.configure(state = 'normal')
		lhu_coll.configure(state = 'normal')
		lhu_inv.configure(state = 'normal')
		lhu_st.configure(state = 'normal')
		lhu_lid.configure(state = 'normal')

		lhu_type.delete(0, END)
		lhu_amt.delete(0, END)
		lhu_coll.delete(0, END)
		lhu_inv.delete(0, END)
		lhu_st.delete(0, END)
		lhu_lid.delete(0, END)

		lhu_type.insert(0, loan['type'])
		lhu_amt.insert(0, loan['amt'])
		lhu_coll.insert(0, loan['collateral'])
		lhu_inv.insert(0, inv)
		lhu_st.insert(0, loan['status'])
		lhu_lid.insert(0, loanno)

		lhu_type.config(state = 'disabled')
		lhu_amt.config(state = 'disabled')
		lhu_coll.config(state = 'disabled')
		lhu_inv.config(state = 'disabled')
		lhu_st.config(state = 'disabled')
		lhu_lid.config(state = 'disabled')

	global bg_lhu

	top_lhu = Toplevel()
	top_lhu.title("View Loan History")
	top_lhu.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_lhu = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_lhu, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_lhu, anchor = "nw")
	my_canvas.create_text(635, 125, text = "View Loan History", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(475, 200, text = "Choose Loan: ", font = ("Helvetica", 14), fill = "steel blue")
	all_loans = []

	try: 
		loan_req = db.child("Loan").child("Request").get()
		for l in loan_req:
			if l.val()['uniqueCid'] == Uid:
				all_loans.append(l)
	except:
		#messagebox.showinfo("Empty", "No Loan Requests Available")
		pass

	try:
		loan_apt = db.child("Loan").child("Accept").get()
		for l in loan_apt:
			if l.val()['uniqueCid'] == Uid:
				all_loans.append(l)
	except:
		#messagebox.showinfo("Empty", "No Loans Accepted")
		pass

	try:			
		loan_rej = db.child("Loan").child("Reject").get()
		for l in loan_rej:
			if l.val()['uniqueCid'] == Uid:
				all_loans.append(l)
	except:
		#messagebox.showinfo("Empty", "No Loans Rejected")
		pass

	print(all_loans)
	record = []
	loanID = []
	status = []

	for l in all_loans:
		record.append(l.val()['date'] + " - " + l.val()['type'])
		loanID.append(l.key())
		status.append(l.val()['status'])

	click_loan = StringVar()
	#click_loan.set(record[0])
	e_loan = OptionMenu(top_lhu, click_loan, *record)
	e_loan_win = my_canvas.create_window(700, 200, window = e_loan)

	sub_button = Button(top_lhu, text = "Submit", command = submit, background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_button_win = my_canvas.create_window(820, 200, window = sub_button)

	my_canvas.create_rectangle(430, 250, 860, 620, outline = "black", fill = "white")

	my_canvas.create_text(470, 300, text = "Type: ", font = ("Helvetica", 14), fill = "steel blue")
	lhu_type = Entry(top_lhu, width = 50, borderwidth = 1)
	lhu_type.config(state = 'disabled')
	lhu_type_win = my_canvas.create_window(700, 300, window = lhu_type)

	my_canvas.create_text(480, 350, text = "Amount: ", font = ("Helvetica", 14), fill = "steel blue")
	lhu_amt = Entry(top_lhu, width = 50, borderwidth = 1)
	lhu_amt.config(state = 'disabled')
	lhu_amt_win = my_canvas.create_window(700, 350, window = lhu_amt)

	my_canvas.create_text(485, 400, text = "Collateral: ", font = ("Helvetica", 14), fill = "steel blue")
	lhu_coll = Entry(top_lhu, width = 50, borderwidth = 1)
	lhu_coll.config(state = 'disabled')
	lhu_coll_win = my_canvas.create_window(700, 400, window = lhu_coll)

	my_canvas.create_text(485, 450, text = "Investor: ", font = ("Helvetica", 14), fill = "steel blue")
	lhu_inv = Entry(top_lhu, width = 50, borderwidth = 1)
	lhu_inv.config(state = 'disabled')
	lhu_inv_win = my_canvas.create_window(700, 450, window = lhu_inv)

	my_canvas.create_text(478, 500, text = "Status: ", font = ("Helvetica", 14), fill = "steel blue")
	lhu_st = Entry(top_lhu, width = 50, borderwidth = 1)
	lhu_st.config(state = 'disabled')
	lhu_st_win = my_canvas.create_window(700, 500, window = lhu_st)

	my_canvas.create_text(485, 550, text = "Loan ID: ", font = ("Helvetica", 14), fill = "steel blue")
	lhu_lid = Entry(top_lhu, width = 50, borderwidth = 1)
	lhu_lid.config(state = 'disabled')
	lhu_lid_win = my_canvas.create_window(700, 550, window = lhu_lid)

	back_button = Button(top_lhu, text = "Back", command = top_lhu.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	back_button_win = my_canvas.create_window(650, 600, window = back_button)

	top_lhu.grab_set()

	#After installing backend
