from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

mods=[]

def addMod(mod):
	global mods
	mods.append(mod)

def sendCommands(keys):
	global mods
	print(len(mods))
	keysToPress = mods + [keys]
	for i in keysToPress:
		kbd.press(i)
	kbd.release_all()
	mods.clear()

artseyio = {
	'10000000': (sendCommands, Keycode.A),
	'01000000': (sendCommands, Keycode.R),
	'00100000': (sendCommands, Keycode.T),
	'00010000': (sendCommands, Keycode.S),
	'00001000': (sendCommands, Keycode.E),
	'00000100': (sendCommands, Keycode.Y),
	'00000010': (sendCommands, Keycode.I),
	'00000001': (sendCommands, Keycode.O),

	'00001001': (sendCommands, Keycode.B),
	'00001100': (sendCommands, Keycode.C),
	'11100000': (sendCommands, Keycode.D),
	'11000000': (sendCommands, Keycode.F),
	'01100000': (sendCommands, Keycode.G),
	'00001010': (sendCommands, Keycode.H),
	'00110000': (sendCommands, Keycode.J),
	'00000101': (sendCommands, Keycode.K),
	'00001110': (sendCommands, Keycode.L),
	'00000111': (sendCommands, Keycode.M),
	'00000011': (sendCommands, Keycode.N),
	'00001101': (sendCommands, Keycode.P),
	'11010000': (sendCommands, Keycode.Q),
	'00000110': (sendCommands, Keycode.U),
	'01010000': (sendCommands, Keycode.V),
	'01110000': (sendCommands, Keycode.X),
	'10010000': (sendCommands, Keycode.W),
	'11110000': (sendCommands, Keycode.Z),
	'00001111': (sendCommands, Keycode.SPACE),
	'10001000': (sendCommands, Keycode.ENTER),
	'00011000': (layout.write, 'test'),


	'01001000': (sendCommands, Keycode.DELETE),
	'00101000': (sendCommands, Keycode.BACKSPACE),

	# mods
	'00010001': (addMod, Keycode.SHIFT),
	'00100001': (addMod, Keycode.ALT),
	'01000001': (addMod, Keycode.CONTROL),
	'10000001': (addMod, Keycode.GUI),

	# layer
	'01001010': 'navigation',
	'00110011': 'numeric',
}

numeric = {
	'10000000': (sendCommands, Keycode.SIX),
	'01000000': (sendCommands, Keycode.FIVE),
	'00100000': (sendCommands, Keycode.FOUR),
	'00010000': (sendCommands, Keycode.S),
	'00001000': (sendCommands, Keycode.THREE),
	'00000100': (sendCommands, Keycode.TWO),
	'00000010': (sendCommands, Keycode.ONE),
	'00000001': (sendCommands, Keycode.O),

	# layer
	'01001010': 'navigation',
	'11001100': 'alpha',
}

navigation = {
	'10000000': (sendCommands, Keycode.PAGE_UP),
	'01000000': (sendCommands, Keycode.UP_ARROW),
	'00100000': (sendCommands, Keycode.PAGE_DOWN),
	'00010000': (sendCommands, Keycode.S),
	'00001000': (sendCommands, Keycode.RIGHT_ARROW),
	'00000100': (sendCommands, Keycode.DOWN_ARROW),
	'00000010': (sendCommands, Keycode.LEFT_ARROW),
	'00000001': (sendCommands, Keycode.O),

	# layer
	'11001100': 'alpha',
	'00110011': 'numeric',
}

layerset = {
	'alpha' : artseyio,
	'numeric' : numeric,
	'navigation': navigation
}
