#!/usr/bin/env python
# coding: utf-8
1. A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave. In order to understand metaclasses well, one needs to have prior experience working with Python classes.

2. Custom metaclasses
There are several ways to do this, but one way is to set __metaclass__ at the module level. This way, all classes of this module will be created using this metaclass, and we just have to tell the metaclass to turn all attributes to upperca

3. Anything you can do with a class decorator, you can of course do with a custom metaclass (just apply the functionality of the "decorator function", i.e., the one that takes a class object and modifies it, in the course of the metaclass's __new__ or __init__ that make the class object

4. A class decorator is a simple function that receives a class instance as a parameter and returns either a new class or a modified version of the original class.
Class decorators are useful when you want to modify every method or attribute of a class with minimal boilerplate.
Metaclasses can’t be composed together easily, while many class decorators can be used to extend the same class without conflicts.