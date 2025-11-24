import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from watermarker import WaterMarker

root = Tk()
REPEAT = tkinter.IntVar()

wm = WaterMarker()

# image
image_lbl = Label(root)
image_lbl.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

main_frm = Frame(root, padx=5, pady=5, bd=2)
main_frm.grid(column=0, row=1, columnspan=3, padx=10)

# text frame
under_img_frame = Frame(main_frm, relief='sunken', padx=5, pady=5, bd=2)
under_img_frame.grid(column=0, row=2, columnspan=2, sticky="ew", pady=5)

save_btn = Button(master=under_img_frame, text="Save Image As", command=lambda: wm.save_img())
save_btn.grid(column=1, row=0, padx=5, pady=5)

img_btn = Button(master=under_img_frame, text="Open image", command=lambda: wm.choose_img_from_explr(wm.img_label))
img_btn.grid(column=0, row=0, sticky="w", padx=5, pady=5)

mark_type_lbl = Label(under_img_frame, text="Mark Type:")
mark_type_lbl.grid(column=2, row=0, padx=5, pady=5, sticky="e")

under_img_frame.columnconfigure(2, weight=1)

mark_type_choice = Combobox(under_img_frame, values=("Text", "Image"), width=6)
mark_type_choice.set("Text")
mark_type_choice.grid(column=3, row=0, padx=5, pady=5, sticky="e")

# settings
text_frm = Frame(main_frm, relief='sunken', bd=2, padx=5)
text_frm.grid(column=0, row=3, sticky="nsew")

text_header_lbl = Label(text_frm, text="Text")
text_header_lbl.grid(column=0, row=0, sticky="nw", pady=3)

text_label = Label(text_frm, text="Enter text to add:")
text_label.grid(column=0, row=1)

text = Entry(master=text_frm)
text.grid(column=1, row=1)

font_size_lbl = Label(text_frm, text="Font Size (max 100):")
font_size_lbl.grid(column=0, row=2)

font_size = Spinbox(master=text_frm, from_=10, to=100, width=5)
font_size.grid(column=1, row=2, sticky="w")

img_header_lbl = Label(text_frm, text="Image")
img_header_lbl.grid(column=0, row=3, sticky="nw", pady=3)

mark_size_lbl = Label(master=text_frm, text="Image size (in %):")
mark_size_lbl.grid(column=0, row=4)

mark_size = Spinbox(master=text_frm, from_=10, to=100, width=5)
mark_size.grid(column=0, row=5, padx=10, pady=5)

img_mark_btn = Button(master=text_frm, text="Choose image for mark",
                      command=lambda: wm.choose_img_from_explr(wm.mark_preview,is_mark=True))
img_mark_btn.grid(column=0, row=6, padx=5, pady=5)

preview_header_lbl = Label(text_frm, text="Preview:")
preview_header_lbl.grid(column=1, row=3, sticky="nw", pady=3)

preview_lbl = Label(text_frm)
preview_lbl.grid(column=1, row=4, sticky="nw", rowspan=3, padx=20)

# repeat frame
settings_frm = Frame(main_frm, relief='sunken', bd=2, padx=5)
settings_frm.grid(column=1, row=3, sticky="nsew")

general_header_lbl = Label(settings_frm, text="General")
general_header_lbl.grid(column=0, row=0, sticky="nw", pady=3)

x_lbl = Label(settings_frm, text="X (max: {VALUE}):")
x_lbl.grid(column=0, row=1, pady=2)

mark_x = Spinbox(master=settings_frm, from_=0, to=wm.image.size[0], width=5)
mark_x.grid(column=1, row=1, pady=2)

y_lbl = Label(master=settings_frm, text="Y (max: {VALUE}):")
y_lbl.grid(column=0, row=2, pady=2)

mark_y = Spinbox(master=settings_frm, from_=0, to=wm.image.size[1], width=5)
mark_y.grid(column=1, row=2, pady=2)

