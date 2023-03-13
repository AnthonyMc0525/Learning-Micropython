import machine
import utime
from pico_i2c_lcd import I2cLcd

adc = machine.ADC(4)
conversion_factor = 3.3/65535

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    reading = adc.read_u16() * conversion_factor
    temperature = 25 - (reading - .706)/.001721
    lcd.putstr("Temp: " + str(temperature))
    utime.sleep(2)
    lcd.clear()