def on_gesture_screen_down():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    radio.send_number(0)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_tilt_left():
    basic.show_leds("""
        . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
    """)
    radio.send_number(3)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_down():
    basic.show_leds("""
        . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
    """)
    radio.send_number(2)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_gesture_shake():
    basic.show_leds("""
        . . # . .
                . # . # .
                # # # # #
                . # . # .
                . . # . .
    """)
    radio.send_number(0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_up():
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
    """)
    radio.send_number(1)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_free_fall():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    radio.send_number(0)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
    """)
    radio.send_number(4)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_screen_up():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    radio.send_number(0)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

radio.set_group(1)