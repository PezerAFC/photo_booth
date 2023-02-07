import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk

# Create a window
root = tk.Tk()
root.title("Take a Picture")

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Open the camera
cap = cv2.VideoCapture(0)

# Function to take a picture
def take_picture():
    ret, frame = cap.read()
    cv2.imwrite("image.jpg", frame)
    image = PIL.Image.open("image.jpg")
    image = image.resize((640, 480), PIL.Image.ANTIALIAS)
    photo = PIL.ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

# Create a button to take a picture
button = tk.Button(root, text="Take Picture", command=take_picture)
button.pack()

# Start the GUI event loop
root.mainloop()

# Release the camera
cap.release()
