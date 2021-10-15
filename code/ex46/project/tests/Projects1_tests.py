from nose.tools import *
import Projects1

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RUN!", end=" ")