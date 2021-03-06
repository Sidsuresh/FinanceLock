from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox
import pyrebase

def search_name_inves(Uid):

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
		name = sni_name.get()
		try:
			record = []
			custID = db.child("CustandInv").get()
			for l in custID:
				if l.val()['uniqueInvid'] == Uid:
					record.append(l.val()['uniqueCid'])
		except:
			pass

		print(record)

		i = 0
		if not record:
			messagebox.showerror("Error", "No customers available")
		else:
			cust = db.child("People").child("Customer").get()
			for c in cust:
				if c.key() in record and c.val()['name'] == name:
					customer = c.val()
					i = 1
					break

		if i == 1:

			vr_name.configure(state = 'normal')
			vr_dob.configure(state = 'normal')
			vr_gen.configure(state = 'normal')
			vr_pid.configure(state = 'normal')
			vr_email.configure(state = 'normal')
			vr_pno.configure(state = 'normal')
			vr_pradd.configure(state = 'normal')
			vr_peadd.configure(state = 'normal')
			vr_emp.configure(state = 'normal')
			vr_ocp.configure(state = 'normal')

			vr_name.delete(0, END)
			vr_dob.delete(0, END)
			vr_gen.delete(0, END)
			vr_pid.delete(0, END)
			vr_email.delete(0, END)
			vr_pno.delete(0, END)
			vr_pradd.delete(0, END)
			vr_peadd.delete(0, END)
			vr_emp.delete(0, END)
			vr_ocp.delete(0, END)

			vr_name.insert(0, customer['name'])
			vr_dob.insert(0, customer['dob'])
			vr_gen.insert(0, customer['gender'])
			vr_pid.insert(0, customer['proof_id'])
			vr_email.insert(0, customer['email'])
			vr_pno.insert(0, customer['phone_no'])
			vr_pradd.insert(0, customer['present_address'])
			vr_peadd.insert(0, customer['permanent_address'])
			vr_emp.insert(0, customer['employed'])
			vr_ocp.insert(0, customer['occupation'])

			vr_name.config(state = 'disabled')
			vr_dob.config(state = 'disabled')
			vr_gen.config(state = 'disabled')
			vr_pid.config(state = 'disabled')
			vr_email.config(state = 'disabled')
			vr_pno.config(state = 'disabled')
			vr_pradd.config(state = 'disabled')
			vr_peadd.config(state = 'disabled')
			vr_emp.config(state = 'disabled')
			vr_ocp.config(state = 'disabled')


	global bg_sni

	top_sni = Toplevel()
	top_sni.title("Search Customers by Name")
	top_sni.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_sni.grab_set()

	bg_sni = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_sni, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_sni, anchor = "nw")
	my_canvas.create_text(635, 125, text = "Search Customers by Name", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(470, 200, text = "Enter the name: ", font = ("Helvetica", 15), fill = "steel blue")
	sni_name = Entry(top_sni, width = 50, borderwidth = 1)
	sni_name_win = my_canvas.create_window(705, 200, window = sni_name)

	sub_but = Button (top_sni, text = "Submit", command = submit, background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_but_win = my_canvas.create_window(900, 200, window = sub_but)

	my_canvas.create_rectangle(75, 250, 1200, 580, outline = "black", fill = "white", tag = "myrect")

	my_canvas.create_text(130, 300, text = "Name: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_name = Entry(top_sni, width = 50, borderwidth = 1)
	vr_name.config(state = 'disabled')
	vr_name_win = my_canvas.create_window(425, 300, window = vr_name)

	my_canvas.create_text(728, 300, text = "Date of Birth: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_dob = Entry(top_sni, width = 25, borderwidth = 1, state = 'disabled')
	vr_dob_win = my_canvas.create_window(930, 300, window = vr_dob)

	my_canvas.create_text(137, 350, text = "Gender: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_gen = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_gen_win = my_canvas.create_window(425, 350, window = vr_gen)

	my_canvas.create_text(712, 350, text = "ID Proof: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_pid = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_pid_win = my_canvas.create_window(1005, 350, window = vr_pid)

	my_canvas.create_text(130, 400, text = "Email: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_email = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_email_win = my_canvas.create_window(425, 400, window = vr_email)

	my_canvas.create_text(740, 400, text = "Phone Number: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_pno = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_pno_win = my_canvas.create_window(1005, 400, window = vr_pno)

	my_canvas.create_text(175, 450, text = "Present Address: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_pradd = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_pradd_win = my_canvas.create_window(425, 450, window = vr_pradd)

	my_canvas.create_text(760, 450, text = "Permanent Address: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_peadd = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_peadd_win = my_canvas.create_window(1005, 450, window = vr_peadd)

	my_canvas.create_text(148, 500, text = "Employed: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_emp = Entry(top_sni, width = 25, borderwidth = 1, state = 'disabled')
	vr_emp_win = my_canvas.create_window(350, 500, window = vr_emp)

	my_canvas.create_text(725, 500, text = "Occupation: ", font = ("Helvetica", 14), fill = "steel blue")
	vr_ocp = Entry(top_sni, width = 50, borderwidth = 1, state = 'disabled')
	vr_ocp_win = my_canvas.create_window(1005, 500, window = vr_ocp)

	clr_but = Button (top_sni, text = "Back", command = top_sni.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	clr_but_win = my_canvas.create_window(625, 550, window = clr_but)



	

