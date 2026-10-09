# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
The number range for the guess should be constrained by the difficulty, easy should be 1 to 20, normal 1 to 100 and hard 1 to 50. The ranges displayed do not make sense, medium and hard should be swapped. The reality of the game showed the range is not taken into consideration when a difficulty is selected, any difficulty selected, the guess range remains 1 to 100.

The 'guess' itself was flawed. It would never get to the right result. The first run, I guessed small, I chose 5, and the hint kept saying go lower, when I reached 1, it still had go lower and that was the lowest accepted number. The second run, I started at 1, and the hint was still go lower, this proved the input itself was not being checked correctly against the answer.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior                                                        | Actual Behavior                      | Console Output / Error |
|-------|--------------------------------------------------------------------------|--------------------------------------|------------------------|
|Visual |Difficulty range should increase with each jump from easy - medium - hard |Difficulty Range incorrect            | None
|5|1| | |Hint should point you in the right direction of the answer                |Hint is misleading                    | None
|Visual |"Guess a number" Should update with difficulty                            |Guess does not update with difficulty | None

---

## 2. How did you use AI as a teammate?

I used Claude for this project. I gave it my bug notes and the project files, and it proposed fixes for the hint logic and the difficulty ranges.

Correct suggestion: Claude pointed out that check_guess had its messages swapped, so a guess above the secret said “Go HIGHER!”. It also found that app.py converted the secret to a string on even attempts, which broke the comparison. I verified both by writing pytest cases (60 vs 50 returns “Too High”, 40 vs 50 returns “Too Low”) and by playing the game with the debug panel open.

Suggestion I changed: My notes said “easy and hard should be swapped.” Claude read my table instead and set the ranges to Easy 1 to 20, Normal 1 to 50, Hard 1 to 100, so the range grows with difficulty. Swapping Easy and Hard literally would have made Hard the smallest range. I checked the sidebar and info text at each difficulty to make sure the result matched what I wanted.

AI suggestion: Claude wanted to replace the issues with a configuration layer, a result type and a game class. This would significantly overcomplicate the request, though it would follow coding principles. I chose to remain function based because of the scope of the project.


---

## 3. Debugging and testing your fixes

I treated a bug as fixed when a test failed before the change and passed after it, and the live game behaved the same way. I wrote four pytest cases: a high guess, a low guess, a correct guess, and the range for each difficulty. The first run of py -m pytest failed because I had two files named test_game_logic.py, one in the project root and one in tests/. I removed the extra copy and the tests passed.

Claude helped me decide what to test. It suggested checking both the outcome and the hint text, since the original bug was in the message.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole script from top to bottom every time you click a button or type in a box. Normal variables reset on each rerun. st.session_state is a dictionary that keeps its values between reruns, so it holds things like the secret number, the score, and the attempt count. That is why the game checks if "secret" not in st.session_state before creating a secret. It only sets the value the first time.

---

## 5. Looking ahead: your developer habits

Habit to reuse: I want to write a small test for each bug before accepting a fix. It gave me a clear pass or fail instead of relying on what the game looked like.

What I would do differently: I would give the AI more precise notes. My “easy and hard should be swapped” line was ambiguous, and a clearer description would have avoided guessing.

This project has not changed how I view AI generated code. It is a tool that should be accurately used whenever possible, the human in the loop will always remain as the most important.
