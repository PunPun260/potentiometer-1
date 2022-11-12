_1 = 0

def on_button_pressed_a():
    if _1 == 1:
        music.play_melody("C5 B A G F E D C ", 120)
        music.stop_all_sounds()
    elif _1 == 1:
        music.play_melody("C D E F G A B C5 ", 120)
        music.stop_all_sounds()
    else:
        music.play_melody("E B C5 A B G A F ", 120)
        music.stop_all_sounds()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global _1
    serial.write_value("x", pins.analog_read_pin(AnalogPin.P0))
    basic.show_number(Math.round(Math.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, 1, 3)))
    _1 = Math.round(Math.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, 1, 3))
basic.forever(on_forever)
