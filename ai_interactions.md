# AI Interactions

## Advanced Edge-Case Testing

### Prompt

I asked Claude to add more pytest cases for the extra credit after my two bug fixes were done and passing. My message was: "Lets do the additional pytests for the extra cred." Claude had the project files and the grading rubric in context, so it targeted the stretch requirement of three or more edge-case tests.

### What Claude Generated

Claude extended `tests/test_game_logic.py` with edge-case tests for `parse_guess`, `check_guess`, `update_score`, and `get_range_for_difficulty`. It kept my four original tests and used `pytest.mark.parametrize` to cover several inputs with one test function.

### Edge Cases and Rationale

| Edge case | Function | Why it was chosen |
|---|---|---|
| Empty string and `None` | `parse_guess` | The text box starts empty, so this is the most common bad input |
| `"abc"`, `"12abc"`, `"1e3"`, `"nan"`, `"--5"`, spaces only | `parse_guess` | Players can type anything. The game must show an error instead of crashing |
| `"-5"` | `parse_guess` | Confirms negative numbers parse correctly |
| `"7.9"` | `parse_guess` | The code truncates decimals to 7. The test documents that behavior |
| `" 42 "` | `parse_guess` | Confirms spaces around a number are ignored |
| Guess of -5 against a secret of 10 | `check_guess` | Confirms the comparison still gives the right hint for negative values |
| Win on attempt 1 and attempt 20 | `update_score` | The points formula goes negative on late attempts without the 10-point floor |
| Unknown difficulty name | `get_range_for_difficulty` | Confirms the fallback range of 1 to 50 |

### Verification

I ran `py -m pytest` from the project root. The terminal output is pasted in the Test Results section of `README.md`.

### Limitation Found

The edge-case tests showed that `parse_guess` accepts numbers outside the game range. A guess of `-5` or `500` is accepted and counts as an attempt. The tests document this current behavior. I did not fix it in this project.