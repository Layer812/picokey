# picokey: Pico HID Keyboard device for TRS-80
# Copyright 2022, Layer8 https://twitter.com/layer812
# Licensed under the Apache License, Version 2.0
import board, digitalio, usb_hid, os, time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#キースキャン間隔(秒)
Keyscaninterval=0.02

#マトリクスキー読み込みルーチン
def mtxkeys(rows, cols, keymap):
    pressed = []
    i=0
    for row in rows:
        row.direction = digitalio.Direction.OUTPUT
        row.value = True
        for col in cols:
            if col.value:
                key = keymap[rows.index(row)][cols.index(col)]
                if not key in pressed:
                    pressed.append(key)
        row.value = False
        row.direction = digitalio.Direction.INPUT
    return pressed

#TRS-80のキーマップ
keymap=(
	(Keycode.Z,	Keycode.A,	Keycode.Q,	Keycode.O,		Keycode.ONE,	Keycode.NINE,		Keycode.SPACEBAR,	Keycode.F1,	Keycode.LEFT_SHIFT),
	(Keycode.X,	Keycode.S,	Keycode.W,	Keycode.P,		Keycode.TWO,	Keycode.ZERO,		Keycode.BACKSPACE,	Keycode.F2,	Keycode.LEFT_CONTROL),
	(Keycode.C,	Keycode.D,	Keycode.E,	Keycode.BACKSLASH,	Keycode.THREE,	Keycode.MINUS,		Keycode.TAB,		Keycode.F3,	Keycode.LEFT_ALT),
	(Keycode.V,	Keycode.F,	Keycode.R,	Keycode.SEMICOLON,	Keycode.FOUR,	Keycode.EQUALS,		Keycode.ESCAPE,		Keycode.F4,	Keycode.GRAVE_ACCENT),
	(Keycode.B,	Keycode.G,	Keycode.T,	Keycode.QUOTE,		Keycode.FIVE,	Keycode.LEFT_ARROW,	Keycode.QUOTE,		Keycode.F5,	Keycode.KEYPAD_NUMLOCK),
	(Keycode.N,	Keycode.H,	Keycode.Y,	Keycode.COMMA,		Keycode.SIX,	Keycode.RIGHT_ARROW,	Keycode.LEFT_BRACKET,	Keycode.F6,	Keycode.CAPS_LOCK),
	(Keycode.M,	Keycode.J,	Keycode.U,	Keycode.PERIOD,		Keycode.SEVEN,	Keycode.UP_ARROW,	Keycode.LEFT_BRACKET,		Keycode.F7,	Keycode.HOME),
	(Keycode.L,	Keycode.K,	Keycode.I,	Keycode.FORWARD_SLASH,	Keycode.EIGHT,	Keycode.DOWN_ARROW,	Keycode.ENTER,		Keycode.F8,	Keycode.RIGHT_BRACKET)
)

#今のところはItsyBitsy RP2040だけサポート
board_type = os.uname().machine
if 'ItsyBitsy RP2040' in board_type:
    rows = [digitalio.DigitalInOut(x) for x in (board.D12,	board.D11,	board.D10,	board.D9,	board.D7,	board.SDA,	board.SCL,	board.TX)]
    cols = [digitalio.DigitalInOut(x) for x in (board.A0,	board.A1,	board.A2,	board.A3,	board.D24,	board.D25,	board.SCK,	board.MOSI,	board.MISO)]
else:
    print("Request me to support your board!")
    exit

#GPIOの初期化
for pin in rows + cols:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.DOWN
#HID USB Keyboardの初期化
usbkey =  Keyboard(usb_hid.devices)
#読めたキーをUSB経由で送るメイン
pkeys=[]
i=0
while True:
    keys = mtxkeys(rows, cols, keymap)
    if keys and keys != pkeys:
        usbkey.send(*keys)
        i=0
    else:
        i=i+1
    if i > 20:
        pkeys=[]
        i=0
    else:
        pkeys=keys
    time.sleep(Keyscaninterval)
