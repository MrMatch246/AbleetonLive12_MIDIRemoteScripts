# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Axiom_25_Classic\Axiom.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 9343 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range, str
import Live, MidiRemoteScript
from _Generic.util import DeviceAppointer
from _Axiom.consts import *
import _Axiom.Encoders as Encoders
import _Axiom.Pads as Pads
import _Axiom.Transport as Transport

class Axiom(object):

    def __init__(self, c_instance):
        self._Axiom__c_instance = c_instance
        self._Axiom__current_track = self.song().view.selected_track
        self._Axiom__current_device = self._Axiom__current_track.view.selected_device
        self.song().add_visible_tracks_listener(self._Axiom__tracks_changed)
        self._Axiom__transport_unit = Transport(self)
        self._Axiom__encoder_unit = Encoders(self, False)
        self._Axiom__pad_unit = Pads(self)
        self._device_appointer = DeviceAppointer(song=(self.song()),
          appointed_device_setter=(self._set_appointed_device))

    def application(self):
        return Live.Application.get_application()

    def song(self):
        return self._Axiom__c_instance.song()

    def disconnect(self):
        self.song().remove_visible_tracks_listener(self._Axiom__tracks_changed)
        self._device_appointer.disconnect()
        self._Axiom__encoder_unit.disconnect()

    def can_lock_to_devices(self):
        return True

    def suggest_input_port(self):
        return str("USB Axiom 25")

    def suggest_output_port(self):
        return str("USB Axiom 25")

    def suggest_map_mode(self, cc_no, channel):
        suggested_map_mode = Live.MidiMap.MapMode.absolute
        if cc_no in AXIOM_ENCODERS:
            suggested_map_mode = Live.MidiMap.MapMode.relative_smooth_binary_offset
        return suggested_map_mode

    def show_message(self, message):
        self._Axiom__c_instance.show_message(message)

    def supports_pad_translation(self):
        return True

    def connect_script_instances(self, instanciated_scripts):
        pass

    def request_rebuild_midi_map(self):
        self._Axiom__c_instance.request_rebuild_midi_map()

    def send_midi(self, midi_event_bytes):
        self._Axiom__c_instance.send_midi(midi_event_bytes)

    def refresh_state(self):
        pass

    def build_midi_map(self, midi_map_handle):
        script_handle = self._Axiom__c_instance.handle()
        for channel in range(4):
            Live.MidiMap.forward_midi_cc(script_handle, midi_map_handle, channel, EXP_PEDAL_CC)

        self._Axiom__transport_unit.build_midi_map(script_handle, midi_map_handle)
        self._Axiom__encoder_unit.build_midi_map(script_handle, midi_map_handle)
        self._Axiom__pad_unit.build_midi_map(script_handle, midi_map_handle)
        self._Axiom__c_instance.set_pad_translation(PAD_TRANSLATION)

    def update_display(self):
        if self._Axiom__transport_unit:
            self._Axiom__transport_unit.refresh_state()

    def receive_midi(self, midi_bytes):
        if midi_bytes[0] & 240 == CC_STATUS:
            channel = midi_bytes[0] & 15
            cc_no = midi_bytes[1]
            cc_value = midi_bytes[2]
            if list(AXIOM_TRANSPORT).count(cc_no) > 0:
                self._Axiom__transport_unit.receive_midi_cc(cc_no, cc_value)
            elif list(AXIOM_ENCODERS).count(cc_no) > 0:
                self._Axiom__encoder_unit.receive_midi_cc(cc_no, cc_value, channel)
            elif list(AXIOM_PADS).count(cc_no) > 0:
                self._Axiom__pad_unit.receive_midi_cc(cc_no, cc_value, channel)
            elif cc_no == EXP_PEDAL_CC:
                self._Axiom__encoder_unit.set_modifier(cc_value == 0)
                self.request_rebuild_midi_map()
        elif midi_bytes[0] == 240:
            pass

    def lock_to_device(self, device):
        self._Axiom__encoder_unit.lock_to_device(device)

    def unlock_from_device(self, device):
        self._Axiom__encoder_unit.unlock_from_device(device)

    def _set_appointed_device(self, device):
        self._Axiom__encoder_unit.set_appointed_device(device)

    def __tracks_changed(self):
        self.request_rebuild_midi_map()

    def bank_changed(self, new_bank):
        if self._Axiom__encoder_unit.set_bank(new_bank):
            self.request_rebuild_midi_map()

    def restore_bank(self, bank):
        self._Axiom__encoder_unit.restore_bank(bank)
        self.request_rebuild_midi_map()

    def instance_identifier(self):
        return self._Axiom__c_instance.instance_identifier()

# okay decompiling ./MIDIRemoteScripts/Axiom_25_Classic/Axiom.pyc
