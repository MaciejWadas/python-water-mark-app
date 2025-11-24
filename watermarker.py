import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
from PIL import ImageFont

class WaterMarker:
    def __init__(self):
        self.image = self.load_img("")
        self.image_mark = None
        self.img_thumb = None
        self.image_to_save = self.image.copy()
        self.scale = 1.0
        self.image_max_size = 500
        self.is_img_mark = False
        self.ux_inputs = {}
        self.params = {}
        self.img_label = None
        self.dynamic_elements = {}
        self.mark_preview = None

    @staticmethod
    def load_img(path=None):
        if not path:
            return Image.new('RGBA', (5000, 3000), (255, 255, 255, 255))
        else:
            return Image.open(path).convert("RGBA")

    def choose_img_from_explr(self,label, is_mark=False):
        filename = filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=(
            ("All files", "*.*"), ("PNG files", ".png"), ("JPG files", ".jpg"), ("JPEG files", ".jpeg")))
        if not is_mark:
            self.update_img_lbl(filename=filename,label=label)

        else:
            self.image_mark = self.load_img(filename)
            img_preview = self.image_mark.copy()
            img_preview.thumbnail((80, 80))
            tk_out = ImageTk.PhotoImage(img_preview)
            self.mark_preview.configure(image=tk_out)
            self.mark_preview.image = tk_out

    def update_img_lbl(self,label,  filename=None, img_sub=None):
        if img_sub:
            self.img_thumb = img_sub.copy()
        else:
            if filename:
                self.image = self.load_img(filename)
                self.image_to_save = self.image.copy()
                self.img_thumb = self.image.copy()
        self.img_thumb.thumbnail((self.image_max_size, self.image_max_size))
        self.scale = self.image.size[0] / self.img_thumb.size[0]
        tk_out = ImageTk.PhotoImage(self.img_thumb)
        label.configure(image=tk_out)
        label.image = tk_out
        self.update_dynamic_elements()

    def update_dynamic_elements(self):
        for elem_dict in self.dynamic_elements.values():
            for elem_dim in ("x","y"):
                value = self.image.size[0] if elem_dim == "x" else self.image.size[1]
                elem = elem_dict[elem_dim]["object"]
                if isinstance(elem, tkinter.Label):
                    content = elem_dict[elem_dim]["value"]
                    content = content.replace("{VALUE}", str(value))
                    elem.config(text=content)
                    elem.text = content
                else:
                    elem.config(to=value)

    def save_img(self):
        file = filedialog.asksaveasfile(mode="wb", initialdir="/", defaultextension=".png")
        if file:
            self.image_to_save.save(file)
        else:
            return

    def set_ux_inputs(self, inputs):
        self.ux_inputs = inputs

    def set_img_label(self, img_lbl):
        self.img_label = img_lbl

    def set_mark_preview(self, mark_preview):
        self.mark_preview = mark_preview

    def set_dynamic_elements(self, dynamic_elements):
        self.dynamic_elements = dynamic_elements

    def mark_image(self):
        self.parse_data()
        mark_height = int(self.params["font_size"] * self.scale)
        txt = Image.new('RGBA', self.image.size, (255, 255, 255, 0))
        mode = "img" if self.params["mark_type"]=="Image" else "str"
        if mode == "str":
            mark_data = self.params["text"]
            font_size = int(self.params["font_size"]*self.scale)
            fnt = ImageFont.truetype("font.ttf", font_size)
            mark_width = int(fnt.getlength(mark_data))
        else:
            mark_data = self.image_mark
            mark_width = int(self.params["mark_size"]*self.scale)
            mark_height = mark_width
            mark_data.resize((mark_width, mark_height))
            fnt = None
        mark_centre = (mark_width // 2, mark_height // 2)
        x_spacing = self.params["spacing_x"] + mark_width
        y_spacing = self.params["spacing_y"] + mark_height
        if self.params["repeat"]:
            for i in range(self.image.size[0] // x_spacing + 1):
                for j in range(self.image.size[1] // y_spacing + 1):
                    mark_position = (i * x_spacing + int(self.params["offset_x"]), j * y_spacing + int(self.params["offset_y"]))
                    self.add_mark(txt, mode, mark_data, mark_centre, mark_position, mark_width, mark_height, fnt)
        else:
            position = int(self.params["pos_x"]),int(self.params["pos_y"])
            self.add_mark(txt, mode, mark_data, mark_centre, position, mark_width, mark_height, fnt)
        out = Image.alpha_composite(self.image, txt)
        self.image_to_save = out
        self.update_img_lbl(img_sub=out,label=self.img_label)

    def add_mark(self, txt, mode, mark_data, mark_centre, position, mark_width, mark_height, fnt=None):
        if mode == "img":
            mark = mark_data.copy()
            r, g, b, a = mark.split()
            opacity = self.params["opacity"] / 100
            a = a.point(lambda p: p * opacity)
            mark.putalpha(a)
            mark = mark.resize((mark_width, mark_height))
        else:
            mark = Image.new("RGBA", (mark_width, mark_height), (255, 255, 255, 0))
            d = ImageDraw.Draw(mark)
            opacity = self.params["opacity"] / 100

            d.text((0, 0), mark_data, font=fnt, fill=(255, 255, 255, 255))

            alpha = mark.split()[3]
            alpha = alpha.point(lambda p: p * opacity)
            mark.putalpha(alpha)

        rot = mark.rotate(self.params["rotation"], center=mark_centre, expand=1)
        txt.paste(rot, position, rot)

    def parse_data(self):
        params = {}
        for key, elem in self.ux_inputs.items():
            if key != "repeat":
                value = elem.get()
                if value.isnumeric():
                    params[key] = int(value)
                else:
                    params[key] = value
        params["repeat"] = self.ux_inputs["repeat"].get()
        params["mark_type"] = self.ux_inputs["mark_type"].get()
        self.params = params
