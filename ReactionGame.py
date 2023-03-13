import machine
import utime
import urandom

left_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
right_button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_external = machine.Pin(15, machine.Pin.OUT)
pressed = False
fastest_button = None
#make led light at a random time
#detect input from a button after the light is pressed
#find how long it took the button to be pressed after the light turned on.
#tell the user how long it took them to press the button

def button_handler(pin):
    global pressed
    global fastest_button
    if not pressed:
        pressed = True
        fastest_button = pin
        

led_external.value(1)
utime.sleep(urandom.uniform(5, 10))
led_external.value(0)
timer_start = utime.ticks_ms()
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)
    
if fastest_button is left_button:
    print("Left Player wins!")
elif fastest_button is right_button:
    print("Right Player wins!")