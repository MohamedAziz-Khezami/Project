import pyfiglet

import sys


if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or len(sys.argv) != 3:
    sys.exit("Invalid usage")
try:
    font = pyfiglet.Figlet(font=sys.argv[2])
except pyfiglet.FigletFontNotFound:
    sys.exit("Invalid usage")


ph = input("")
result = font.renderText(ph)
print(result)
