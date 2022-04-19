# afiseaza in consola temperatura la apasare B
# afiseaza in consola nivel lumina la apasare logo


def on_forever():
    if input.button_is_pressed(Button.B):
        print(basic.show_number(input.temperature()))
    elif input.logo_is_pressed():
        print(basic.show_number(input.light_level()))
basic.forever(on_forever)
