import pytest

import tidalapi

from .cover import verify_image_cover


@pytest.mark.vcr
def test_mix(session):
    mixes = session.mixes()
    first = next(iter(mixes))
    assert isinstance(first, tidalapi.Mix)


@pytest.mark.vcr
def test_image(session):
    mixes = session.mixes()
    first = next(iter(mixes))
    verify_image_cover(session, first, [320, 640, 1500])
