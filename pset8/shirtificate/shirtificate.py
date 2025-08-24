from fpdf import FPDF


def main():
    name = input("Enter your name: ").strip()
    pdf_generator(name)


def pdf_generator(str):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    # Top text
    pdf.set_font('helvetica', style="B", size=40)
    pdf.set_text_color(0, 0, 0) # Black text
    title = "CS50 Shirtificate"
    title_width = pdf.get_string_width(title)
    pdf.set_x((210 - title_width) / 2)
    pdf.set_y(30)
    pdf.cell(0, 10, title, align="C")  

    # Image
    # Set image's width to 180, allowing it to fit page, and triggering autoscale
    pdf.image("shirtificate/shirtificate.png", x=(210-180)/2, y=70, w=180)

    # Image text
    pdf.set_font('helvetica', style="B", size=20)
    pdf.set_text_color(255, 255, 255) # White text
    name = f"{str} took CS50"
    pdf.set_y(120)
    pdf.set_x((210 - 100)/2)
    # multi_cell allows auto-breaking text
    pdf.multi_cell(100, 10, name, align="C")  

    pdf.output("shirtificate/shirtificate.pdf")


if __name__ == "__main__":
    main()


# Documentation used:
# https://pypi.org/project/fpdf2/
# https://py-pdf.github.io/fpdf2/fpdf/