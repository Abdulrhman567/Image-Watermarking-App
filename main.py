from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


# Creating The Image Watermarking App
class ImageWatermarking:
    def __init__(self):
        self.resized_img = None
        self.updated_img = None
        self.main_window = Tk()
        self.main_window.title("Image Watermarking")
        self.main_window.config(pady=20)

        # CANVAS
        self.canvas = Canvas(self.main_window, width=750, height=500, bg="#dee2e6",
                             highlightthickness=2, highlightbackground="#525E75")
        self.canvas.grid(row=1, column=0, columnspan=3, pady=20)

        # BUTTONS
        self.select_image_button = Button(self.main_window, text="select Image", width=17,
                                          bg="#6BCB77", fg="#fff",
                                          font=("bold", 12), highlightthickness=1,
                                          bd=0, command=self.select_image)
        self.select_image_button.grid(row=0, column=0, columnspan=3)

        self.add_text_button = Button(self.main_window, text="Add Text", width=17,
                                      bg="#4D96FF", fg="#fff",
                                      font=("bold", 12), highlightthickness=0,
                                      bd=0, state=DISABLED, command=self.add_text)
        self.add_text_button.grid(row=2, column=0)

        self.add_logo_button = Button(self.main_window, text="Add Logo", width=17,
                                      bg="#4D96FF", fg="#fff",
                                      font=("bold", 12), highlightthickness=0,
                                      bd=0, state=DISABLED, command=self.add_logo)
        self.add_logo_button.grid(row=2, column=1)

        self.submit_button = Button(self.main_window, text="Submit", width=17,
                                    bg="#6BCB77", fg="#fff",
                                    font=("bold", 12), highlightthickness=0,
                                    bd=0, state=DISABLED, command=self.submit_image)
        self.submit_button.grid(row=2, column=2)

        self.main_window.mainloop()

    def select_image(self):
        """
        It gives you the ability to choose an image from your system files and resize it and display it on the canvas.
        """
        img_name = filedialog.askopenfilename(title="Select an image",
                                              filetypes=(("jpg images", "*.jpg*"), ("png images", "*.png*")))
        if img_name:
            with Image.open(img_name) as img:
                self.resized_img = img.resize((750, 500))
                self.resized_img.show()

            self.photo_img = ImageTk.PhotoImage(self.resized_img)
            self.canvas_img = self.canvas.create_image(375, 250, image=self.photo_img)

            self.add_text_button.config(state=NORMAL)
            self.add_logo_button.config(state=NORMAL)
            self.submit_button.config(state=NORMAL)

    def add_text(self):
        """
        Displays the 'Text' window to enter some text you want to display on the main image and choose a font type and
        a font size to the text.
        """
        # The Text Window
        text_window = Tk()
        text_window.title("Add Text")
        text_window.config(bg="#fff")
        text_window.config(padx=40, pady=30)

        # Labels, buttons, entries, font scale and font type list box for the text window
        text_label = Label(text_window, text="Enter Text:", bg="#fff")
        text_label.pack(anchor=NW)

        self.text_entry = Entry(text_window, width=43, highlightthickness=2)
        self.text_entry.focus()
        self.text_entry.pack(anchor=NW, pady=8)

        font_label = Label(text_window, text="Fonts:", bg="#fff")
        font_label.pack(anchor=NW)

        self.scale_font = Scale(text_window, activebackground="#adb5bd", bg="#fff", highlightbackground="#fff",
                           troughcolor="#868e96", bd=0, from_=12, to=64, orient=HORIZONTAL, length=260)
        self.scale_font.pack(anchor=NW)

        font_type_label = Label(text_window, text="Font Type:", bg="#fff")
        font_type_label.pack(anchor=NW)

        # These fonts need to be installed on your device first if they are already installed try to change
        # the path of the font inside the 'insert' method
        self.font_type_listbox = Listbox(text_window, width=40, height=4, selectmode=SINGLE)
        self.font_type_listbox.pack(anchor=NW)
        self.font_type_listbox.insert(1, "Arabtype.ttf")
        self.font_type_listbox.insert(2, "Arial.ttf")
        self.font_type_listbox.insert(3, "Calibril.ttf")
        self.font_type_listbox.insert(4, "Comic.ttf")
        self.font_type_listbox.insert(5, "Framd.ttf")

        text_submit_button = Button(text_window, text="Submit Text", bg="#6BCB77", fg="#fff",
                                    highlightthickness=0, bd=0, width=14, font=("bold", 12),
                                    command=self.submit_text)
        text_submit_button.pack(anchor=NW, pady=20)

        text_window.mainloop()

    def submit_text(self):
        """
        displays the text entered on the image and puts it on the canvas
        """
        text = self.text_entry.get()
        text_size = self.scale_font.get()
        text_font_type = self.font_type_listbox.get(first=self.font_type_listbox.curselection()[0], last=None)
        text_font = ImageFont.truetype(text_font_type, text_size)

        text_on_img = ImageDraw.Draw(self.resized_img)
        text_on_img.text((375, 250), text=text, font=text_font, fill="#fff")
        self.updated_img = ImageTk.PhotoImage(self.resized_img)
        self.canvas.itemconfig(self.canvas_img, image=self.updated_img)

    def add_logo(self):
        """
        Display the 'Adjust Logo' window to choose where the entered logo should be placed on the main image using
        the x-axis and the y-axis.
        """
        # The Logo Window
        logo_window = Tk()
        logo_window.title("Adjust Logo")
        logo_window.config(padx=25, pady=25, bg="#fff")

        x_axis_label = Label(logo_window, text="X-AXIS", bg="#fff")
        x_axis_label.pack(anchor=NW)

        self.x_axis_scale = Scale(logo_window, activebackground="#F24A72", highlightbackground="#fff", bg="#fff",
                                  troughcolor="#F24A72",bd=0, from_=0, to=685, orient=HORIZONTAL, length=260)
        self.x_axis_scale.pack(anchor=NW, pady=5)

        y_axis_label = Label(logo_window, text="Y-AXIS", bg="#fff")
        y_axis_label.pack(anchor=NW)

        self.y_axix_scale = Scale(logo_window, activebackground="#4D96FF", highlightbackground="#fff", bg="#fff",
                                  troughcolor="#4D96FF", bd=0, from_=0, to=435, orient=HORIZONTAL, length=260)
        self.y_axix_scale.pack(anchor=NW, pady=5)

        add_logo_submit_button = Button(logo_window, text="Get logo", width=13,
                                        fg="#fff", bg="#6BCB77", bd=0,
                                        highlightthickness=0, font=("bold", 12), command=self.submit_logo)
        add_logo_submit_button.pack(anchor=NW, pady=14)

        logo_window.mainloop()

    def submit_logo(self):
        """
        Chooses the logo to be displayed where the user chose to be placed on the main image and display the main image
        on the canvas.
        """
        x_axis_point = self.x_axis_scale.get()
        y_axis_point = self.y_axix_scale.get()
        logo_name = filedialog.askopenfilename(title="Select a Logo",
                                               filetypes=(("jpg images", "*.jpg*"), ("png images", "*.png*")))
        if logo_name:
            with Image.open(logo_name) as logo_img:
                resized_logo_img = logo_img.resize((60, 60))
                self.resized_img.paste(resized_logo_img, (x_axis_point, y_axis_point))
                self.resized_img.show()
            final_img = ImageTk.PhotoImage(self.resized_img)
            self.canvas.itemconfig(self.canvas_img, image=final_img)

    def submit_image(self):
        """
        Saves the new image on the system files and clears the canvas.
        """
        self.resized_img.save("new_image.jpg")
        self.canvas.delete("all")


if __name__ == "__main__":
    app = ImageWatermarking()
