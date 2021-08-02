from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from Search_Name_Inves import *
from Click_Name_Inves import *

def view_cust_det(Uid):

	def choose():

		if r_ch1.get() == 1 and r_ch2.get() == 0:
			my_canvas.delete("only_one")
			my_canvas.delete("atleast_one")
			search_name_inves(Uid)
		elif r_ch1.get() == 0 and r_ch2.get() == 1:
			my_canvas.delete("only_one")
			my_canvas.delete("atleast_one")
			click_name_inves(Uid)
		elif r_ch1.get() == 0 and r_ch2.get() == 0:
			my_canvas.delete("only_one")
			my_canvas.create_text(300, 300, text = "Choose 'Atleast One' Account Type", font = ("Helvetica", 15), fill = "steel blue", tag = "atleast_one")
		else:
			my_canvas.delete("atleast_one")
			my_canvas.create_text(300, 300, text = "Choose 'Only One' Account Type", font = ("Helvetica", 15), fill = "steel blue", tag = "only_one")

	global bg_vcd

	top_vcd = Toplevel()
	top_vcd.title("Customer Details")
	top_vcd.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	#top_ca.attributes('-topmost', 'true')

	bg_vcd = ImageTk.PhotoImage(Image.open("BG/bg3.jpeg"))
	my_canvas = Canvas(top_vcd, width = 600, height = 410)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_vcd, anchor = "nw")
	my_canvas.create_text(300, 100, text = "View Customer Details", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	r_ch1 = IntVar()
	r_ch2 = IntVar()

	c1 = Checkbutton(top_vcd, text = "Search Customer by Name", variable = r_ch1)
	c1_win = my_canvas.create_window(300, 175, window = c1)
	c2 = Checkbutton(top_vcd, text = "Search Customer from List", variable = r_ch2)
	c2_win = my_canvas.create_window(300, 215, window = c2)

	next_button = Button (top_vcd, text = "Next", command = choose, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(400, 250, window = next_button)

	goback_button = Button (top_vcd, text = "Back", command = top_vcd.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(200, 250, window = goback_button)

	top_vcd.grab_set()
