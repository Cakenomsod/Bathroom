Distance = 0

def on_forever():
    global Distance
    Distance = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    basic.show_number(Distance)
    pins.servo_write_pin(AnalogPin.P8, 0)
    if Distance > 0 and Distance <= 25:
        pins.servo_write_pin(AnalogPin.P8, 0)
        basic.pause(3000)
    else:
        pins.servo_write_pin(AnalogPin.P8, 90)
        basic.pause(500)
    basic.pause(200)
basic.forever(on_forever)
