from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', '', 50)
        # Calculate width of title and position
        w = self.get_string_width('CS50 Shirtificate') + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 60, 'CS50 Shirtificate', 0, 1, 'C') #2nd parapeter is Y axis of title

    def chapter_title(self, name):
        self.set_font('Arial', '', 25)
        # Calculate width of title and position
        w = self.get_string_width(f'{name} took CS50') + 6
        self.set_x((210 - w) / 2)
        self.set_text_color(255, 255, 255)
        self.cell(w, 6, f'{name} took CS50p', 0, 1, 'C', fill=False)


def create_shirtificate(name):
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()
    # Calculate x position to center image
    img_width = 190  # The width of the image in mm
    page_width = 210  # The width of an A4 page in portrait orientation in mm
    x = (page_width - img_width) / 2

    pdf.image('shirtificate.png', x = x, y = 80, w = img_width, h = 0, type = '', link = '') # y is Y axis of Shirt pic
    pdf.ln(70)  # Y axis of name writing
    pdf.chapter_title(name)
    pdf.output('shirtificate.pdf', 'F')


def main():
    name = input('Name: ')
    create_shirtificate(name)


if __name__ == "__main__":
    main()
