# uncompyle6 version 3.9.1.dev0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
# [GCC 9.3.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Framework\LogicalDisplaySegment.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 2473 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object

class LogicalDisplaySegment(object):
    separator = ""

    def __init__(self, width=None, update_callback=None, *a, **k):
        (super(LogicalDisplaySegment, self).__init__)(*a, **k)
        self._update_callback = update_callback
        self._width = width
        self._position_identifier = ()
        self._data_source = None
        self._display_string = None

    def disconnect(self):
        self._update_callback = None
        self._position_identifier = None
        if self._data_source != None:
            self._data_source.set_update_callback(None)
            self._data_source = None

    def set_data_source(self, data_source):
        if self._data_source != None:
            self._data_source.set_update_callback(None)
        self._data_source = data_source
        if self._data_source != None:
            self._data_source.set_update_callback(self.update)
        self._display_string = self._get_display_string()

    def data_source(self):
        return self._data_source

    def set_position_identifier(self, position_identifier):
        self._position_identifier = position_identifier

    def position_identifier(self):
        return self._position_identifier

    def update(self):
        if self._update_callback:
            self._display_string = self._get_display_string()
            self._update_callback()

    def _get_display_string(self):
        if self._data_source != None:
            separator = self._data_source.separator + self.separator
            width = self._width - len(separator)
            return self._data_source.adjust_string(width) + separator
        return " " * int(self._width)

    def display_string(self):
        if self._display_string is None:
            self._display_string = self._get_display_string()
        return self._display_string

    def __str__(self):
        return self.display_string()

# okay decompiling ./MIDIRemoteScripts/_Framework/LogicalDisplaySegment.pyc
