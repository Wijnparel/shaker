def on_logo_touched():
    basic.show_string("BIOS")
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO1, 45, 64)
    basic.pause(5000)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO1, 90, 64)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 120, 64)
    basic.pause(1000)
    for index in range(4):
        PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 0, 64)
        basic.pause(200)
        PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 60, 64)
        basic.pause(200)
    basic.pause(1000)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 120, 64)
input.on_button_pressed(Button.B, on_button_pressed_b)

PCA9685.reset(64)
PCA9685.set_servo_position(PCA9685.ServoNum.SERVO1, 100, 64)
basic.pause(1000)
PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 120, 64)