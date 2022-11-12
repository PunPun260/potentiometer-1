let _1 = 0
input.onButtonPressed(Button.A, function () {
    if (_1 == 1) {
        music.playMelody("C5 B A G F E D C ", 120)
        music.stopAllSounds()
    } else if (_1 == 2) {
        music.playMelody("C D E F G A B C5 ", 120)
        music.stopAllSounds()
    } else {
        music.playMelody("E B C5 A B G A F ", 120)
        music.stopAllSounds()
    }
})
basic.forever(function () {
    serial.writeValue("x", pins.analogReadPin(AnalogPin.P0))
    basic.showNumber(Math.round(Math.map(pins.analogReadPin(AnalogPin.P1), 0, 1023, 1, 3)))
    _1 = Math.round(Math.map(pins.analogReadPin(AnalogPin.P1), 0, 1023, 1, 3))
})
