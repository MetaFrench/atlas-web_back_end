#!/usr/bin/env python3
"""range parameters"""


def index_range(page, page_size):
    """Returns the start and end indexes for pagination."""
    if page <= 0 or page_size <= 0:
        return None

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
