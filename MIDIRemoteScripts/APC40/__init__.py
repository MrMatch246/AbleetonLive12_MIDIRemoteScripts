# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\APC40\__init__.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 690 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .APC40 import APC40

def create_instance(c_instance):
    return APC40(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=2536,
                          product_ids=[115],
                          model_name="Akai APC40")), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT, REMOTE]),
                 outport(props=[SCRIPT, REMOTE])]}

# okay decompiling ./MIDIRemoteScripts/APC40/__init__.pyc
