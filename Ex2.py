def on_forever():
    if  input.logo_is_pressed():
        basic.show_icon(IconNames.SQUARE)
        basic.show_icon(IconNames.SMALL_SQUARE)
basic.forever(on_forever)
