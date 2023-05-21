import tkinter as tk
from PIL import Image, ImageTk

# Slide data
slides = [
    {
        "title": "Introduction",
        "content": "hello",
        "image": "slide1.jpg",
    },
    {
        "title": "Slide 1",
        "content": "This is Slide 1 content.",
        "image": "slide2.jpg",
    },
    {
        "title": "Slide 2",
        "content": "This is Slide 2 content.",
        "image": "slide3.jpg",
    },
    {
        "title": "Slide 3",
        "content": "This is Slide 3 content.",
        "image": "slide4.jpg",
    },
    {
        "title": "Conclusion",
        "content": "Thank you for attending!",
        "image": "slide5.jpg",
    }
]

window = tk.Tk()

window.title("Smart Assistant")

window.geometry("800x600")

title_label = tk.Label(window, font=("Arial", 24, "bold"))
title_label.pack(pady=20)

content_label = tk.Label(window, font=("Arial", 18))
content_label.pack(pady=50)

image_label = tk.Label(window)
image_label.pack(pady=20)


def next_slide():
    current_slide = slides.index(current_slide_data)
    if current_slide < len(slides) - 1:
        show_slide(current_slide + 1)


def previous_slide():
    current_slide = slides.index(current_slide_data)
    if current_slide > 0:
        show_slide(current_slide - 1)


def show_slide(slide_index):
    global current_slide_data
    current_slide_data = slides[slide_index]
    title_label.config(text=current_slide_data["title"])
    content_label.config(text=current_slide_data["content"])

    image_path = current_slide_data["image"]
    image = Image.open("C:\\Users\\Mhsn\\Documents\\DesktopAssistant\\ppt.jpg")
    image = image.resize((400, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo

    window.configure(background=photo)


next_button = tk.Button(window, text="Next", command=next_slide)
next_button.pack(side=tk.RIGHT, padx=10)

previous_button = tk.Button(window, text="Previous", command=previous_slide)
previous_button.pack(side=tk.LEFT, padx=10)

show_slide(0)

window.mainloop()
