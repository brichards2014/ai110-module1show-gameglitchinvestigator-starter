from logic_utils import check_guess, get_range_for_difficulty


def test_guess_above_secret_is_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_below_secret_is_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_correct_guess_wins():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_ranges_increase_with_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)