# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\APC_Key_25_mk2\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 1409 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import ControlSurfaceSpecification, create_control_surface, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, HIDDEN, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, controller_id, inport, outport
from .colors import Rgb, Skin
from .elements import Elements
from .mappings import create_mappings

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[78],
                          model_name=["APC Key 25 mk2"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[NOTES_CC]),
                 outport(props=[NOTES_CC, SCRIPT, SYNC, HIDDEN])]}


def create_instance(c_instance):
    return create_control_surface(name="APC_Key_25_mk2",
      specification=Specification,
      c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin, colors=Rgb)
    num_tracks = 8
    num_scenes = 5
    include_returns = True
    identity_response_id_bytes = (71, 78, 0, 25)
    create_mappings_function = create_mappings

# okay decompiling ./MIDIRemoteScripts/APC_Key_25_mk2/__init__.pyc
