"""
B3.1 / B3.2 OOP PRACTICE PROJECT
================================
Fill in each TODO below. Do not change any method or class NAMES, or the
tests won't be able to find your code.

Task 0 is already solved for you as a worked example — read it first,
it shows the pattern every other task follows.

Once you've written some code, run the tests (see the top of test_tasks.py
for exact instructions) to check your answer.
"""

from abc import ABC, abstractmethod


# ============================================================
# TASK 0 — WORKED EXAMPLE (already done for you, B3.1.1)
# ============================================================
# A basic class with a constructor and a method. This one is complete —
# use it as your reference for how the rest of the file should look.

class Bird:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"


# ============================================================
# TASK 1 — Encapsulation: private attribute + getter (B3.1.5)
# ============================================================
# Create a BankAccount class.
# - The constructor takes a starting balance and stores it PRIVATELY
#   (remember: private means a double-underscore prefix, e.g. self.__x)
# - get_balance() should return that private balance

class BankAccount:
    def __init__(self, balance):
        # TODO: store `balance` as a private attribute
        pass

    def get_balance(self):
        # TODO: return the private balance
        pass


# ============================================================
# TASK 2 — Encapsulation: a setter with validation logic (B3.1.5)
# ============================================================
# Add 2 methods to BankAccount below.
# - deposit(amount): only adds the amount to the balance if amount > 0.
#   If amount <= 0, do nothing (no error needed).
# - withdraw(amount): only subtracts the amount if the account has
#   enough balance (amount <= current balance). Otherwise, do nothing.
#
# Remember: making a variable private does NOT validate anything by
# itself — the validation has to be written into the method.

class BankAccountWithRules(BankAccount):
    def deposit(self, amount):
        # TODO: only add amount to the balance if amount > 0
        pass

    def withdraw(self, amount):
        # TODO: only subtract amount if there's enough balance
        pass


# ============================================================
# TASK 3 — Static variables (B3.1.3)
# ============================================================
# Create a Robot class that keeps track of how many Robot objects have
# EVER been created — shared across every instance, not per-object.
# - total_robots should be a static (class-level) variable, starting at 0
# - Every time a new Robot is created, total_robots should increase by 1
# - get_total_robots() should return the current shared count

class Robot:
    # TODO: declare a static variable here, total_robots, starting at 0

    def __init__(self, name):
        self.name = name
        # TODO: increase the shared total_robots count by 1
        # (hint: use the CLASS name, not self, to access a static variable)

    def get_total_robots(self):
        # TODO: return the static total_robots count
        pass


# ============================================================
# TASK 4 — __str__ (B3.1.4)
# ============================================================
# Add a __str__ method to the Robot class above so that
# print(myRobot) shows:   "Robot: <name>"
# (Add this method inside the Robot class above, not here.)


# ============================================================
# TASK 5 & 6 — Inheritance + method overriding (B3.2.1 / B3.2.2)
# ============================================================
# Vehicle is already written for you. Complete the Car subclass below.

class Vehicle:
    def __init__(self, fuelType, capacity):
        self.fuelType = fuelType
        self.capacity = capacity

    def move(self):
        return "The vehicle is moving"


class Car(Vehicle):
    def __init__(self, fuelType, capacity, electric):
        # TODO: call the superclass constructor with fuelType and capacity
        # TODO: then store `electric` as self.electric
        pass

    def move(self):
        # TODO: override this method to return "The car is moving"
        pass


# ============================================================
# TASK 7 — Polymorphism / isinstance (B3.2.1 / B3.2.2)
# ============================================================
# Truck is already written for you (it does NOT have an `electric`
# attribute at all). Write a function that safely counts only the
# ELECTRIC CARS in a mixed list of vehicles, without crashing on Trucks.

class Truck(Vehicle):
    def move(self):
        return "The truck is moving"


def count_electric_cars(vehicles):
    # TODO: loop through `vehicles`. For each item, check if it's a Car
    # (use isinstance) AND if item.electric is True. Return how many
    # match both conditions. Do NOT just check for `.electric` on every
    # item — Truck objects don't have it, and that would crash.
    pass


# ============================================================
# TASK 8 — Abstraction (B3.2.3)
# ============================================================
# Shape should be an abstract class: it can never be instantiated
# directly, and it forces every subclass to implement BOTH area() and
# perimeter().

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    # TODO: add a second abstract method here called perimeter()
    # (follow the exact same pattern as area() above)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # TODO: return the area of a square (side * side)
        pass

    def perimeter(self):
        # TODO: return the perimeter of a square (4 * side)
        pass


# ============================================================
# TASK 9 — Aggregation (B3.2.4)
# ============================================================
# Song is already written for you. Complete the Playlist class so it
# can hold a list of Song objects.

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self, name):
        self.name = name
        # TODO: create an empty list here to hold songs

    def add_song(self, song):
        # TODO: add `song` to the list of songs
        pass

    def get_songs(self):
        # TODO: return the list of songs
        pass

    def total_songs(self):
        # TODO: return how many songs are currently in the playlist
        pass


# ============================================================
# TASK 10 — Singleton design pattern (B3.2.5)
# ============================================================
# ConfigManager should only ever allow ONE instance to exist, no matter
# how many times ConfigManager() is called. Use __new__, not __init__,
# to control this (see the B3.2 slides for the pattern).

class ConfigManager:
    _instance = None

    def __new__(cls):
        # TODO: if cls._instance is None, create it with
        # super(ConfigManager, cls).__new__(cls) and give it a fresh
        # dictionary attribute called `settings`.
        # Either way, return cls._instance at the end.
        pass


# ============================================================
# BONUS (not tested) — Factory design pattern (B3.2.5)
# ============================================================
# For extra practice, try writing a Factory class that has a method
# create_square(side) which returns a new Square object. This isn't
# checked by the tests — it's just for extra practice if you finish
# everything else early.
