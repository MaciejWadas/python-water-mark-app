# Desktop Image Watermarker

A simple desktop application for adding customizable watermarks to images. Supports both text and image-based watermarks with flexible positioning, sizing, opacity, rotation, and repetition options.

## Features

- Load any image file (PNG, JPG, JPEG, etc.) as the base image.
- Add watermarks in two modes:
  - **Text watermark:** Enter custom text, choose font size, rotation, and opacity.
  - **Image watermark:** Load a watermark image, adjust size, rotation, and opacity.
- Position watermark precisely by X and Y coordinates.
- Optionally repeat the watermark across the entire image with configurable spacing and offsets.
- Preview watermark applied directly on the image before saving.
- Save the watermarked image in PNG format.
- User-friendly GUI built with Tkinter for easy image and watermark management.

## User Interface

- **Open image:** Choose the base image to watermark.
- **Save image as:** Save the edited image with watermark.
- **Mark type:** Select between "Text" or "Image" watermark.
- **Text settings:** Input the watermark text and font size.
- **Image settings:** Choose an image to use as a watermark and set size percentage.
- **General settings:** Adjust position (X, Y), opacity (%), rotation (degrees), and enable repeat mode.
- **Repeat settings:** Configure spacing and offset between repeated watermarks.
- **Preview:** Shows a thumbnail preview of the image watermark (if image watermark is selected).
- **Add mark:** Applies the configured watermark to the base image and updates the preview.

## Technical Details

- Written in Python using PIL/Pillow for image processing and Tkinter for the GUI.
- Uses alpha compositing to blend watermark with the source image, allowing transparency control.
- Scales watermark size and positioning dynamically based on image dimensions.
- Supports rotation and opacity adjustments for artistic watermark effects.
- Repeat mode tiles the watermark based on user-defined spacing and offsets.

## Usage

1. Run `main.py` to launch the application.
2. Use the "Open image" button to select the image you want to watermark.
3. Choose watermark type: text or image.
4. Configure watermark text or select an image for watermarking.
5. Set size, position, opacity, rotation, and repetition options as desired.
6. Click "Add mark" to apply the watermark on the preview.
7. Save the resulting image using the "Save Image As" button.

## Requirements

- Python 3.x
- Pillow (PIL) library
- Tkinter (usually included with Python standard library)

## License

This project is open source and free to use.

---

This application provides a flexible and intuitive way to watermark images for personal or professional use, with full control over watermark appearance and positioning.