opacity_lbl = Label(settings_frm, text=f"Opacity (in %):")
opacity_lbl.grid(column=2, row=1, pady=2)

opacity = Spinbox(master=settings_frm, from_=0, to=100, width=5)
opacity.grid(column=3, row=1, pady=2)

rotate_lbl = Label(settings_frm, text=f"Rotate (In degrees):")
rotate_lbl.grid(column=2, row=2, pady=2)

rotate = Spinbox(master=settings_frm, from_=0, to=360, width=5)
rotate.grid(column=3, row=2, pady=2)

other_header_lbl = Label(settings_frm, text="Other")
other_header_lbl.grid(column=0, row=3, sticky="nw", pady=3)

repeat = Checkbutton(master=settings_frm, text="Repeat", onvalue=1, offvalue=0, variable=REPEAT)
repeat.grid(column=0, row=4)

spacing_lbl = Label(settings_frm, text=f"Space between marks")
spacing_lbl.grid(column=0, row=5, columnspan=2)

spacing_x_lbl = Label(settings_frm, text=f"Spacing x:")
spacing_x_lbl.grid(column=0, row=6, pady=2)

spacing_x = Spinbox(master=settings_frm, from_=0, to=wm.image.size[0], width=5)
spacing_x.grid(column=1, row=6, pady=2)

spacing_y_lbl = Label(settings_frm, text=f"Spacing y:")
spacing_y_lbl.grid(column=2, row=6, pady=2)

spacing_y = Spinbox(master=settings_frm, from_=0, to=wm.image.size[1], width=5)
spacing_y.grid(column=3, row=6, pady=2)

offset_x_lbl = Label(settings_frm, text=f"Offset x:")
offset_x_lbl.grid(column=0, row=7, pady=2)

offset_x = Spinbox(master=settings_frm, from_=0, to=wm.image.size[0], width=5)
offset_x.grid(column=1, row=7, pady=2)

offset_y_lbl = Label(settings_frm, text=f"Offset y:")
offset_y_lbl.grid(column=2, row=7, pady=2)

offset_y = Spinbox(master=settings_frm, from_=0, to=wm.image.size[1], width=5)
offset_y.grid(column=3, row=7, pady=2)

# buttons
text_btn = Button(master=main_frm, text="Add mark",
                  command=wm.mark_image,
                  width=10)
text_btn.grid(column=1, sticky="ne", row=4, padx=10, pady=5)

inputs = {
    "mark_type": mark_type_choice,
    "text": text,
    "font_size": font_size,
    "mark_size": mark_size,
    "pos_x": mark_x,
    "pos_y": mark_y,
    "opacity": opacity,
    "rotation": rotate,
    "repeat": REPEAT,
    "spacing_x": spacing_x,
    "spacing_y": spacing_y,
    "offset_x": offset_x,
    "offset_y": offset_y,
}

dynamic_elements = {
    "spacing_lbl": {"x":{"object": x_lbl, "value": "X (max: {VALUE}):"},
                 "y": {"object": y_lbl, "value": "Y (max: {VALUE}):"},},
    "pos_lbl": {"x":{"object": spacing_x_lbl, "value": "X (max: {VALUE}):"},
                 "y": {"object": spacing_y_lbl, "value": "Y (max: {VALUE}):"},},
    "pos_input": {"x":{"object": spacing_x},
                  "y": {"object": spacing_y},},
    "spacing_input": {"x":{"object": spacing_x},
                      "y": {"object": spacing_y},},
    "offset_input": {"x":{"object": offset_x},
                     "y": {"object": offset_y},}
}

wm.set_ux_inputs(inputs)
wm.set_img_label(image_lbl)
wm.set_mark_preview(preview_lbl)
wm.set_dynamic_elements(dynamic_elements)
wm.update_img_lbl(wm.img_label,img_sub=wm.image)
root.mainloop()
