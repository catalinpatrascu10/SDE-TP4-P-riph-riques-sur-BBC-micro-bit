def on_sound_loud():
    basic.show_leds("""
    # # # # #
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
input.on_sound(DetectedSound.LOUD, on_sound_loud)