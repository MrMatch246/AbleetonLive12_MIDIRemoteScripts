# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MPD218\MPD218.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 417 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _MPDMkIIBase.MPDMkIIBase as MPDMkIIBase
PAD_CHANNEL = 9
PAD_IDS = [
 [
  48, 49, 50, 51], [44, 45, 46, 47], [40, 41, 42, 43], [36, 37, 38, 39]]

class MPD218(MPDMkIIBase):

    def __init__(self, *a, **k):
        (super(MPD218, self).__init__)(PAD_IDS, PAD_CHANNEL, *a, **k)

# okay decompiling ./MIDIRemoteScripts/MPD218/MPD218.pyc
