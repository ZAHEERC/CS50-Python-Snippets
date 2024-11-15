pip install fpdf
from fpdf import FPDF

# Create PDF class that extends FPDF
class PDF(FPDF):
    def header(self):
        # Set font for the header (title)
        self.set_font('Arial', 'B', 24)
        # Title: CS50 Shirtificate, centered horizontally
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

    def footer(self):
        # Go to 1.5 cm from the bottom
        self.set_y(-15)
        # Set font for the footer
        self.set_font('Arial', 'I', 8)
        # Add page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create a PDF document
pdf = PDF()

# Add a page (portrait, A4 size)
pdf.add_page()

# User input for the name
name = input("What is your name? ")

# Set font for the name on the shirt
pdf.set_font('Arial', 'B', 36)
# Set text color to white (RGB)
pdf.set_text_color(255, 255, 255)

# Get the width of the name (so it can be centered)
name_width = pdf.get_string_width(name)

# Calculate X position to center the text (A4 size is 210mm)
pdf.set_xy((210 - name_width) / 2, 100)  # X is centered, Y is at 100mm (just below the title)

# Print the user's name in the center of the page
pdf.cell(name_width, 10, name, 0, 1, 'C')

# Add the shirt image centered horizontally
# Set the image properties (file name, x position, y position, width, height)
shirt_image = 'shirtificate.png'
image_width = 140  # Width in mm
image_height = 140  # Height in mm

# Image's x position should be centered horizontally
image_x = (210 - image_width) / 2

# The y position (just below the name) can be fixed or adjusted based on your needs
image_y = 130  # This is just an arbitrary choice to position the shirt below the name

# Add the shirt image to the PDF
pdf.image(shirt_image, x=image_x, y=image_y, w=image_width, h=image_height)

# Output the PDF to a file
pdf.output('shirtificate.pdf')

print("Shirtificate generated as shirtificate.pdf!")
