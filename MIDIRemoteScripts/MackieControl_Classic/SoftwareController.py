# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MackieControl_Classic\SoftwareController.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 12339 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .MackieControlComponent import *

class SoftwareController(MackieControlComponent):

    def __init__(self, main_script):
        MackieControlComponent.__init__(self, main_script)
        self._SoftwareController__last_can_undo_state = False
        self._SoftwareController__last_can_redo_state = False
        av = self.application().view
        av.add_is_view_visible_listener("Session", self._SoftwareController__update_session_arranger_button_led)
        av.add_is_view_visible_listener("Detail/Clip", self._SoftwareController__update_detail_sub_view_button_led)
        av.add_is_view_visible_listener("Browser", self._SoftwareController__update_browser_button_led)
        av.add_is_view_visible_listener("Detail", self._SoftwareController__update_detail_button_led)
        self.song().view.add_draw_mode_listener(self._SoftwareController__update_draw_mode_button_led)
        self.song().view.add_follow_song_listener(self._SoftwareController__update_follow_song_button_led)
        self.song().add_back_to_arranger_listener(self._SoftwareController__update_back_to_arranger_button_led)

    def destroy(self):
        av = self.application().view
        av.remove_is_view_visible_listener("Session", self._SoftwareController__update_session_arranger_button_led)
        av.remove_is_view_visible_listener("Detail/Clip", self._SoftwareController__update_detail_sub_view_button_led)
        av.remove_is_view_visible_listener("Browser", self._SoftwareController__update_browser_button_led)
        av.remove_is_view_visible_listener("Detail", self._SoftwareController__update_detail_button_led)
        self.song().view.remove_draw_mode_listener(self._SoftwareController__update_draw_mode_button_led)
        self.song().view.remove_follow_song_listener(self._SoftwareController__update_follow_song_button_led)
        self.song().remove_back_to_arranger_listener(self._SoftwareController__update_back_to_arranger_button_led)
        for note in software_controls_switch_ids:
            self.send_midi((NOTE_ON_STATUS, note, BUTTON_STATE_OFF))

        for note in function_key_control_switch_ids:
            self.send_midi((NOTE_ON_STATUS, note, BUTTON_STATE_OFF))

        MackieControlComponent.destroy(self)

    def handle_function_key_switch_ids(self, switch_id, value):
        pass

    def handle_software_controls_switch_ids(self, switch_id, value):
        if switch_id == SID_MOD_SHIFT:
            self.main_script().set_shift_is_pressed(value == BUTTON_PRESSED)
        else:
            if switch_id == SID_MOD_OPTION:
                self.main_script().set_option_is_pressed(value == BUTTON_PRESSED)
            else:
                if switch_id == SID_MOD_CTRL:
                    self.main_script().set_control_is_pressed(value == BUTTON_PRESSED)
                else:
                    if switch_id == SID_MOD_ALT:
                        self.main_script().set_alt_is_pressed(value == BUTTON_PRESSED)
                    else:
                        if switch_id == SID_AUTOMATION_ON:
                            if value == BUTTON_PRESSED:
                                self._SoftwareController__toggle_session_arranger_is_visible()
                        else:
                            if switch_id == SID_AUTOMATION_RECORD:
                                if value == BUTTON_PRESSED:
                                    self._SoftwareController__toggle_detail_sub_view()
                            else:
                                if switch_id == SID_AUTOMATION_SNAPSHOT:
                                    if value == BUTTON_PRESSED:
                                        self._SoftwareController__toggle_browser_is_visible()
                                else:
                                    if switch_id == SID_AUTOMATION_TOUCH:
                                        if value == BUTTON_PRESSED:
                                            self._SoftwareController__toggle_detail_is_visible()
                                    else:
                                        if switch_id == SID_FUNC_UNDO:
                                            if value == BUTTON_PRESSED:
                                                self.song().undo()
                                        elif switch_id == SID_FUNC_REDO:
                                            if value == BUTTON_PRESSED:
                                                self.song().redo()
                                        elif switch_id == SID_FUNC_CANCEL:
                                            if value == BUTTON_PRESSED:
                                                self._SoftwareController__toggle_back_to_arranger()
                                        elif switch_id == SID_FUNC_ENTER:
                                            if value == BUTTON_PRESSED:
                                                self._SoftwareController__toggle_draw_mode()
                                        elif switch_id == SID_FUNC_MARKER:
                                            if value == BUTTON_PRESSED:
                                                self.song().set_or_delete_cue()
                                        elif switch_id == SID_FUNC_MIXER:
                                            if value == BUTTON_PRESSED:
                                                self._SoftwareController__toggle_follow_song()

    def refresh_state(self):
        self.main_script().set_shift_is_pressed(False)
        self.main_script().set_option_is_pressed(False)
        self.main_script().set_control_is_pressed(False)
        self.main_script().set_alt_is_pressed(False)
        self._SoftwareController__update_session_arranger_button_led()
        self._SoftwareController__update_detail_sub_view_button_led()
        self._SoftwareController__update_browser_button_led()
        self._SoftwareController__update_detail_button_led()
        self._SoftwareController__update_follow_song_button_led()
        self._SoftwareController__update_undo_button_led()
        self._SoftwareController__update_redo_button_led()
        self._SoftwareController__update_draw_mode_button_led()
        self._SoftwareController__update_back_to_arranger_button_led()

    def on_update_display_timer(self):
        if self._SoftwareController__last_can_undo_state != self.song().can_undo:
            self._SoftwareController__last_can_undo_state = self.song().can_undo
            self._SoftwareController__update_undo_button_led()
        if self._SoftwareController__last_can_redo_state != self.song().can_redo:
            self._SoftwareController__last_can_redo_state = self.song().can_redo
            self._SoftwareController__update_redo_button_led()

    def __toggle_session_arranger_is_visible(self):
        if self.application().view.is_view_visible("Session"):
            if self.shift_is_pressed():
                self.application().view.focus_view("Session")
            else:
                self.application().view.hide_view("Session")
        elif self.shift_is_pressed():
            self.application().view.focus_view("Arranger")
        else:
            self.application().view.hide_view("Arranger")

    def __toggle_detail_sub_view(self):
        if self.application().view.is_view_visible("Detail/Clip"):
            if self.shift_is_pressed():
                self.application().view.focus_view("Detail/Clip")
            else:
                self.application().view.show_view("Detail/DeviceChain")
        elif self.shift_is_pressed():
            self.application().view.focus_view("Detail/DeviceChain")
        else:
            self.application().view.show_view("Detail/Clip")

    def __toggle_browser_is_visible(self):
        if self.application().view.is_view_visible("Browser"):
            if self.shift_is_pressed():
                self.application().view.focus_view("Browser")
            else:
                self.application().view.hide_view("Browser")
        else:
            self.application().view.show_view("Browser")

    def __toggle_detail_is_visible(self):
        if self.application().view.is_view_visible("Detail"):
            if self.shift_is_pressed():
                self.application().view.focus_view("Detail")
            else:
                self.application().view.hide_view("Detail")
        else:
            self.application().view.show_view("Detail")

    def __toggle_back_to_arranger(self):
        self.song().back_to_arranger = not self.song().back_to_arranger

    def __toggle_draw_mode(self):
        self.song().view.draw_mode = not self.song().view.draw_mode

    def __toggle_follow_song(self):
        self.song().view.follow_song = not self.song().view.follow_song

    def __update_session_arranger_button_led(self):
        if self.application().view.is_view_visible("Session"):
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_ON, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_ON, BUTTON_STATE_OFF))

    def __update_detail_sub_view_button_led(self):
        if self.application().view.is_view_visible("Detail/Clip"):
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_RECORD, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_RECORD, BUTTON_STATE_OFF))

    def __update_browser_button_led(self):
        if self.application().view.is_view_visible("Browser"):
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_SNAPSHOT, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_SNAPSHOT, BUTTON_STATE_OFF))

    def __update_detail_button_led(self):
        if self.application().view.is_view_visible("Detail"):
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_TOUCH, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_AUTOMATION_TOUCH, BUTTON_STATE_OFF))

    def __update_follow_song_button_led(self):
        if self.song().view.follow_song:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_MIXER, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_MIXER, BUTTON_STATE_OFF))

    def __update_undo_button_led(self):
        if self.song().can_undo:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_UNDO, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_UNDO, BUTTON_STATE_OFF))

    def __update_redo_button_led(self):
        if self.song().can_redo:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_REDO, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_REDO, BUTTON_STATE_OFF))

    def __update_back_to_arranger_button_led(self):
        if self.song().back_to_arranger:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_CANCEL, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_CANCEL, BUTTON_STATE_OFF))

    def __update_draw_mode_button_led(self):
        if self.song().view.draw_mode:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_ENTER, BUTTON_STATE_ON))
        else:
            self.send_midi((NOTE_ON_STATUS, SID_FUNC_ENTER, BUTTON_STATE_OFF))

# okay decompiling ./MIDIRemoteScripts/MackieControl_Classic/SoftwareController.pyc
