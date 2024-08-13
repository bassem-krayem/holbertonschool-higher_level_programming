#!/usr/bin/python3

class LockedClass():
    def __setattr__(self, name, value):
        if name != "first_name":
            raise
        AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
