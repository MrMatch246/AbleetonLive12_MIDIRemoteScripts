# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchpad_Pro\ActionsComponent.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 3016 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Control import ButtonControl, ToggleButtonControl
import _Framework.ControlSurfaceComponent as ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot
import _Framework.ToggleComponent as ToggleComponent
from _Framework.Util import BooleanContext
from .consts import ACTION_BUTTON_COLORS
RecordingQuantization = Live.Song.RecordingQuantization

class ActionsComponent(ControlSurfaceComponent):
    undo_button = ButtonControl(**ACTION_BUTTON_COLORS)
    redo_button = ButtonControl(color="Misc.Shift",
      pressed_color="Misc.ShiftOn",
      disabled_color="DefaultButton.Disabled")
    quantization_on_button = ToggleButtonControl(untoggled_color="Misc.Shift",
      toggled_color="Misc.ShiftOn")

    def __init__(self, *a, **k):
        self.suppressing_control_notifications = BooleanContext()
        (super(ActionsComponent, self).__init__)(*a, **k)
        self._record_quantization = RecordingQuantization.rec_q_sixtenth
        self._on_record_quantization_changed_in_live.subject = self.song()
        self._on_record_quantization_changed_in_live()
        self._metronome_toggle = ToggleComponent("metronome", self.song())

    def control_notifications_enabled(self):
        return self.is_enabled() and not self.suppressing_control_notifications

    def quantize_clip(self, clip):
        clip.quantize(self._record_quantization, 1.0)

    @undo_button.pressed
    def undo_button(self, button):
        if self.song().can_undo:
            self.song().undo()

    @redo_button.pressed
    def redo_button(self, button):
        if self.song().can_redo:
            self.song().redo()

    @quantization_on_button.toggled
    def quantization_on_button(self, is_toggled, button):
        self._record_quantization_on = is_toggled
        self.song().midi_recording_quantization = self._record_quantization if self._record_quantization_on else RecordingQuantization.rec_q_no_q

    @subject_slot("midi_recording_quantization")
    def _on_record_quantization_changed_in_live(self):
        quant_value = self.song().midi_recording_quantization
        quant_on = quant_value != RecordingQuantization.rec_q_no_q
        if quant_on:
            self._record_quantization = quant_value
        self._record_quantization_on = quant_on
        with self.suppressing_control_notifications():
            self.quantization_on_button.is_toggled = quant_on

    def set_metronome_button(self, button):
        self._metronome_toggle.set_toggle_button(button)

    def update(self):
        super(ActionsComponent, self).update()
        self._metronome_toggle.update()

# okay decompiling ./MIDIRemoteScripts/Launchpad_Pro/ActionsComponent.pyc
