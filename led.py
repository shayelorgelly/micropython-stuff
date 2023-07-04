"""onboard led stuff"""


from machine import Pin as pin
from machine import PWM
led = pin(2, pin.OUT); 
def on():
    disable_pwm()
    led = pin(2, pin.OUT)
    led.value(1)
def off():
    disable_pwm()
    led = pin(2, pin.OUT)
    led.value(0)
def toggle():
    if led.value() == 1:
        off()
    else:
        on()
def pwm(duty, freq):  # duty is between 0 (all off) and 1023 (all on)   frequency must be between 1Hz and 1kHz.
    disable_pwm()
    global ledpwm
    ledpwm = PWM(led)
    ledpwm.freq(freq)
    ledpwm.duty(duty)
    
def disable_pwm():
     if "ledpwm" in globals():
        global ledpwm  # get pwm global thing
        ledpwm.deinit()  # turn it off
        del ledpwm  # delete global
    
        
