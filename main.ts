input.onButtonPressed(Button.A, function () {
    if (Scroll == 1) {
        if (Close == 0) {
            led.plot(0, 2)
            led.plot(0, 3)
            led.plot(0, 4)
            led.plot(1, 2)
            led.plot(1, 3)
            led.plot(1, 4)
            Close = 1
        } else {
            Close = 0
            led.unplot(0, 2)
            led.unplot(0, 3)
            led.unplot(0, 4)
            led.unplot(1, 2)
            led.unplot(1, 3)
            led.unplot(1, 4)
        }
    } else if (Scroll == 2) {
        if (Close2 == 0) {
            led.plot(3, 2)
            led.plot(3, 3)
            led.plot(3, 4)
            led.plot(4, 2)
            led.plot(4, 3)
            led.plot(4, 4)
            Close2 = 1
        } else {
            Close2 = 0
            led.unplot(3, 2)
            led.unplot(3, 3)
            led.unplot(3, 4)
            led.unplot(4, 2)
            led.unplot(4, 3)
            led.unplot(4, 4)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (Scroll == 1) {
        Scroll = 0
        myImage.showImage(2)
        myImage.showImage(3)
        Scroll = 2
        myImage.showImage(5)
    } else if (Scroll == 2) {
        Scroll = 0
        myImage.showImage(3)
        myImage.showImage(2)
        Scroll = 1
        myImage.showImage(0)
    }
})
let myImage: Image = null
let Scroll = 0
let Close2 = 0
let Close = 0
Close = 0
Close2 = 0
Scroll = 1
myImage = images.createBigImage(`
    . . # . . . . # . .
    # # # . . . . # # #
    . . # . # # . # . .
    . . # # # # # # . .
    . . # . . . . # . .
    `)
myImage.showImage(0)
basic.forever(function () {
    if (Close == 1 && Scroll == 1) {
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
    }
})
basic.forever(function () {
    if (Close2 == 1 && Scroll == 2) {
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.plot(4, 2)
        led.plot(4, 3)
        led.plot(4, 4)
    }
})
