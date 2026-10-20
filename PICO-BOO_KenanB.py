"""

PICO-BOO!

By:Kenan Batic
10/13/2025
v 1.0
"""

from machine import I2C, Pin, PWM       #these 3 lines import everything i need to set up the pico-BOO
from pico_i2c_lcd import I2cLcd
from time import sleep

# sets photoresistor as analog input
photoresistor_pin = 27            
photoresistor = machine.ADC(photoresistor_pin)

led_pin = 15 # sets the LED pin to correct number
led = Pin(led_pin, Pin.OUT) #sets pin 15 as an output pin

secondLED_pin = 14    #sets up 2nd LED pin to correct number
secondLED = Pin(secondLED_pin, Pin.OUT)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=50000) #this sets up my LCD screen to the right pin
I2C_ADDR = 0x27
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()
lcd.putstr("Ready!") #displays this when i start the code on the LCD
sleep(1)
lcd.clear()
                

def slow_type(lcd, text, delay=0.1):     #defines the function to display text
    for i in text:                       #this makes it so that it reads text as a list
        lcd.putstr(i)                    #this prints the letter to the LCD
        sleep(delay)                     # has a delay for putting the text


# Setup the pin as a PWM object
servo_pin = 2
servo = PWM(machine.Pin(servo_pin))

# Set Duty Cycle for Different Angles
# Default pulse width: 550 - 2400 ms
# Duty cycle (%) = (pulsewidth/period)*100
max_duty = 7864
min_duty = 1802
half_duty = int((max_duty+min_duty)/2)




# Set PWM frequency
frequency = 50
servo.freq(frequency)


while True: #my while statement for the Boo effect
    photoRes = int((photoresistor.read_u16() / 65535)*100) #prints the value of my photoresistor as a whole number (this and the line below it)
    print(photoRes)
    sleep(0.5)
    if photoRes < 5:  #if statement so that when it is dark the boo effect takes place
        servo.duty_u16(min_duty) #this and line 70 move the servo back and forth
        led.on()
        secondLED.on()
        lcd.show_cursor()
        lcd.blink_cursor_on()
        slow_type(lcd,"boo!!", 0) #prints boo!! on LCD
        sleep(0.1)
        servo.duty_u16(max_duty) 
        led.off()
        secondLED.off()
    else:   #if its not dark then its this
        led.off()
        secondLED.off()
        lcd.blink_cursor_off()
        lcd.hide_cursor()
        lcd.clear()#Clears screen
        
        
        
        
    
