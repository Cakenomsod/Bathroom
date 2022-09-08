let Distance = 0
basic.forever(function () {
    Distance = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
    )
    basic.showNumber(Distance)
    pins.servoWritePin(AnalogPin.P8, 0)
    if (Distance > 0 && Distance <= 25) {
        pins.servoWritePin(AnalogPin.P8, 0)
        basic.pause(3000)
    } else {
        pins.servoWritePin(AnalogPin.P8, 90)
        basic.pause(500)
    }
    basic.pause(200)
})
