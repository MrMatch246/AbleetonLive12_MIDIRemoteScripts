# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_AIR_Mini32\EncoderMixerModeSelector.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1491 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import _Framework.ModeSelectorComponent as ModeSelectorComponent

class EncoderMixerModeSelector(ModeSelectorComponent):

    def __init__(self, mixer):
        ModeSelectorComponent.__init__(self)
        self._mixer = mixer
        self._controls = None

    def disconnect(self):
        self._mixer = None
        self._controls = None
        ModeSelectorComponent.disconnect(self)

    def set_mode_toggle(self, button):
        ModeSelectorComponent.set_mode_toggle(self, button)
        self.set_mode(0)

    def set_controls(self, controls):
        self._controls = controls
        self.update()

    def number_of_modes(self):
        return 2

    def update(self):
        super(EncoderMixerModeSelector, self).update()
        if self.is_enabled():
            if self._controls != None:
                mode = self._mode_index
                for index in range(len(self._controls)):
                    strip = self._mixer.channel_strip(index)
                    if mode == 0:
                        strip.set_pan_control(None)
                        strip.set_volume_control(self._controls[index])
                    elif mode == 1:
                        strip.set_volume_control(None)
                        strip.set_pan_control(self._controls[index])

# okay decompiling ./MIDIRemoteScripts/Axiom_AIR_Mini32/EncoderMixerModeSelector.pyc
