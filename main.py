direction = 0
distance = 0
n = 0
DFRobotMaqueenPlusV2.init()
DFRobotMaqueenPlusV2.control_led(MyEnumLed.E_ALL_LED, MyEnumSwitch.E_OPEN)
DFRobotMaqueenPlusV2.set_brightness(100)
R = 0
G = 1
B = 2
P = 3

def on_forever():
    global R, G, B, P, n
    if R <= 3:
        DFRobotMaqueenPlusV2.set_index_color(R, 0xff0000)
        R += 1
    else:
        R = 0
    if G <= 3:
        DFRobotMaqueenPlusV2.set_index_color(G, 0x00ff00)
        G += 1
    else:
        G = 0
    if B <= 3:
        DFRobotMaqueenPlusV2.set_index_color(B, 0x007fff)
        B += 1
    else:
        B = 0
    if P <= 3:
        DFRobotMaqueenPlusV2.set_index_color(P, 0xff00ff)
        P += 1
    else:
        P = 0
    n += 1
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    global distance, direction
    distance = DFRobotMaqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    direction = randint(1, 2)
    if distance < 30 and distance != 0:
        if direction == 1:
            DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 100)
            DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 0)
            basic.pause(1000)
        if direction == 2:
            DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 0)
            DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 100)
            basic.pause(1000)
    else:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_ALL_MOTOR, MyEnumDir.E_FORWARD, 100)
basic.forever(on_forever2)
