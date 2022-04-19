# la scuturat placa -> un cantec suna
# cand apasa A si B simultan alarma se opreste
def on_gesture_shake():
    accel = input.acceleration(Dimension.X)
    basic.show_number(accel)
    music.play_melody("", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
def stopAlarm():
    while True:
        if input.button_is_pressed(Button.A) and input.button_is_pressed(Button.B):
            music.stop_all_sounds()