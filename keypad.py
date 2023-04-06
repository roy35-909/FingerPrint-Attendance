from Display import print_lcd
def get_input(s="#"):
    if s!="#":
        print_lcd(s)
    data = -1
    data = input()
    return data
