from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    # Check number of command line arguments
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage! Usage: 'python figlet.py' OR 'python figlet.py -f <font_name>' OR 'python figlet.py --font <font_name>'")
    # Check validity of font provided by user
    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit("Invalid usage! Usage: 'python figlet.py' OR 'python figlet.py -f <font_name>' OR 'python figlet.py --font <font_name>'")
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid font! Check all fonts available: http://www.figlet.org/fontdb.cgi")
        # Convert text to the specific font provided by user
        figlet.setFont(font=sys.argv[2])

    # Get user's input
    text = input("Input: ")
    # Output formated text
    print("Output:", figlet.renderText(text))


if __name__ == "__main__":
    main()