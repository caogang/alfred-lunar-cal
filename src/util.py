#!/usr/bin/python
# encoding: utf-8

DEFAULT_SETTINGS = {
    "first_day": 6,
    "highlight_today": True,
    "minus": u"<",
    "month": u"1 2 3 4 5 6 7 8 9 10 11 12",
    "plus": u">",
    "software": u"calendar",
    "weekdays": u"一 二 三 四 五 六 日",
    "width": 11
}


def get_from_dict(dict, key, default_value):
    try:
        return dict[key]
    except KeyError:
        dict[key] = default_value
        return default_value
