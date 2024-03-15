# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v3\control_surface\components\drum_group_scroll.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2582 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...live import liveobj_valid
from ..display import Renderable
from .page import Pageable, PageComponent
MAX_DRUM_GROUP_SCROLL_POSITION = 28

class DrumGroupScrollComponent(PageComponent, Pageable, Renderable):
    position_count = 32
    page_length = 4
    page_offset = 1

    def __init__(self, name='Drum_Group_Scroll', *a, **k):
        self._drum_group_device = None
        (super().__init__)(a, name=name, scroll_skin_name="DrumGroup.Scroll", **k)

    def set_scroll_encoder(self, encoder):
        self._position_scroll.set_scroll_encoder(encoder)

    def set_drum_group_device(self, drum_group_device):
        self._drum_group_device = drum_group_device
        self.update()

    @property
    def position(self):
        if liveobj_valid(self._drum_group_device):
            return self._drum_group_device.view.drum_pads_scroll_position
        return 0

    @position.setter
    def position(self, index):
        if liveobj_valid(self._drum_group_device):
            self._drum_group_device.view.drum_pads_scroll_position = index

    def can_scroll_page_up(self):
        if not liveobj_valid(self._drum_group_device):
            return False
        return super().can_scroll_page_up()

    def scroll_page_up(self):
        super().scroll_page_up()
        self.notify(self.notifications.DrumGroup.Page.up)

    def scroll_page_down(self):
        super().scroll_page_down()
        self.notify(self.notifications.DrumGroup.Page.down)

    def scroll_up(self):
        super().scroll_up()
        self.notify(self.notifications.DrumGroup.Scroll.up)

    def scroll_down(self):
        super().scroll_down()
        self.notify(self.notifications.DrumGroup.Scroll.down)

# okay decompiling ./MIDIRemoteScripts/ableton/v3/control_surface/components/drum_group_scroll.pyc
