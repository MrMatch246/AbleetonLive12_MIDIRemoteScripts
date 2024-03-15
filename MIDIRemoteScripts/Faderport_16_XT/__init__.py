# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Faderport_16_XT\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 777 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from MackieControlXT import MackieControlXT

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=6479,
                          product_ids=[516],
                          model_name=["PreSonus FP16"])), 
     
     PORTS_KEY: [
                 inport(props=[]),
                 inport(props=[SCRIPT, REMOTE]),
                 outport(props=[]),
                 outport(props=[SCRIPT, REMOTE])]}


def create_instance(c_instance):
    return MackieControlXT(c_instance)

# okay decompiling ./MIDIRemoteScripts/Faderport_16_XT/__init__.pyc
