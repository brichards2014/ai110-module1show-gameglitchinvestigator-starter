# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
The number range for the guess should be constrained by the difficulty, easy should be 1 to 20, normal 1 to 100 and hard 1 to 50. The ranges displayed do not make sense, easy and hard should be swapped. The reality of the game showed the range is not taken into consideration when a difficulty is selected, any difficulty selected, the guess range remains 1 to 100.

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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
