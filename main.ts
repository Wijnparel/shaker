input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    basic.showString("BIOS")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    PCA9685.setServoPosition(PCA9685.ServoNum.Servo1, 45, 64)
    basic.pause(5000)
    PCA9685.setServoPosition(PCA9685.ServoNum.Servo1, 90, 64)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    PCA9685.setServoPosition(PCA9685.ServoNum.Servo4, 120, 64)
    basic.pause(1000)
    for (let index = 0; index < 4; index++) {
        PCA9685.setServoPosition(PCA9685.ServoNum.Servo4, 0, 64)
        basic.pause(200)
        PCA9685.setServoPosition(PCA9685.ServoNum.Servo4, 60, 64)
        basic.pause(200)
    }
    basic.pause(1000)
    PCA9685.setServoPosition(PCA9685.ServoNum.Servo4, 120, 64)
})
PCA9685.reset(64)
PCA9685.setServoPosition(PCA9685.ServoNum.Servo1, 100, 64)
basic.pause(1000)
PCA9685.setServoPosition(PCA9685.ServoNum.Servo4, 120, 64)
