"""
check_progress.py
==================
A friendlier way to check your work than raw unittest output.

Run this instead of (or in addition to) test_tasks.py directly:

    python check_progress.py

It runs the exact same tests from test_tasks.py, but prints one line per
TASK instead of one line per individual check — so a task only shows as
PASS once every check for that task passes.

If a task shows FAIL, run just that task's tests on their own to see the
detailed error message, e.g. for Task 8:

    python -m unittest test_tasks.TestTask8Abstraction -v

(Swap in the class name shown next to any FAIL below.)
"""

import io
import unittest
from collections import defaultdict

import test_tasks


# Maps each TestCase class in test_tasks.py to a friendly task label,
# in the order they should be displayed.
TASK_ORDER = [
    ("TestTask0Example", "Task 0  (Worked example)"),
    ("TestTask1Encapsulation", "Task 1  (Encapsulation: private attr + getter)"),
    ("TestTask2SetterValidation", "Task 2  (Encapsulation: setter validation)"),
    ("TestTask3StaticVariable", "Task 3  (Static variable)"),
    ("TestTask4Str", "Task 4  (__str__)"),
    ("TestTask5And6InheritanceAndOverriding", "Task 5-6 (Inheritance + overriding)"),
    ("TestTask7Polymorphism", "Task 7  (Polymorphism / isinstance)"),
    ("TestTask8Abstraction", "Task 8  (Abstraction)"),
    ("TestTask9Aggregation", "Task 9  (Aggregation)"),
    ("TestTask10Singleton", "Task 10 (Singleton pattern)"),
]


def collect_tests(suite):
    """Flatten a (possibly nested) TestSuite into a flat list of test cases."""
    tests = []
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            tests.extend(collect_tests(item))
        else:
            tests.append(item)
    return tests


def main():
    suite = unittest.TestLoader().loadTestsFromModule(test_tasks)

    # IMPORTANT: collect the flat list of test objects BEFORE running the
    # suite. unittest clears each test's slot in the suite (sets it to
    # None) right after running it, to free memory — so if we wait until
    # after runner.run(), the suite is full of Nones.
    all_tests = collect_tests(suite)

    # Run the whole suite quietly — we build our own summary from the result.
    runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
    result = runner.run(suite)

    failed_ids = {test.id() for test, _ in (result.failures + result.errors)}

    counts = defaultdict(lambda: [0, 0])  # class_name -> [passed, total]
    for test in all_tests:
        cls_name = test.__class__.__name__
        counts[cls_name][1] += 1
        if test.id() not in failed_ids:
            counts[cls_name][0] += 1

    print()
    print("=" * 60)
    print(" B3.1 / B3.2 PRACTICE PROJECT -- TASK PROGRESS")
    print("=" * 60)

    tasks_complete = 0
    tasks_seen = 0
    for cls_name, label in TASK_ORDER:
        if cls_name not in counts:
            continue
        tasks_seen += 1
        passed, total = counts[cls_name]
        complete = passed == total
        tasks_complete += 1 if complete else 0
        status = "PASS" if complete else "FAIL"
        print(f"[{status}] {label:<48} ({passed}/{total} checks)  -- {cls_name}")

    print("-" * 60)
    total_checks = result.testsRun
    passed_checks = total_checks - len(failed_ids)
    print(f"{tasks_complete}/{tasks_seen} tasks fully complete "
          f"({passed_checks}/{total_checks} individual checks passing)")
    print("=" * 60)

    if tasks_complete == tasks_seen:
        print("All tasks complete! Great work.")
    else:
        print("For any task marked FAIL, run its class name directly, e.g.:")
        print("    python -m unittest test_tasks.TestTask3StaticVariable -v")
    print()


if __name__ == "__main__":
    main()
