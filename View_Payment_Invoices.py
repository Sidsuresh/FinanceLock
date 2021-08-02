from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox
import pyrebase

def view_invoices(Uid):

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
		chkind = records.index(click_bill.get())
		invid = inv_id[chkind]
		inv = db.child('Invoices').child(invid).get()

		vpi_lid.configure(state = 'normal')
		vpi_amt.configure(state = 'normal')
		vpi_bal.configure(state = 'normal')
		vpi_date.configure(state = 'normal')

		vpi_lid.delete(0, END)
		vpi_amt.delete(0, END)
		vpi_bal.delete(0, END)
		vpi_date.delete(0, END)

		vpi_lid.insert(0, inv.val()['loan_id'])
		vpi_amt.insert(0, inv.val()['amnt'])
		vpi_bal.insert(0, inv.val()['balance'])
		vpi_date.insert(0, inv.val()['date'])

		vpi_lid.config(state = 'disabled')
		vpi_amt.config(state = 'disabled')
		vpi_bal.config(state = 'disabled')
		vpi_date.config(state = 'disabled')

	global bg_vpi

	top_vpi = Toplevel()
	top_vpi.title("View Payment Invoices")
	top_vpi.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_vpi.grab_set()

	bg_vpi = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_vpi, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_vpi, anchor = "nw")
	my_canvas.create_text(650, 125, text = "View Payment Invoices", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(400, 300, 860, 560, outline = "black", fill = "white")

	inv_id = []
	records = []

	try:
		inv = db.child('Invoices').get()
		for l in inv:
			print(l.val()['custId'])
			if l.val()['custId'] == Uid:
				inv_id.append(l.key())
				records.append(l.val()['loan_id'] + " - " +str(l.val()['inv_no']))
	except:
		pass

	print(records)
	my_canvas.create_text(432, 250, text = "Choose LoanID and Invoice Number: ", font = ("Helvetica", 14), fill = "steel blue")
	click_bill = StringVar()
	e_bill = OptionMenu(top_vpi, click_bill, *records)
	e_bill_win = my_canvas.create_window(700, 250, window = e_bill)

	sub_button = Button(top_vpi, text = "Submit", command = submit, background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_button_win = my_canvas.create_window(885, 250, window = sub_button)

	my_canvas.create_text(452, 350, text = "Loan ID: ", font = ("Helvetica", 14), fill = "steel blue")
	vpi_lid = Entry(top_vpi, width = 50, borderwidth = 1, state = 'disabled')
	vpi_lid_win = my_canvas.create_window(700, 350, window = vpi_lid)

	my_canvas.create_text(472, 400, text = "Amount Paid: ", font = ("Helvetica", 14), fill = "steel blue")
	vpi_amt = Entry(top_vpi, width = 50, borderwidth = 1, state = 'disabled')
	vpi_amt_win = my_canvas.create_window(700, 400, window = vpi_amt)

	my_canvas.create_text(453, 450, text = "Balance: ", font = ("Helvetica", 14), fill = "steel blue")
	vpi_bal = Entry(top_vpi, width = 50, borderwidth = 1, state = 'disabled')
	vpi_bal_win = my_canvas.create_window(700, 450, window = vpi_bal)

	my_canvas.create_text(439, 500, text = "Date: ", font = ("Helvetica", 14), fill = "steel blue")
	vpi_date = Entry(top_vpi, width = 50, borderwidth = 1, state = 'disabled')
	vpi_date_win = my_canvas.create_window(700, 500, window = vpi_date)

	goback_button = Button (top_vpi, text = "Back", command = top_vpi.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(650, 540, window = goback_button)
