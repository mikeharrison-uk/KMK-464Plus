#AMSTRAD 464 PLUS firmware - Mike Harrison 2025
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.international import International
from kmk.modules.macros import Macros
import board

#Initialisation
keyboard = KMKKeyboard()
layers = Layers()
macros = Macros()
keyboard.modules.append(macros)
keyboard.debug_enabled = False
keyboard.modules.append(layers)
keyboard.extensions.append(International())

#Keys row and column pinout - change this to match the GPIO pins you have used on your board
keyboard.col_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define the macros for non standard keys - UK regional keyboard settings selected on OS
AT_SYMBOL = KC.MACRO('"')
GBP_SYMBOL = KC.MACRO('#')
HASH_SYMBOL = KC.MACRO('\\')

keyboard.keymap = [

    # AMSTRAD 464 Plus QWERTY (Layer 0)
    # ,-------------------------------------------------------------------------------------------------------------------------------.
    # |  ESC   |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  |   -  |   £  |  CLR |  DEL |  f7  |  f8  |  f9  |
    # |--------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------|
    # |  TAB   |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |   @  |   [  |   RETURN    |  f4  |  f5  |  f6  |
    # |--------+------+------+------+------+-------------+------+------+------+------+------+------+             +------+------+------|
    # |  CAPS  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   :  |   ;  |   ]  |             |  f1  |  f2  |  f3  |
    # |--------+------+------+------+------+------+------+------+------+------+------+------+------+-------------+------+------+------|
    # |  SHIFT |   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |   /  |   \  | #####|    SHIFT    |  f0  |  UP  |   .  |
    # |--------+------+------+------+------+------+------+------+------+------+------+------+------+-------------+------+------+------|
    # | CONTROL| COPY |                               SPACE                                        |    ENTER    | LEFT | DOWN | RIGHT|
    # `--------------------------------------------------------------------------------------------+-------------+------+------+------'

    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.DEL,
     KC.NO, KC.N1, KC.N2, KC.ESC, KC.Q, KC.TAB, KC.A, KC.CAPS, KC.Z, KC.NO,
     KC.NO, KC.N4, KC.N3, KC.E, KC.W, KC.S, KC.D, KC.C, KC.X, KC.NO,
     KC.NO, KC.N6, KC.N5, KC.R, KC.T, KC.G, KC.F, KC.B, KC.V, KC.NO,
     KC.NO, KC.N8, KC.N7, KC.U, KC.Y, KC.H, KC.J, KC.N, KC.SPACE, KC.NO,
     KC.NO, KC.N0, KC.N9, KC.O, KC.I, KC.L, KC.K, KC.M, KC.COMMA, KC.NO,
     KC.NO, KC.LSFT(KC.N6), KC.MINUS, AT_SYMBOL, KC.P, KC.SCLN, KC.COLON, KC.SLSH, KC.DOT, KC.NO,
     KC.NO, KC.BSPC, KC.LBRC, KC.ENT, KC.RBRC, KC.F4, KC.MO(1), KC.NONUS_BSLASH, KC.LCTL, KC.NO,
     KC.NO, KC.LEFT, KC.LCTL(KC.C), KC.F7, KC.F8, KC.F5, KC.F1, KC.F2, KC.F10, KC.NO,
     KC.NO, KC.UP, KC.RIGHT, KC.DOWN, KC.F9, KC.F6, KC.F3, KC.PENT, KC.PDOT, KC.NO],
    

    # AMSTRAD 464 Plus SHIFTED enabling non-standard special character mappings (Layer 1)
    # ,-------------------------------------------------------------------------------------------------------------------------------.
    # |        |   !  |   "  |   #  |   $  |   %  |   &  |   '  |   (  |   )  |   _  |   =  |   ^  |      |      |      |  UP  |      |
    # |--------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------|
    # |        |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  |   |  |   {  |   RETURN    | LEFT | DOWN | RIGHT|
    # |--------+------+------+------+------+-------------+------+------+------+------+------+------+             +------+------+------|
    # |        |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   *  |   +  |   }  |             |      |      |      |
    # |--------+------+------+------+------+------+------+------+------+------+------+------+------+-------------+------+------+------|
    # |        |   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   <  |   >  |   ?  |   '  |      |             |      |      |      |
    # |--------+------+------+------+------+------+------+------+------+------+------+------+------+-------------+------+------+------|
    # |        | GUI  |                                                                            |    ENTER    |      |      |      |
    # `--------------------------------------------------------------------------------------------+-------------+------+------+------'

    [KC.NO,KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.DEL,
     KC.NO, KC.EXCLAIM, KC.AT, KC.NO, KC.LSFT(KC.Q), KC.NO, KC.LSFT(KC.A), KC.NO, KC.LSFT(KC.Z), KC.NO,
     KC.NO, KC.DOLLAR, KC.NONUS_HASH, KC.LSFT(KC.E), KC.LSFT(KC.W), KC.LSFT(KC.S), KC.LSFT(KC.D), KC.LSFT(KC.C), KC.LSFT(KC.X), KC.NO,
     KC.NO, KC.AMPERSAND, KC.PERCENT, KC.LSFT(KC.R), KC.LSFT(KC.T), KC.LSFT(KC.G), KC.LSFT(KC.F), KC.LSFT(KC.B), KC.LSFT(KC.V), KC.NO,
     KC.NO, KC.LPRN, KC.QUOTE, KC.LSFT(KC.U), KC.LSFT(KC.Y), KC.LSFT(KC.H), KC.LSFT(KC.J), KC.LSFT(KC.N), KC.NO, KC.NO,
     KC.NO, KC.UNDERSCORE, KC.RPRN, KC.LSFT(KC.O), KC.LSFT(KC.I), KC.LSFT(KC.L), KC.LSFT(KC.K), KC.LSFT(KC.M), KC.LSFT(KC.COMMA), KC.NO,
     KC.NO, GBP_SYMBOL, KC.EQUAL, KC.LSFT(KC.NONUS_BSLASH), KC.LSFT(KC.P), KC.LSFT(KC.EQUAL), KC.LSFT(KC.N8), KC.LSFT(KC.SLSH), KC.LSFT(KC.DOT), KC.NO,
     KC.NO, KC.NO, KC.LSFT(KC.LBRC), KC.LSFT(KC.ENT), KC.LSFT(KC.RBRC), KC.LEFT, KC.NO, KC.GRAVE, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.LGUI, KC.NO, KC.UP, KC.DOWN, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO],
]

if __name__ == '__main__':
    keyboard.go()
