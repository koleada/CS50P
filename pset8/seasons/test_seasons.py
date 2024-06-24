from seasons import get_minutes
import pytest
from datetime import date, timedelta


def test():
    assert (
        get_minutes("1999-01-01")
        == "Thirteen million, three hundred ninety-six thousand, three hundred twenty minutes"
    )
    assert (
        get_minutes(str(date.today() - timedelta(days=365)))
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        get_minutes(str(date.today() - timedelta(days=2 * 365)))
        == "One million, fifty-one thousand, two hundred minutes"
    )

    with pytest.raises(SystemExit):
        get_minutes("bird-sa-sa")
    with pytest.raises(SystemExit):
        get_minutes("cat")
    with pytest.raises(SystemExit):
        get_minutes("2022-13-10")
    with pytest.raises(SystemExit):
        get_minutes("2022-13-35")
    with pytest.raises(SystemExit):
        get_minutes("bird-sa-sa")
    with pytest.raises(SystemExit):
        get_minutes(" 2022-13-12")
