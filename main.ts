bitbot.select_model(BBModel.XL)
basic.forever(function () {
    if (bitbot.readLine(BBLineSensor.Left) == 1) {
        bitbot.rotatems(BBRobotDirection.Left, 20, 400)
        bitbot.setPixelColor(6, 0xFF0000)
    } else if (bitbot.readLine(BBLineSensor.Right) == 1) {
        bitbot.rotatems(BBRobotDirection.Right, 20, 400)
        bitbot.setPixelColor(12, 0xFF0000)
    } else if (bitbot.readLine(BBLineSensor.Left) == 1 && bitbot.readLine(BBLineSensor.Right) == 1) {
        bitbot.stop(BBStopMode.Brake)
    } else {
        bitbot.go(BBDirection.Forward, 20)
    }
})
