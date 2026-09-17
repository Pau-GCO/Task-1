# B3.1 / B3.2 OOP Practice Project

A mini coding project to practice the object-oriented programming skills from
B3.1 and B3.2 — classes, encapsulation, static variables, inheritance,
polymorphism, abstraction, aggregation, and the Singleton design pattern.

## Files

- **`tasks.py`** — this is the ONLY file you need to edit. It contains 10
  tasks, each marked with `# TODO` comments telling you exactly what to
  write. Task 0 is already fully solved for you as a worked example.
- **`check_progress.py`** — run this to see a clean, one-line-per-task
  summary of your progress. This is the easiest way to check your work.
- **`test_tasks.py`** — the actual tests. You don't need to edit this
  file. `check_progress.py` runs these same tests, just displayed more
  simply — full instructions are also in the comment block at the top
  of this file if you want to run it directly.

## Getting started

1. Open this folder in VS Code (`File → Open Folder...`).
2. Open `tasks.py` and read Task 0 at the top — it's already complete,
   and shows you the pattern every other task follows.
3. Work through Tasks 1–10 in order. Each one builds on skills from the
   task before it, and most reference a specific part of B3.1 or B3.2.
4. After finishing a task (or even partway through), open a terminal
   (`Terminal → New Terminal`) and run:

   ```
   python check_progress.py
   ```

   You'll get a one-line-per-task summary like:

   ```
   [PASS] Task 1  (Encapsulation: private attr + getter)   (2/2 checks)
   [FAIL] Task 2  (Encapsulation: setter validation)       (0/4 checks)
   ```

5. For any task marked `[FAIL]`, run the command it suggests to see the
   detailed error for just that task, e.g.:

   ```
   python -m unittest test_tasks.TestTask2SetterValidation -v
   ```

   The error message tells you exactly what your code returned versus
   what was expected.
6. Keep editing and re-running `check_progress.py` until every task
   shows `[PASS]`.

## Task list

| Task | Skill | Topic |
|---|---|---|
| 0 | — | Worked example (already done) |
| 1 | Private attribute + getter | B3.1.5 Encapsulation |
| 2 | Setter with validation logic | B3.1.5 Encapsulation |
| 3 | Static (class-level) variable | B3.1.3 Static vs. non-static |
| 4 | `__str__` formatting | B3.1.4 Constructing objects |
| 5 & 6 | Inheritance + method overriding | B3.2.1 / B3.2.2 |
| 7 | Polymorphism with `isinstance` | B3.2.1 / B3.2.2 |
| 8 | Abstract classes | B3.2.3 Abstraction |
| 9 | Aggregation (a class holding a list of objects) | B3.2.4 |
| 10 | Singleton design pattern | B3.2.5 Design patterns |

There's also an optional, ungraded **Bonus** task at the bottom of
`tasks.py` for the Factory design pattern, if you finish everything
else and want more practice.

## Getting stuck?

- Re-read the TODO comment carefully — it usually names the exact method
  or variable name expected.
- Check the error message from the test — it tells you exactly what went
  wrong (wrong value, missing attribute, or a crash).
- Go back to the B3.1/B3.2 slides for that specific skill if you're stuck
  on the underlying concept, not just the syntax.
