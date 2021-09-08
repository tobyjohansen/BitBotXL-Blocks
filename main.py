bitbot.select_model(BBModel.XL)

def on_forever():
    if bitbot.read_line(BBLineSensor.LEFT) == 1:
        bitbot.rotatems(BBRobotDirection.LEFT, 20, 400)
        bitbot.set_pixel_color(6, 0xFF0000)
    elif bitbot.read_line(BBLineSensor.RIGHT) == 1:
        bitbot.rotatems(BBRobotDirection.RIGHT, 20, 400)
        bitbot.set_pixel_color(12, 0xFF0000)
    elif bitbot.read_line(BBLineSensor.LEFT) == 1 and bitbot.read_line(BBLineSensor.RIGHT) == 1:
        bitbot.stop(BBStopMode.BRAKE)
    else:
        bitbot.go(BBDirection.FORWARD, 20)
basic.forever(on_forever)
