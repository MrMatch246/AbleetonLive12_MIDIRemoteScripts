# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\settings.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 689 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.setting import OnOffSetting

def create_settings(preferences=None):
    preferences = preferences if preferences is not None else {}
    return {'workflow':OnOffSetting(name="Workflow",
       value_labels=[
      "Scene", "Clip"],
       default_value=True,
       preferences=preferences), 
     'aftertouch_mode':OnOffSetting(name="Pressure",
       value_labels=[
      "Mono", "Polyphonic"],
       default_value=True,
       preferences=preferences)}

# okay decompiling ./MIDIRemoteScripts/Push2/settings.pyc
