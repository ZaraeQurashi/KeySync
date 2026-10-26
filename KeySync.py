# KeySync MIDI Controller
# 7 capacitive touch keys, 2 switches, 1 rotary encoder
# Board: Seeed Studio XIAO ESP32-S3

import keypad
import touchio
from microcontroller import pin

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.midi import MidiKeys
from kmk.scanners import Scanner
from kmk.scanners.keypad import KeysScanner


# Custom scanner for capacitive touch pads
class TouchScanner(Scanner):
    def __init__(self, pins):
        self.pads = [touchio.TouchIn(p) for p in pins]
        self.pressed = [False] * len(pins)

    @property
    def key_count(self):
        return len(self.pads)

    def scan_for_changes(self):
        for i, pad in enumerate(self.pads):
            touched = pad.value

            if touched != self.pressed[i]:
                self.pressed[i] = touched
                return keypad.Event(i + self.offset, touched)

        return None


# Initialize keyboard and extensions
keyboard = KMKKeyboard()

midi = MidiKeys()
media_keys = MediaKeys()


# Input configuration
keyboard.matrix = [
    # 7 capacitive touch pads: GPIO3-GPIO9
    TouchScanner([
        pin.GPIO3,
        pin.GPIO4,
        pin.GPIO5,
        pin.GPIO6,
        pin.GPIO7,
        pin.GPIO8,
        pin.GPIO9,
    ]),

    # 2 physical switches: GPIO43 and GPIO44
    KeysScanner(
        [pin.GPIO43, pin.GPIO44],
        value_when_pressed=False,
        pull=True,
    ),
]


# Key mappings
keyboard.keymap = [[
    # Touch pads: C major scale
    KC.MIDI_NOTE(60),  # C4
    KC.MIDI_NOTE(62),  # D4
    KC.MIDI_NOTE(64),  # E4
    KC.MIDI_NOTE(65),  # F4
    KC.MIDI_NOTE(67),  # G4
    KC.MIDI_NOTE(69),  # A4
    KC.MIDI_NOTE(71),  # B4

    # Switches: drum sounds
    KC.MIDI_NOTE(36),  # Kick drum
    KC.MIDI_NOTE(38),  # Snare drum
]]


# Rotary encoder: GPIO1 and GPIO2
encoder = EncoderHandler()

encoder.pins = (
    (pin.GPIO1, pin.GPIO2, None),
)

encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),
]

# Register modules and extensions
keyboard.modules = [
    midi,
    encoder,
]

keyboard.extensions = [
    media_keys,
]

# Start the controller
if __name__ == "__main__":
    keyboard.go()
