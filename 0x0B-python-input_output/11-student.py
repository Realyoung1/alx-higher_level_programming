#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Representing the student."""

    def __init__(self, first_name, last_name, age):
        """Initializing the new Student.
        Args:
            first_name (str): The firsts name of the student.
            last_name (str): The lasts name of the student.
            age (int): The agess of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representations of the Students.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for m, n in json.items():
            setattr(self, m, n)
