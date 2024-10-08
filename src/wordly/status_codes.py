"""DICT status codes."""

from enum import Enum, unique
from functools import cache


@unique
class Status(Enum):
    """
    Enumeration of possible status responses from a DICT server.

    Note:
        The first digit of the response has the following meaning:

            1yz - Positive Preliminary reply
            2yz - Positive Completion reply
            3yz - Positive Intermediate reply
            4yz - Transient Negative Completion reply
            5yz - Permanent Negative Completion reply

        The next digit in the code indicates the response category:

            x0z - Syntax
            x1z - Information (e.g., help)
            x2z - Connections
            x3z - Authentication
            x4z - Unspecified as yet
            x5z - DICT System (These replies indicate the status of the
                  receiver DICT system vis-a-vis the requested transfer
                  or other DICT system action.)
            x8z - Nonstandard (private implementation) extensions

    """

    DATABASE_PRESENT = b"110"
    STRATEGIES_AVAILABLE = b"111"
    DATABASE_INFO = b"112"
    HELP = b"113"
    SERVER_INFO = b"114"
    DEFINITION_RETRIEVED = b"150"
    DEFINITION = b"151"
    MATCHES_FOUND = b"152"
    INITIAL_CONNECTION = b"220"
    CLOSING_CONNECTION = b"221"
    AUTH_SUCCESSFUL = b"230"
    COMMAND_COMPLETE = b"250"
    SERVER_TEMPORARILY_UNAVAILABLE = b"420"
    SERVER_SHUTTING_DOWN = b"421"
    COMMAND_NOT_RECOGNIZED = b"500"
    ILLEGAL_PARAMETERS = b"501"
    COMMAND_NOT_IMPLEMENTED = b"502"
    COMMAND_PARAMETER_NOT_IMPLEMENTED = b"503"
    ACCESS_DENIED = b"530"
    NO_MATCH = b"552"

    @classmethod
    @cache
    def statuses(cls):
        return {member.value: member for _, member in cls.__members__.items()}

    @classmethod
    def by_value(cls, value):
        return cls.statuses().get(value)
