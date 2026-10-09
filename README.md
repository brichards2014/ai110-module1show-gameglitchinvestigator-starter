# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
## Game Purpose
A Streamlit number guessing game. The player picks a difficulty, guesses the secret number, and gets a Higher or Lower hint after each guess.

- [x] Detail which bugs you found.
## Bugs Found
- Hints were reversed in `check_guess`.
- The secret was converted to a string on even attempts.
- Difficulty ranges were out of order, and the info text and New Game ignored the selected range.
- [x] Explain what fixes you applied.
## Fixes Applied
- Moved the logic into `logic_utils.py` and corrected the hint messages.
- Removed the string conversion.
- Set ranges to Easy 1 to 20, Normal 1 to 50, Hard 1 to 100, and used them in the info text and New Game.

## 📸 Demo Walkthrough

1. Pick a difficulty in the sidebar. The sidebar shows the number range and how many attempts you get:
   - Easy: 1 to 20, 6 attempts
   - Normal: 1 to 50, 8 attempts
   - Hard: 1 to 100, 5 attempts
2. Read the box under "Make a guess." It shows the range for your difficulty and how many attempts you have left.
3. Type a whole number in the "Enter your guess" box and click **Submit Guess**.
4. Read the hint under the button:
   - "📈 Go HIGHER!" means the secret number is larger than your guess.
   - "📉 Go LOWER!" means the secret number is smaller than your guess.
5. Keep guessing, using each hint to narrow the range. Your score changes after each guess.
6. Win by entering the secret number. The game shows balloons and your final score.
7. If you run out of attempts, the game ends and reveals the secret number.
8. Click **New Game** to play again. Your score, attempts, and history reset, and a new secret number is picked.
9. Uncheck **Show hint** if you want to play without hints.
10. Change the difficulty at any time. The game restarts with the new range and attempt limit.


## 🧪 Test Results

```
tests\test_game_logic.py ....                                                                                                                                                          [100%]

===================================================================================== 4 passed in 0.03s =====================================================================================
```
