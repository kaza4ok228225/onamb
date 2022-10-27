def on_button_pressed_a():
    global Close, Close2
    if Scroll == 1:
        if Close == 0:
            led.plot(0, 2)
            led.plot(0, 3)
            led.plot(0, 4)
            led.plot(1, 2)
            led.plot(1, 3)
            led.plot(1, 4)
            Close = 1
        else:
            Close = 0
            led.unplot(0, 2)
            led.unplot(0, 3)
            led.unplot(0, 4)
            led.unplot(1, 2)
            led.unplot(1, 3)
            led.unplot(1, 4)
    elif Scroll == 2:
        if Close2 == 0:
            led.plot(3, 2)
            led.plot(3, 3)
            led.plot(3, 4)
            led.plot(4, 2)
            led.plot(4, 3)
            led.plot(4, 4)
            Close2 = 1
        else:
            Close2 = 0
            led.unplot(3, 2)
            led.unplot(3, 3)
            led.unplot(3, 4)
            led.unplot(4, 2)
            led.unplot(4, 3)
            led.unplot(4, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Scroll
    if Scroll == 1:
        Scroll = 0
        myImage.show_image(2)
        myImage.show_image(3)
        Scroll = 2
        myImage.show_image(5)
    elif Scroll == 2:
        Scroll = 0
        myImage.show_image(3)
        myImage.show_image(2)
        Scroll = 1
        myImage.show_image(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

myImage: Image = None
Scroll = 0
Close2 = 0
Close = 0
Close = 0
Close2 = 0
Scroll = 1
myImage = images.create_big_image("""
    . . # . . . . # . .
        # # # . . . . # # #
        . . # . # # . # . .
        . . # # # # # # . .
        . . # . . . . # . .
""")
myImage.show_image(0)

def on_forever():
    if Close2 == 1 and Scroll == 2:
        led.plot(3, 2)
        led.plot(3, 3)
        led.plot(3, 4)
        led.plot(4, 2)
        led.plot(4, 3)
        led.plot(4, 4)
basic.forever(on_forever)

def on_forever2():
    if Close == 1 and Scroll == 1:
        led.plot(0, 2)
        led.plot(0, 3)
        led.plot(0, 4)
        led.plot(1, 2)
        led.plot(1, 3)
        led.plot(1, 4)
basic.forever(on_forever2)
