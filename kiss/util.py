#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python KISS Module Utility Functions Definitions."""

from . import constants

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'  # NOQA pylint: disable=R0801
__copyright__ = 'Copyright 2017 Greg Albrecht and Contributors'  # NOQA pylint: disable=R0801
__license__ = 'Apache License, Version 2.0'  # NOQA pylint: disable=R0801


def escape_special_codes(raw_codes):
    """
    Escape special codes, per KISS spec.

    "If the FEND or FESC codes appear in the data to be transferred, they
    need to be escaped. The FEND code is then sent as FESC, TFEND and the
    FESC is then sent as FESC, TFESC."
    - http://en.wikipedia.org/wiki/KISS_(TNC)#Description
    """
    output = b''
    for i, x in enumerate(raw_codes):
        x = bytes([x])
        if constants.FESC == x:
            output += constants.FESC_TFESC
        elif constants.FEND == x:
            output += constants.FESC_TFEND
        else:
            output += x
    return output


def recover_special_codes(escaped_codes):
    """
    Recover special codes, per KISS spec.

    "If the FESC_TFESC or FESC_TFEND escaped codes appear in the data received,
    they need to be recovered to the original codes. The FESC_TFESC code is
    replaced by FESC code and FESC_TFEND is replaced by FEND code."
    - http://en.wikipedia.org/wiki/KISS_(TNC)#Description
    """

    output = b''
    enumerated = enumerate(escaped_codes)
    for i, x in enumerated:
        if constants.FESC_TFESC == escaped_codes[i:i+2]:
            output += constants.FESC
            next(enumerated, None)
        elif constants.FESC_TFEND == escaped_codes[i:i+2]:
            output += constants.FEND
            next(enumerated, None)
        else:
            output += bytes([x])
    return output

def extract_ui(frame):
    """
    Extracts the UI component of an individual frame.

    :param frame: APRS/AX.25 frame.
    :type frame: str
    :returns: UI component of frame.
    :rtype: str
    """
    start_ui = frame.split(
        b''.join([constants.FEND, constants.DATA_FRAME]))
    end_ui = start_ui[0].split(b''.join([constants.SLOT_TIME, constants.UI_PROTOCOL_ID]))
    return ''.join([chr(x >> 1) for x in end_ui[0]])


def strip_df_start(frame):
    """
    Strips KISS DATA_FRAME start (0x00) and newline from frame.

    :param frame: APRS/AX.25 frame.
    :type frame: str
    :returns: APRS/AX.25 frame sans DATA_FRAME start (0x00).
    :rtype: str
    """
    return frame.lstrip(constants.DATA_FRAME).strip()


def strip_nmea(frame):
    """
    Extracts NMEA header from T3-Micro or NMEA encoded KISS frames.
    """
    if len(frame) > 0:
        if frame[0] == 240:
            return frame[1:].rstrip()
    return frame
