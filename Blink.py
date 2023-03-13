import machine
import utime

led_external = machine.Pin(14, machine.Pin.OUT)
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(1)

while True:
    led_external.toggle()
    led_onboard.toggle()
    utime.sleep(.5)