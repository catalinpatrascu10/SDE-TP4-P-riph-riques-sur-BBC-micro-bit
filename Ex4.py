# Pentru N si S indica nivel bruit
# Pentru E sau V indica nivel lumina
def on_forever():
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string('N')
        print(basic.show_number(input.sound_level()))
    elif degrees < 135:
        basic.show_string('E')
        print(basic.show_number(input.light_level()))
    elif degrees < 225:
        basic.show_string('S')
        print(basic.show_number(input.sound_level()))
    elif degrees < 315:
        basic.show_string('W')
        print(basic.show_number(input.light_level()))
    else:
        basic.clear_screen()
basic.forever(on_forever)