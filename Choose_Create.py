from tkinter import *
from CAA_User import *
from CAA_Inves import *
from PIL import ImageTk, Image

def chk_caa():

	global bg_ch

	def choose():

		if r_ch1.get() == 1 and r_ch2.get() == 0:
			open_caa_user()
			#top_ch.destroy()
		elif r_ch1.get() == 0 and r_ch2.get() == 1:
			open_caa_inves()
			#top_ch.destroy()
		elif r_ch1.get() == 0 and r_ch2.get() == 0:
			my_canvas.delete("only_one")
			my_canvas.create_text(300, 300, text = "Choose 'Atleast One' Account Type", font = ("Helvetica", 15), fill = "steel blue", tag = "atleast_one")
		else:
			my_canvas.delete("atleast_one")
			my_canvas.create_text(300, 300, text = "Choose 'Only One' Account Type", font = ("Helvetica", 15), fill = "steel blue", tag = "only_one")
			

	top_ch = Toplevel()
	top_ch.title("Choose Account Type")
	top_ch.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_ch = ImageTk.PhotoImage(Image.open("BG/bg3.jpeg"))
	my_canvas = Canvas(top_ch, width = 600, height = 410)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_ch, anchor = "nw")
	my_canvas.create_text(300, 100, text = "Choose the Account Type", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	r_ch1 = IntVar()
	r_ch2 = IntVar()

	c1 = Checkbutton(top_ch, text = "Customer", variable = r_ch1)
	c1_win = my_canvas.create_window(300, 175, window = c1)
	c2 = Checkbutton(top_ch, text = "Investors", variable = r_ch2)
	c2_win = my_canvas.create_window(298, 215, window = c2)

	next_button = Button (top_ch, text = "Next", command = choose, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(400, 250, window = next_button)

	goback_button = Button (top_ch, text = "Back", command = top_ch.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)
	goback_button_win = my_canvas.create_window(200, 250, window = goback_button)
