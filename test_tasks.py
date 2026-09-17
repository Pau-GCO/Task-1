"""
==============================================================
 HOW TO CHECK YOUR ANSWERS
==============================================================
There are 2 ways to check your work. Use whichever you prefer — they
run the exact same tests underneath, just displayed differently.

--------------------------------------------------------------
OPTION A (recommended): the clean per-task summary
--------------------------------------------------------------
Open a terminal in VS Code (Terminal → New Terminal) and run:

        python check_progress.py

This prints ONE line per task, like:

        [PASS] Task 1  (Encapsulation: private attr + getter)   (2/2 checks)
        [FAIL] Task 2  (Encapsulation: setter validation)       (0/4 checks)

A task only shows PASS once every check for that task passes. If a
task shows FAIL, the line also tells you the exact command to run to
see the detailed error for just that task, for example:

        python -m unittest test_tasks.TestTask2SetterValidation -v

--------------------------------------------------------------
OPTION B: the full raw test output
--------------------------------------------------------------
If you want to see every individual check at once (more detailed, but
much longer and harder to scan), run:

        python -m unittest test_tasks.py -v

Each line ends in "ok", "FAIL", or "ERROR":
    ok     → that check is correct
    FAIL   → your code ran, but gave the wrong answer
    ERROR  → your code crashed (check for typos, missing
             return statements, etc.)

At the very bottom you'll see a summary like:

        Ran 22 tests in 0.01s
        OK

"OK" at the bottom means every single check passed. If it instead says
"FAILED (failures=2)", scroll UP to find those tests and read the
error message above each one — it shows what your code returned vs.
what was expected.

--------------------------------------------------------------
Either way: there's no penalty for getting it wrong. Fix tasks.py and
re-run as many times as you like.

TIP: If you have the official "Python" extension installed in VS Code,
you can also click the little "Run Test" arrow that appears above each
test function/class in this file, instead of using the terminal.
==============================================================
"""

import unittest
from tasks import (
    Bird,
    BankAccount,
    Robot,
    Vehicle,
    Car,
    Truck,
    count_electric_cars,
    Shape,
    Square,
    Song,
    Playlist,
    ConfigManager,
)


class TestTask0Example(unittest.TestCase):
    """Task 0 — worked example. This should already pass with no edits."""

    def test_bird_make_sound(self):
        b = Bird("Duck", "Quack")
        self.assertEqual(b.make_sound(), "Duck says Quack")


class TestTask1Encapsulation(unittest.TestCase):
    """Task 1 — private attribute + getter."""

    def test_get_balance_returns_starting_value(self):
        acct = BankAccount(100)
        self.assertEqual(acct.get_balance(), 100)

    def test_balance_is_actually_private(self):
        acct = BankAccount(50)
        # A private attribute gets "name-mangled" by Python to
        # _ClassName__attribute. If this key isn't present, the
        # attribute probably wasn't declared with double underscores.
        self.assertIn("_BankAccount__balance", vars(acct))


class TestTask2SetterValidation(unittest.TestCase):
    """Task 2 — deposit/withdraw with validation rules."""

    def test_deposit_positive_amount(self):
        acct = BankAccount(100)
        acct.deposit(50)
        self.assertEqual(acct.get_balance(), 150)

    def test_deposit_ignores_non_positive_amount(self):
        acct = BankAccount(100)
        acct.deposit(-20)
        acct.deposit(0)
        self.assertEqual(acct.get_balance(), 100)

    def test_withdraw_within_balance(self):
        acct = BankAccount(100)
        acct.withdraw(40)
        self.assertEqual(acct.get_balance(), 60)

    def test_withdraw_more_than_balance_is_ignored(self):
        acct = BankAccount(100)
        acct.withdraw(500)
        self.assertEqual(acct.get_balance(), 100)


class TestTask3StaticVariable(unittest.TestCase):
    """Task 3 — a static variable shared across every instance."""

    def test_total_robots_increases_with_each_new_robot(self):
        before = Robot("placeholder").get_total_robots()
        Robot("R2D2")
        Robot("C3PO")
        after = Robot("BB8").get_total_robots()
        # 3 new robots were created since `before` was measured
        self.assertEqual(after - before, 3)

    def test_all_robots_share_the_same_count(self):
        r1 = Robot("Wall-E")
        r2 = Robot("Eve")
        self.assertEqual(r1.get_total_robots(), r2.get_total_robots())


class TestTask4Str(unittest.TestCase):
    """Task 4 — __str__ formatting."""

    def test_robot_str_format(self):
        r = Robot("Optimus")
        self.assertEqual(str(r), "Robot: Optimus")


class TestTask5And6InheritanceAndOverriding(unittest.TestCase):
    """Tasks 5 & 6 — Car inherits Vehicle, and overrides move()."""

    def test_car_inherits_vehicle_attributes(self):
        c = Car("Petrol", 5, True)
        self.assertEqual(c.fuelType, "Petrol")
        self.assertEqual(c.capacity, 5)
        self.assertEqual(c.electric, True)

    def test_car_move_is_overridden(self):
        c = Car("Diesel", 5, False)
        self.assertEqual(c.move(), "The car is moving")

    def test_plain_vehicle_move_is_unchanged(self):
        v = Vehicle("Diesel", 4)
        self.assertEqual(v.move(), "The vehicle is moving")


class TestTask7Polymorphism(unittest.TestCase):
    """Task 7 — isinstance-based counting across mixed subclasses."""

    def test_counts_only_electric_cars(self):
        fleet = [
            Car("Electric", 5, True),
            Car("Petrol", 5, False),
            Car("Electric", 5, True),
            Truck("Diesel", 20),
        ]
        self.assertEqual(count_electric_cars(fleet), 2)

    def test_does_not_crash_on_trucks_only(self):
        fleet = [Truck("Diesel", 20), Truck("Diesel", 25)]
        self.assertEqual(count_electric_cars(fleet), 0)


class TestTask8Abstraction(unittest.TestCase):
    """Task 8 — abstract class enforcement + a concrete subclass."""

    def test_shape_cannot_be_instantiated_directly(self):
        with self.assertRaises(TypeError):
            Shape()

    def test_square_area(self):
        sq = Square(4)
        self.assertEqual(sq.area(), 16)

    def test_square_perimeter(self):
        sq = Square(4)
        self.assertEqual(sq.perimeter(), 16)


class TestTask9Aggregation(unittest.TestCase):
    """Task 9 — Playlist holding a list of Song objects."""

    def test_add_and_get_songs(self):
        p = Playlist("Road Trip")
        p.add_song(Song("Song A", "Artist A"))
        p.add_song(Song("Song B", "Artist B"))
        songs = p.get_songs()
        self.assertEqual(len(songs), 2)
        self.assertEqual(songs[0].title, "Song A")

    def test_total_songs(self):
        p = Playlist("Chill")
        p.add_song(Song("Song A", "Artist A"))
        self.assertEqual(p.total_songs(), 1)


class TestTask10Singleton(unittest.TestCase):
    """Task 10 — Singleton pattern using __new__."""

    def setUp(self):
        # Reset the singleton before each test in this class, so tests
        # don't interfere with each other.
        ConfigManager._instance = None

    def test_two_instances_are_the_same_object(self):
        a = ConfigManager()
        b = ConfigManager()
        self.assertIs(a, b)

    def test_settings_are_shared_between_references(self):
        a = ConfigManager()
        a.settings["volume"] = 80
        b = ConfigManager()
        self.assertEqual(b.settings["volume"], 80)


if __name__ == "__main__":
    unittest.main()
