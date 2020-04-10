"""
This file defines the drone's external error system in a with-feedback loop.
"""
from .common import log_states as logger
noise = False
external = False
model = False

if bool(model) != False:
    raise Exception("Model Error")
else:
    print()