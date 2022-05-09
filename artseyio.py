import time
import board
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from layers import layerset
from layers import mods

# globals
bitChar = {False: '1', True: '0'}
defaultLayer = 'alpha'

# define output LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# flash the LED when booting
for x in range(0, 5):
	led.value = False
	time.sleep(0.2)
	led.value = True
	time.sleep(0.2)

# configure device as keyboard
print('Keyboard ready...')

def initializePin(pin):
	tmp = DigitalInOut(pin)
	tmp.switch_to_input(pull=Pull.UP)
	return tmp

# pins should follow ARTSEYIO sequence
pins = (board.D10,  board.D9,  board.D3,  board.D4, board.D7, board.D8, board.D5, board.D6)
macropad = [initializePin(pin) for pin in pins]

while True:
	tmpStr = [str(bitChar.get(ky.value)) for ky in macropad]
	
	if '1' in tmpStr:
		keystring = ''.join([str(item) for item in tmpStr])
		comboCode = (layerset.get(defaultLayer)).get(keystring)
		if  isinstance(comboCode, str) :
			defaultLayer = comboCode
		elif comboCode:
			(comboCode[0])(comboCode[1])
		else:
			print('Undefined')

	time.sleep(0.1)