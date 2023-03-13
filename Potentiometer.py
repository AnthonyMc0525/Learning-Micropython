import machine
import utime

potentiometer = machine.ADC(26)
external_led = machine.PWM(machine.Pin(15))
external_led.freq(1000)


while True:
    external_led.duty_u16(potentiometer.read_u16())