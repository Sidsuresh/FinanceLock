from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from User_Pass_Inves import *
from validate_email import validate_email
import pyrebase


def open_caa_inves():

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

	def next_but():

		chk_cnt = 1
		chk_list = []

		if len(e_fname.get()) == 0 or e_fname.get() == "Entry should be filled":
			e_fname.delete(0, END)
			e_fname.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_lname.get()) == 0 or e_lname.get() == "Entry should be filled":
			e_lname.delete(0, END)
			e_lname.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_dob.get()) == 0 or e_dob.get() == "Entry should be filled":
			e_dob.delete(0, END)
			e_dob.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_doc.get()) == 0 or e_doc.get() == "Entry should be filled":
			e_doc.delete(0, END)
			e_doc.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_idate.get()) == 0 or (click_pid != "Aadhar Card" and e_idate.get() == "*") or e_idate.get() == "Entry should be filled":
			e_idate.delete(0, END)
			e_idate.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_edate.get()) == 0 or (click_pid != "Aadhar Card" and e_edate.get() == "*") or e_edate.get() == "Entry should be filled":
			e_edate.delete(0, END)
			e_edate.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_email.get()) == 0:
			e_email.delete(0, END)
			e_email.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_pno.get()) == 0 or e_pno.get() == "Entry should be filled":
			e_pno.delete(0, END)
			e_pno.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_sal.get()) == 0 or e_sal.get() == "Entry should be filled":
			e_sal.delete(0, END)
			e_sal.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_salc.get()) == 0 or e_salc.get() == "Entry should be filled":
			e_salc.delete(0, END)
			e_salc.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_peadd.get()) == 0 or e_peadd.get() == "Entry should be filled":
			e_peadd.delete(0, END)
			e_peadd.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_pepb.get()) == 0 or e_pepb.get() == "Entry should be filled":
			e_pepb.delete(0, END)
			e_pepb.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_pest.get()) == 0 or e_pest.get() == "Entry should be filled":
			e_pest.delete(0, END)
			e_pest.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_pecnt.get()) == 0 or e_pecnt.get() == "Entry should be filled":
			e_pecnt.delete(0, END)
			e_pecnt.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_pradd.get()) == 0 or e_pradd.get() == "Entry should be filled":
			e_pradd.delete(0, END)
			e_pradd.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_prpb.get()) == 0 or e_prpb.get() == "Entry should be filled":
			e_prpb.delete(0, END)
			e_prpb.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_prst.get()) == 0 or e_prst.get() == "Entry should be filled":
			e_prst.delete(0, END)
			e_prst.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		if len(e_prcnt.get()) == 0 or e_prcnt.get() == "Entry should be filled":
			e_prcnt.delete(0, END)
			e_prcnt.insert(0, "Entry should be filled")
			chk_list.append(0)
		else:
			chk_list.append(1)

		t1 = False
		if chk_list[6] == 1:
			t1 = validate_email(e_email.get())
		if not t1:
			e_email.delete(0, END)
			e_email.insert(0, "Enter valid e-mail id")

		for i in chk_list:
			if i == 0:
				chk_cnt = 0
				break

		if chk_cnt == 1 and t1:
			name = e_fname.get() + " " + e_lname.get()
			perm_add = e_peadd.get() + " " + e_pepb.get() + " " + e_pest.get() + " " + e_pecnt.get()
			pr_add = e_pradd.get() + " " + e_prpb.get() + " " + e_prst.get() + " " + e_prcnt.get()
			
			data_good = {'name': name,'dob': e_dob.get(), 'gender': click_gen.get(), 'proof_id': click_pid.get(), 'phone_no': e_pno.get(), 'employed': click_emp.get(), 'occupation': e_ocp.get(), 'doc_num': e_doc.get(), 'issue_date': e_idate.get(), 'expiry_date': e_edate.get(), 'email': e_email.get(), 'salary': e_sal.get(), 'salary_cert': e_salc.get(), 'permanent_address': perm_add, 'present_address': pr_add}
			db.child("People").child("Investor").push(data_good)	
			user_pass_inves(e_email.get())
			top_cain.destroy()

	def select():
		e_salc.delete(0, END)
		salc_open = filedialog.askopenfilename(initialdir = "C:/Users/sidsu/Desktop/V.I.T", title = "Select Salary Certificate", filetypes=[("PDF Files", "*.pdf")])
		e_salc.insert(0, salc_open)

	def clear():
		e_fname.delete(0, END)
		e_lname.delete(0, END)
		e_dob.delete(0, END)
		click_gen.set("Male")
		click_pid.set("Passport")
		e_doc.delete(0, END)
		e_idate.delete(0, END)
		e_edate.delete(0, END)
		e_email.delete(0, END)
		e_pno.delete(0, END)
		e_peadd.delete(0, END)
		e_pepb.delete(0, END)
		e_pest.delete(0, END)
		e_pecnt.delete(0, END)
		e_pradd.delete(0, END)
		e_prpb.delete(0, END)
		e_prst.delete(0, END)
		e_prcnt.delete(0, END)

	def sel():
		if click_emp.get() == "Yes":
			e_ocp.configure(state = "normal")
		else:
			e_ocp.config(state = "disabled")


	global bg_cain

	top_cain = Toplevel()
	top_cain.title("Create Your Account")
	top_cain.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_cain = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_cain, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_cain, anchor = "nw")
	my_canvas.create_text(635, 25, text = "Create Your Account", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(100, 75, text = "First Name: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_fname = Entry(top_cain, width = 50, borderwidth = 2)
	e_fname_win = my_canvas.create_window(325, 75, window = e_fname)

	my_canvas.create_text(750, 75, text = "Last Name: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_lname = Entry(top_cain, width = 50, borderwidth = 2)
	#e_lname.insert(0, "Last Name")
	e_lname_win = my_canvas.create_window(975, 75, window = e_lname)

	my_canvas.create_text(100, 125, text = "Date of Birth: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_dob = Entry(top_cain, width = 25, borderwidth = 2)
	#e_dob.insert(0, "Date of Birth")
	e_dob_win = my_canvas.create_window(250, 125, window = e_dob)

	my_canvas.create_text(750, 125, text = "Gender: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	click_gen = StringVar()
	click_gen.set("Male")
	e_gen = OptionMenu(top_cain, click_gen, "Male", "Female", "Others")
	e_gen_win = my_canvas.create_window(858, 125, window = e_gen)

	my_canvas.create_text(100, 175, text = "Proof of ID: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	click_pid = StringVar()
	click_pid.set("Passport")
	e_pid = OptionMenu(top_cain, click_pid, "Passport", "Aadhar Card", "PAN Card", "Driving License")
	e_pid_win = my_canvas.create_window(218, 175, window = e_pid)

	my_canvas.create_text(725, 175, text = "Document Number: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_doc = Entry(top_cain, width = 30, borderwidth = 2)
	#e_doc.insert(0, "Document Number")
	e_doc_win = my_canvas.create_window(915, 175, window = e_doc)

	my_canvas.create_text(100, 225, text = "Issue Date: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_idate = Entry(top_cain, width = 25, borderwidth = 2)
	e_idate.insert(0, "*")
	e_idate_win = my_canvas.create_window(250, 225, window = e_idate)
	my_canvas.create_text(284, 250, text = "*Not required if Proof of ID is Aadhar Card", font = ("Arial Rounded MT Bold", 8), fill = "steel blue")
	
	my_canvas.create_text(750, 225, text = "Expiry Date: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_edate = Entry(top_cain, width = 25, borderwidth = 2)
	e_edate.insert(0, "*")
	e_edate_win = my_canvas.create_window(900, 225, window = e_edate)
	my_canvas.create_text(934, 250, text = "*Not required if Proof of ID is Aadhar Card", font = ("Arial Rounded MT Bold", 8), fill = "steel blue")

	my_canvas.create_text(100, 275, text = "Email ID: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_email = Entry(top_cain, width = 50, borderwidth = 2)
	#e_email.insert(0, "Email")
	e_email_win = my_canvas.create_window(325, 275, window = e_email)
	
	my_canvas.create_text(750, 275, text = "Phone Number: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_pno = Entry(top_cain, width = 25, borderwidth = 2)
	#e_pno.insert(0, "Phone Number")
	e_pno_win = my_canvas.create_window(900, 275, window = e_pno)

	my_canvas.create_text(100, 325, text = "Employed: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	click_emp = StringVar()
	click_emp.set("Yes")
	e_emp = OptionMenu(top_cain, click_emp, "Yes", "No")
	e_emp_win = my_canvas.create_window(200, 325, window = e_emp)
	select_but = Button(top_cain, text = "Select", command = sel, background = "white", highlightbackground = "black", highlightthickness = 2)
	select_but_win = my_canvas.create_window(300, 325, window = select_but)

	my_canvas.create_text(750, 325, text = "Occupation: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue" )
	e_ocp = Entry(top_cain, width = 50, borderwidth = 2)
	e_ocp.insert(0, "Nil")
	e_ocp.config(state = "disabled")
	e_ocp_win = my_canvas.create_window(975, 325, window = e_ocp)

	my_canvas.create_text(100, 375, text = "Salary: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_sal = Entry(top_cain, width = 25, borderwidth = 2)
	#e_sal.insert(0, "Salary")
	e_sal_win = my_canvas.create_window(250, 375, window = e_sal)

	my_canvas.create_text(750, 375, text = "Salary Certificate: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_salc = Entry(top_cain, width = 50, borderwidth = 2)
	#e_salc.insert(0, "Salary Certificate")
	e_salc_win = my_canvas.create_window(975, 375, window = e_salc)
	salc_button = Button (top_cain, text = "Select", command = select, background = "white", highlightbackground = "black", highlightthickness = 2)
	salc_button_win = my_canvas.create_window(1165, 375, window = salc_button)
	top_cain.grab_set()

	my_canvas.create_text(250, 425, text = "Permanent Address ", font = ("Arial Rounded MT Bold", 15), fill = "steel blue")

	my_canvas.create_text(100, 475, text = "Address: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_peadd = Entry(top_cain, width = 50, borderwidth = 2)
	#e_peadd.insert(0, "Permanent Address")
	e_peadd_win = my_canvas.create_window(325, 475, window = e_peadd)

	my_canvas.create_text(100, 525, text = "P.O. BOX: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_pepb = Entry(top_cain, width = 25, borderwidth = 2)
	#e_pepb.insert(0, "P.O. Box")
	e_pepb_win = my_canvas.create_window(250, 525, window = e_pepb)

	my_canvas.create_text(100, 575, text = "State: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_pest = Entry(top_cain, width = 50, borderwidth = 2)
	#e_pest.insert(0, "State")
	e_pest_win = my_canvas.create_window(325, 575, window = e_pest)

	my_canvas.create_text(100, 625, text = "Country: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_pecnt = Entry(top_cain, width = 50, borderwidth = 2)
	#e_pecnt.insert(0, "Country")
	e_pecnt_win = my_canvas.create_window(325, 625, window = e_pecnt)

	my_canvas.create_text(850, 425, text = "Present Address ", font = ("Arial Rounded MT Bold", 15), fill = "steel blue")

	my_canvas.create_text(750, 475, text = "Address: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_pradd = Entry(top_cain, width = 50, borderwidth = 2)
	#e_pradd.insert(0, "Present Address")
	e_pradd_win = my_canvas.create_window(975, 475, window = e_pradd)

	my_canvas.create_text(750, 525, text = "P.O. BOX: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_prpb = Entry(top_cain, width = 25, borderwidth = 2)
	#e_prpb.insert(0, "P.O. Box")
	e_prpb_win = my_canvas.create_window(900, 525, window = e_prpb)

	my_canvas.create_text(750, 575, text = "State: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_prst = Entry(top_cain, width = 50, borderwidth = 2)
	#e_prst.insert(0, "State")
	e_prst_win = my_canvas.create_window(975, 575, window = e_prst)

	my_canvas.create_text(750, 625, text = "Country: ", font = ("Arial Rounded MT Bold", 12), fill = "steel blue")
	e_prcnt = Entry(top_cain, width = 50, borderwidth = 2)
	#e_prcnt.insert(0, "Country")
	e_prcnt_win = my_canvas.create_window(975, 625, window = e_prcnt)

	next_button = Button (top_cain, text = "Next", command = next_but, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(900, 675, window = next_button)

	goback_button = Button (top_cain, text = "Back", command = top_cain.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(300, 675, window = goback_button)

	res_button = Button (top_cain, text = "Reset Fields", command = clear, background = "white", highlightbackground = "black", highlightthickness = 2)
	res_button_win = my_canvas.create_window(600, 675, window = res_button)