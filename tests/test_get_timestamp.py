import datetime

from onebag.functions import get_timestamp


def test_get_timestamp():
    now = datetime.datetime.now()
    assert get_timestamp() == now.strftime("%-m/%d [%H:%M] ")
