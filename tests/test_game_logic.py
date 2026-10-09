import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


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


# Edge cases


@pytest.mark.parametrize("raw", ["", None])
def test_parse_guess_rejects_empty_input(raw):
    ok, value, error = parse_guess(raw)
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


@pytest.mark.parametrize("raw", ["abc", "12abc", "1e3", "nan", "--5", "   "])
def test_parse_guess_rejects_non_numeric_text(raw):
    ok, value, error = parse_guess(raw)
    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_parse_guess_accepts_negative_numbers():
    assert parse_guess("-5") == (True, -5, None)


def test_parse_guess_truncates_decimals():
    assert parse_guess("7.9") == (True, 7, None)


def test_parse_guess_ignores_surrounding_spaces():
    assert parse_guess(" 42 ") == (True, 42, None)


def test_check_guess_handles_negative_guess():
    outcome, message = check_guess(-5, 10)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_win_score_has_ten_point_floor():
    assert update_score(0, "Win", 1) == 80
    assert update_score(0, "Win", 20) == 10


def test_unknown_difficulty_uses_default_range():
    assert get_range_for_difficulty("Impossible") == (1, 50)