# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ATOMSQ\skin.py
# Size of source mod 2**32: 1503 bytes
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from .colors import Rgb, create_color_for_liveobj

class Skin:

    class DefaultButton:
        On = Rgb.ON
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class Transport:
        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_DIM
        LoopOn = Rgb.GREEN
        LoopOff = Rgb.GREEN_DIM

    class Mixer:
        Selected = Rgb.ON
        NotSelected = Rgb.OFF

    class Session:
        Slot = Rgb.OFF
        SlotRecordButton = Rgb.RED_HALF
        NoSlot = Rgb.OFF
        ClipStopped = create_color_for_liveobj
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipPlaying = Rgb.GREEN_PULSE
        ClipRecording = Rgb.RED_PULSE
        Scene = partial(create_color_for_liveobj, is_scene=True)
        SceneTriggered = Rgb.GREEN_BLINK
        NoScene = Rgb.OFF
        StopClipTriggered = Rgb.RED_BLINK
        StopClip = Rgb.RED
        StopClipDisabled = Rgb.RED_HALF

    class ViewToggle:
        DetailOn = Rgb.YELLOW
        DetailOff = Rgb.YELLOW_HALF
        SessionOn = Rgb.BLUE
        SessionOff = Rgb.BLUE_HALF
        ClipOn = Rgb.PURPLE
        ClipOff = Rgb.PURPLE_HALF
        BrowserOn = Rgb.GREEN
        BrowserOff = Rgb.GREEN_HALF

    class LowerPadModes:

        class Select:
            On = Rgb.RED_HALF

        class Stop:
            On = Rgb.RED

# okay decompiling ./MIDIRemoteScripts/ATOMSQ/skin.pyc
