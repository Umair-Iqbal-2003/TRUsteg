from tkinter import *
from tkinter import filedialog 
import tkinter as tk 
from PIL import Image, ImageTk 
import os
from stegano import lsb #pip install stegano
from ttkthemes import ThemedTk 

root = ThemedTk(theme="arc")
root.title("Steganography - Hide a Secret Text Message in an Image") 
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

# Function to display image
def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG File", "*.jpg"),
                                                     ("All file", "*.txt")))
    if filename:
        # Open the image file
        img = Image.open(filename)

        # Set the size for the thumbnail
        max_width, max_height = 340, 280
        thumbnail_size = calculate_thumbnail_size(img, max_width, max_height)

        # Resize the image thumbnail to fit inside the box
        img.thumbnail(thumbnail_size)

        # Create a Tkinter-compatible photo image
        img = ImageTk.PhotoImage(img)

        # Configure the label to display the resized image
        lbl.configure(image=img, width=max_width, height=max_height)
        lbl.image = img

# Thumbnail Size Calculation
# Calculate thumbnail size while preserving aspect ratio
def calculate_thumbnail_size(image, max_width, max_height):
    width, height = image.size
    aspect_ratio = width / height

    if width > max_width or height > max_height:
        if aspect_ratio > 1:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
    else:
        new_width, new_height = width, height

    return new_width, new_height

# Function to hide secret data in the image
def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

# Function to reveal hidden data in the image
def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END) 
    text1.insert(END, clear_message)
    
# Function to save the modified image
def save():
    # Check if the secret variable is defined
    if 'secret' in globals():
        # Ask the user to select the destination folder and file name
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                  filetypes=(("PNG file", "*.png"), ("All Files", "*.*")),
                                                  title="Save Image As",
                                                  initialfile="hidden.png")
        # Check if the user canceled the save operation
        if save_path:
            # Save the image with the specified file name and location
            secret.save(save_path)
            print("Image saved successfully as:", save_path)
    else:
        print("No secret data found.")

# Icon
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

# Logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# First Frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

# Label Configuration
# Configure label size to match the frame dimensions
lbl = Label(f, bg="black", width=340, height=280)
lbl.place(x=40, y=10)

# Second Frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)

Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Fourth Frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
