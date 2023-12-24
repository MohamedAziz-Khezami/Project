from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 30)

        width = self.get_string_width(self.title) + 6
        self.set_x((220 - width) / 2)

        self.set_text_color(250, 250, 250)

        self.cell(
            width,
            12,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )

    def _name(self, n):
        self.add_page()
        self.image("shirtificate.png", 0.4, 50)
        self.set_font("helvetica", "B", 15)
        self.set_text_color(250, 250, 250)
        self.set_line_width(1)
        width = self.get_string_width(n) + 6
        x = (220 - width) / 2
        y = 110

        self.set_xy(x, y)

        self.cell(0, 6, n)


def main():
    name = input("Name: ")

    pdf = PDF("P", "mm", "A4")
    pdf.set_title("CS 50 Shirtificate")
    pdf._name(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
