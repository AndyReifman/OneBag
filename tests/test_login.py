import os.path

from onebag import login_bot


def test_login():
    path = os.path.dirname(os.path.dirname(__file__))
    r, subreddit = login_bot(path)
    assert subreddit == 'gunners'
    assert r.user.me() == 'gunnersmoderator'