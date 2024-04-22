#!/usr/bin/env python3
"""
Annotate the below functions parameters
and return values with the appropriate types
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence],
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Return a list of tuples where the first element
    of each passed tuple is the original tuple
    and the second element is the length of the tuple.
    """
    return [(i, len(i)) for i in lst]
