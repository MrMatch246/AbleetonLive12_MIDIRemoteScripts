# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\iRig_Keys_IO\skin.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 708 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color

class Colors(object):

    class DefaultButton(object):
        On = Color(0)
        Off = Color(0)
        Disabled = Color(0)

    class Transport(object):
        PlayOn = Color(0)
        PlayOff = Color(0)

    class Recording(object):
        On = Color(0)
        Off = Color(0)

    class Mixer(object):
        MuteOff = Color(127)
        MuteOn = Color(0)
        SoloOn = Color(127)
        SoloOff = Color(0)


skin = Skin(Colors)

# okay decompiling ./MIDIRemoteScripts/iRig_Keys_IO/skin.pyc
