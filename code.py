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

#Keys row and column pinout
keyboard.col_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define the macros for non standard keys
AT_SYMBOL = KC.MACRO('"')
GBP_SYMBOL = KC.MACRO('#')
BSL_SYMBOL = KC.MACRO('~')

#Keymap
keyboard.keymap = [
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.DEL, KC.NO, KC.NO,
     KC.N1, KC.N2, KC.ESC, KC.Q, KC.TAB, KC.A, KC.CAPS, KC.Z, KC.NO, KC.NO,
     KC.N4, KC.N3, KC.E, KC.W, KC.S, KC.D, KC.C, KC.X, KC.NO, KC.NO,
     KC.N6, KC.N5, KC.R, KC.T, KC.G, KC.F, KC.B, KC.V, KC.NO, KC.NO,
     KC.N8, KC.N7, KC.U, KC.Y, KC.H, KC.J, KC.N, KC.SPACE, KC.NO, KC.NO,
     KC.N0, KC.N9, KC.O, KC.I, KC.L, KC.K, KC.M, KC.COMMA, KC.NO, KC.NO,
     GBP_SYMBOL, KC.EQUAL, AT_SYMBOL, KC.P, KC.SCLN, KC.COLON, KC.SLSH, KC.DOT, KC.NO, KC.NO,
     KC.BSPC, KC.LBRC, KC.ENT, KC.RBRC, KC.F4, KC.LSFT, KC.PIPE, KC.LCTL, KC.NO, KC.NO,
     KC.LEFT, KC.LGUI, KC.F7, KC.F8, KC.F5, KC.F1, KC.F2, KC.MO(1), KC.NO, KC.NO,
     KC.UP, KC.RIGHT, KC.DOWN, KC.F9, KC.F6, KC.F3, KC.PENT, KC.PDOT, KC.NO, KC.NO],

     #Custom layer (when you press f0 key)
     [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.DEL, KC.NO, KC.NO,
     KC.EXCLAIM, KC.DOUBLE_QUOTE, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.DOLLAR, KC.NONUS_HASH, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.AMPERSAND, KC.PERCENT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.LPRN, KC.QUOTE, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.UNDERSCORE, KC.RPRN, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.CARET, KC.MINS, KC.PIPE, KC.PLUS, KC.NO, KC.ASTERISK, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],
]

if __name__ == '__main__':
    keyboard.go()
    