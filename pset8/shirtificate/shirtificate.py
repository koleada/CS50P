from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont


def main():
    name = input("Name: ")
    shirt_text = f"{name} took CS50"
    create_pdf(shirt_text)


def create_pdf(shirt_text):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("Times", size=45)
    pdf.cell(
        w=pdf.epw, h=35, text="CS50 Shirtificate", align="C", center=True, new_x="LEFT"
    )
    img = set_img_text(shirt_text)
    pdf.image(img, y=70, w=pdf.epw)

    pdf.output("shirtificate.pdf", "F")


def set_img_text(shirt_text):
    img = Image.open("shirtificate.png")
    draw = ImageDraw.Draw(img)
    y = img.height * 1 / 3
    x = img.width / 2
    font = ImageFont.load_default(size=25)
    draw.text((x, y), text=shirt_text, align="center", font=font, anchor="mt")
    return img


if __name__ == "__main__":
    main()
