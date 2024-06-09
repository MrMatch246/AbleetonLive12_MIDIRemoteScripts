# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\scene.py
# Size of source mod 2**32: 5325 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import depends, listens
from ...live import action, display_name, liveobj_changed, liveobj_valid, scene_index
from .. import Component
from ..controls import ButtonControl
from ..display import Renderable
from ..skin import LiveObjSkinEntry
from . import ClipSlotComponent

class SceneComponent(Component, Renderable):
    launch_button = ButtonControl()
    select_button = ButtonControl(color=None)
    delete_button = ButtonControl(color=None)
    duplicate_button = ButtonControl(color=None)
    include_in_top_level_state = False

    @depends(session_ring=None)
    def __init__(self, session_ring=None, clip_slot_component_type=None, *a, **k):
        (super().__init__)(*a, **k)
        self._session_ring = session_ring
        self._scene = None
        clip_slot_component_type = clip_slot_component_type or ClipSlotComponent
        self._clip_slots = [clip_slot_component_type(parent=self) for _ in range(session_ring.num_tracks)]
        self.register_slot(session_ring, self._reassign_clip_slots, "tracks")

    @property
    def scene(self):
        return self._scene

    def set_scene(self, scene):
        if liveobj_changed(scene, self._scene):
            self._scene = scene
            self._SceneComponent__on_is_triggered_changed.subject = scene
            self._SceneComponent__on_scene_color_changed.subject = scene
            self.update()

    def clip_slot(self, index):
        return self._clip_slots[index]

    def set_launch_button(self, button):
        self.launch_button.set_control_element(button)
        self.update()

    @launch_button.pressed
    def launch_button(self, _):
        self._on_launch_button_pressed()

    def _on_launch_button_pressed(self):
        scene_name = display_name(self._scene) if liveobj_valid(self._scene) else ""
        if self.select_button.is_pressed:
            if action.select(self._scene):
                self.notify(self.notifications.Scene.select, scene_name)
        elif self.duplicate_button.is_pressed:
            if action.duplicate(self._scene):
                self.notify(self.notifications.Scene.duplicate, scene_name)
        elif self.delete_button.is_pressed:
            if action.delete(self._scene):
                self.notify(self.notifications.Scene.delete, scene_name)
        else:
            self._do_launch_scene()

    def _do_launch_scene(self):
        action.fire((self._scene), button_state=True)

    @launch_button.released
    def launch_button(self, _):
        self._on_launch_button_released()

    def _on_launch_button_released(self):
        if self.launch_button.is_momentary:
            if not self._any_modifier_pressed():
                action.fire((self._scene), button_state=False)

    def _any_modifier_pressed(self):
        return self.select_button.is_pressed or self.delete_button.is_pressed or self.duplicate_button.is_pressed

    def update(self):
        super().update()
        self._reassign_clip_slots()
        self._update_launch_button_color()

    def _update_launch_button_color(self):
        value_to_send = "Session.NoScene"
        if liveobj_valid(self._scene):
            value_to_send = self._feedback_value()
        self.launch_button.color = value_to_send

    def _feedback_value(self):
        value = "Session.Scene"
        if self._scene.is_triggered:
            value = "Session.SceneTriggered"
        return LiveObjSkinEntry(value, self._scene)

    def _reassign_clip_slots(self):
        if liveobj_valid(self._scene) and self.is_enabled():
            scene_offset = scene_index(self._scene)
            regular_tracks = self.song.tracks
            for (slot_wrapper, track) in zip(self._clip_slots, self._session_ring.tracks):
                if track in regular_tracks:
                    slot_wrapper.set_clip_slot(track.clip_slots[scene_offset])
                else:
                    slot_wrapper.set_non_player_track(track)

        else:
            for slot in self._clip_slots:
                slot.set_clip_slot(None)

    @listens("is_triggered")
    def __on_is_triggered_changed(self):
        self._update_launch_button_color()

    @listens("color")
    def __on_scene_color_changed(self):
        self._update_launch_button_color()

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/components/scene.pyc
