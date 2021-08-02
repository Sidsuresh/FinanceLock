from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox
import pyrebase
import os
import subprocess

def view_req(Uid):

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
	storage = firebase.storage()

	def submit():
		chkind = requests.index(click_gen.get())
		cusCid = cust[chkind]
		date = dates[chkind]
		ltype = ltypes[chkind]
		people = db.child("People").child("Customer").get()
		loans_req = db.child("Loan").child("Request").get() 

		for p in people:
			if p.key() == cusCid:
				customer = p.val()

		for l in loans_req:
			print(l)
			print(l.val()['date'])
			print(date)
			print(l.val()['type'])
			print(ltype)
			print(l.val()['uniqueIid'])
			print(Uid)
			print(l.val()['uniqueCid'])
			print(cusCid)
			if (l.val()['date'] == date and l.val()['type'] == ltype and l.val()['uniqueIid'] == Uid and l.val()['uniqueCid'] == cusCid):
				custloan = l.val()

		vr_name.configure(state = 'normal')
		vr_age.configure(state = 'normal')
		vr_ltype.configure(state = 'normal')
		vr_amt.configure(state = 'normal')
		vr_sal.configure(state = 'normal')
		vr_coll.configure(state = 'normal')
		vr_emp.configure(state = 'normal')
		vr_ocp.configure(state = 'normal')
		vr_ld.configure(state = 'normal')
		vr_tp.configure(state = 'normal')

		vr_name.delete(0, END)
		vr_age.delete(0, END)
		vr_ltype.delete(0, END)
		vr_amt.delete(0, END)
		vr_sal.delete(0, END)
		vr_coll.delete(0, END)
		vr_emp.delete(0, END)
		vr_ocp.delete(0, END)
		vr_ld.delete(0, END)
		vr_tp.delete(0, END)

		vr_name.insert(0, customer['name'])
		vr_age.insert(0, customer['dob'])
		vr_ltype.insert(0, custloan['type'])
		vr_amt.insert(0, custloan['amt'])
		vr_sal.insert(0, customer['salary'])
		vr_coll.insert(0, custloan['collateral'])
		vr_emp.insert(0, customer['employed'])
		vr_ocp.insert(0, customer['occupation'])
		vr_ld.insert(0, custloan['loan_dur'])
		vr_tp.insert(0, custloan['timeper'])

		vr_name.config(state = 'disabled')
		vr_age.config(state = 'disabled')
		vr_ltype.config(state = 'disabled')
		vr_amt.config(state = 'disabled')
		vr_sal.config(state = 'disabled')
		vr_coll.config(state = 'disabled')
		vr_emp.config(state = 'disabled')
		vr_ocp.config(state = 'disabled')
		vr_ld.config(state = 'disabled')
		vr_tp.config(state = 'disabled')

	def accept():
		chkind = requests.index(click_gen.get())
		cusCid = cust[chkind]
		date = dates[chkind]
		ltype = ltypes[chkind]
		loans_req = db.child("Loan").child("Request").get()
		for l in loans_req:
			if (l.val()['date'] == date and l.val()['type'] == ltype and l.val()['uniqueIid'] == Uid and l.val()['uniqueCid'] == cusCid):
				custloan = l.val()
				loanId = l.key()

		db.child("Loan").child("Request").child(loanId).remove()
		custloan['status'] = "Accepted"
		db.child("Loan").child("Accept").push(custloan)
		messagebox.showinfo("Success", "The Loan Request has been Accepted")

		loans_acp = db.child("Loan").child("Accept").get()
		for l in loans_acp:
			if (l.val()['date'] == date and l.val()['type'] == ltype and l.val()['uniqueIid'] == Uid and l.val()['uniqueCid'] == cusCid):
				loanID = l.key()

		
		if ltype == 'Educational Loan':
			interest = 10.25
		elif ltype == 'Car loan':
			interest = 7.25
		elif ltype == 'Home Loan':
			interest = 6.85
		else:
			interest = 8.95

		prin_amt = float(l.val()['amt'])
		tp = float(l.val()['timeper'])

		if(l.val()['loan_dur'] == "Monthly"):
			interest /= 1200
			div = 12
		elif(l.val()['loan_dur'] == "Half Annual"):
			interest /= 200
			div = 2
		else:
			interest /= 100
			div = 1
		
		amount = (prin_amt * interest * pow(1 + interest, tp) / (pow(1 + interest, tp) - 1)) * tp
		payment = amount/(tp*div)
		bal = db.child('People').child('Investor').child(Uid).get()
		bal_amt = bal.val()['invest_balance']
		bal_amt = bal_amt - float(l.val()['amt'])
		db.child('People').child('Investor').child(Uid).update({'invest_balance': bal_amt})
		data_up = {'loan_id': loanID, 'amnt': amount, 'payment': payment, 'invoice': 1}
		db.child("Accounts").push(data_up)
		os.remove("C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/Download/" + cusCid + ".pdf")

	def reject():
		chkind = requests.index(click_gen.get())
		cusCid = cust[chkind]
		date = dates[chkind]
		ltype = ltypes[chkind]
		loans_req = db.child("Loan").child("Request").get()
		for l in loans_req:
			if (l.val()['date'] == date and l.val()['type'] == ltype and l.val()['uniqueIid'] == Uid and l.val()['uniqueCid'] == cusCid):
				custloan = l.val()
				loanId = l.key()

		db.child("Loan").child("Request").child(loanId).remove()
		custloan['status'] = "Rejected"
		db.child("Loan").child("Reject").push(custloan)
		messagebox.showinfo("Success", "The Loan Request has been Rejected")
		os.remove("C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/Download/" + cusCid + ".pdf")

	def chk():
		chkind = requests.index(click_gen.get())
		cusCid = cust[chkind]
		filename = "SalaryCert/" + cusCid + ".pdf"
		print(filename)
		storage.child(filename).download("C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/Download/", cusCid + ".pdf")
		os.rename("C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/" + cusCid + ".pdf", "C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/Download/" + cusCid + ".pdf")
		file = "C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/Download/" + cusCid + ".pdf"
		subprocess.Popen([file],shell=True)

	global bg_vd

	top_vd = Toplevel()
	top_vd.title("View Loan Requests")
	top_vd.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_vd = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_vd, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_vd, anchor = "nw")
	my_canvas.create_text(635, 125, text = "View Loan Requests", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(75, 250, 1200, 580, outline = "black", fill = "white")

	my_canvas.create_text(550, 225, text = "Loan ID: ", font = ("Helvetica", 14), fill = "steel blue")

	requests = []
	cust = []
	dates = []
	ltypes = []
	click_gen = StringVar()

	try:

		record = db.child("Loan").child("Request").get()
		
		for r in record.each():
			if r.val()['uniqueIid'] == Uid:
				d = r.val()['date']
				t = r.val()['type']
				requests.append(d+ " - " +t)
				dates.append(d)
				ltypes.append(t)
				cust.append(r.val()['uniqueCid'])
		click_gen.set(requests[0])
		e_gen = OptionMenu(top_vd, click_gen, *requests)
		e_gen_win = my_canvas.create_window(700, 225, window = e_gen)
		print(cust)

	except:
		messagebox.showinfo("Empty", "No Loan Requests Pending")
		top_vd.destroy()

	sub_button = Button(top_vd, text = "Submit", command = submit, background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_button_win = my_canvas.create_window(820, 225, window = sub_button)

	my_canvas.create_text(125, 300, text = "Name: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_name = Entry(top_vd, width = 50, borderwidth = 1)
	vr_name.config(state = 'disabled')
	vr_name_win = my_canvas.create_window(375, 300, window = vr_name)

	my_canvas.create_text(800, 300, text = "Date of Birth: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_age = Entry(top_vd, width = 25, borderwidth = 1, state = 'disabled')
	vr_age_win = my_canvas.create_window(930, 300, window = vr_age)

	my_canvas.create_text(145, 350, text = "Loan Type: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_ltype = Entry(top_vd, width = 50, borderwidth = 1, state = 'disabled')
	vr_ltype_win = my_canvas.create_window(375, 350, window = vr_ltype)

	my_canvas.create_text(785, 350, text = "Amount: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_amt = Entry(top_vd, width = 50, borderwidth = 1, state = 'disabled')
	vr_amt_win = my_canvas.create_window(1005, 350, window = vr_amt)

	my_canvas.create_text(123, 400, text = "Salary: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_sal = Entry(top_vd, width = 50, borderwidth = 1, state = 'disabled')
	vr_sal_win = my_canvas.create_window(375, 400, window = vr_sal)
	chk_button = Button(top_vd, text = "Check", command = chk,background = "white", highlightbackground = "black", highlightthickness = 2)
	chk_button_win = my_canvas.create_window(575, 400, window = chk_button)

	my_canvas.create_text(790, 400, text = "Collateral: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_coll = Entry(top_vd, width = 50, borderwidth = 1, state = 'disabled')
	vr_coll_win = my_canvas.create_window(1005, 400, window = vr_coll)

	my_canvas.create_text(140, 450, text = "Employed: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_emp = Entry(top_vd, width = 25, borderwidth = 1, state = 'disabled')
	vr_emp_win = my_canvas.create_window(300, 450, window = vr_emp)

	my_canvas.create_text(800, 450, text = "Occupation: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_ocp = Entry(top_vd, width = 50, borderwidth = 1, state = 'disabled')
	vr_ocp_win = my_canvas.create_window(1005, 450, window = vr_ocp)

	my_canvas.create_text(155, 500, text = "Loan Duration: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_ld = Entry(top_vd, width = 25, borderwidth = 1, state = 'disabled')
	vr_ld_win = my_canvas.create_window(300, 500, window = vr_ld)

	my_canvas.create_text(800, 500, text = "Timeperiod: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_tp = Entry(top_vd, width = 50, borderwidth = 1, state = 'disabled')
	vr_tp_win = my_canvas.create_window(1005, 500, window = vr_tp)

	accept_button = Button(top_vd, text = "Accept", command = accept, background = "white", highlightbackground = "black", highlightthickness = 2)
	accept_button_win = my_canvas.create_window(750, 550, window = accept_button)

	reject_button = Button(top_vd, text = "Reject", command = reject, background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	reject_button_win = my_canvas.create_window(625, 550, window = reject_button)

	goback_button = Button(top_vd, text = "Go back", command = top_vd.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	goback_button_win = my_canvas.create_window(500, 550, window = goback_button)

	top_vd.grab_set()