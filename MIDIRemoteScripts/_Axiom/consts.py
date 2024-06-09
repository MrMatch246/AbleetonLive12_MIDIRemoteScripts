# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Axiom\consts.py
# Size of source mod 2**32: 2237 bytes
from __future__ import absolute_import, print_function, unicode_literals
NOTE_OFF_STATUS = 128
NOTE_ON_STATUS = 144
CC_STATUS = 176
NUM_NOTES = 128
NUM_CC_NO = 128
NUM_CHANNELS = 16
EXP_PEDAL_CC = 11
SYSEX_BEGIN = (240, 126, 127, 6)
SYSEX_END = (247, )
ID_REQUEST = (1, )
ID_RESP_BEGIN = (2, 0, 32, 8, 99, 14)
ID_RESP_25 = 24
ID_RESP_49 = 25
ID_RESP_61 = 26
AXIOM_LOOP = 20
AXIOM_RWD = 21
AXIOM_FFWD = 22
AXIOM_STOP = 23
AXIOM_PLAY = 24
AXIOM_REC = 25
AXIOM_TRANSPORT = (AXIOM_LOOP, AXIOM_RWD, AXIOM_FFWD, AXIOM_STOP, AXIOM_PLAY, AXIOM_REC)
AXIOM_ENC1 = 102
AXIOM_ENC2 = 103
AXIOM_ENC3 = 104
AXIOM_ENC4 = 105
AXIOM_ENC5 = 106
AXIOM_ENC6 = 107
AXIOM_ENC7 = 108
AXIOM_ENC8 = 109
AXIOM_ENCODERS = (
 AXIOM_ENC1,
 AXIOM_ENC2,
 AXIOM_ENC3,
 AXIOM_ENC4,
 AXIOM_ENC5,
 AXIOM_ENC6,
 AXIOM_ENC7,
 AXIOM_ENC8)
AXIOM_SLI1 = 110
AXIOM_SLI2 = 111
AXIOM_SLI3 = 112
AXIOM_SLI4 = 113
AXIOM_SLI5 = 114
AXIOM_SLI6 = 115
AXIOM_SLI7 = 116
AXIOM_SLI8 = 117
AXIOM_SLI9 = 118
AXIOM_SLIDERS = (
 AXIOM_SLI1,
 AXIOM_SLI2,
 AXIOM_SLI3,
 AXIOM_SLI4,
 AXIOM_SLI5,
 AXIOM_SLI6,
 AXIOM_SLI7,
 AXIOM_SLI8)
AXIOM_BUT1 = 52
AXIOM_BUT2 = 53
AXIOM_BUT3 = 54
AXIOM_BUT4 = 55
AXIOM_BUT5 = 56
AXIOM_BUT6 = 57
AXIOM_BUT7 = 58
AXIOM_BUT8 = 59
AXIOM_BUT9 = 60
AXIOM_BUTTONS = (
 AXIOM_BUT1,
 AXIOM_BUT2,
 AXIOM_BUT3,
 AXIOM_BUT4,
 AXIOM_BUT5,
 AXIOM_BUT6,
 AXIOM_BUT7,
 AXIOM_BUT8,
 AXIOM_BUT9)
AXIOM_PAD1 = 80
AXIOM_PAD2 = 81
AXIOM_PAD3 = 82
AXIOM_PAD4 = 83
AXIOM_PAD5 = 85
AXIOM_PAD6 = 86
AXIOM_PAD7 = 87
AXIOM_PAD8 = 88
AXIOM_PADS = (
 AXIOM_PAD1,
 AXIOM_PAD2,
 AXIOM_PAD3,
 AXIOM_PAD4,
 AXIOM_PAD5,
 AXIOM_PAD6,
 AXIOM_PAD7,
 AXIOM_PAD8)
PAD_TRANSLATION = ((0, 2, 67, 9), (1, 2, 69, 9), (2, 2, 71, 9), (3, 2, 72, 9), (0, 3, 60, 9),
                   (1, 3, 62, 9), (2, 3, 64, 9), (3, 3, 65, 9))

# okay decompiling ./MIDIRemoteScripts/_Axiom/consts.pyc
