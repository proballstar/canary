"""
This file defines the drone's external error system in a with-feedback loop.
"""
from common import log_states as logger
# from ____ import drone
noise = False
external = False
model = False

logger.__init__()
logger.WARNING("This API will be deprecated in a future version.")

if bool(model) != False:
    logger.FATAL("Model error detected! Sending signal to drone...")
    # drone.cmd_position(drone.global_home[0], drone.global_home[1], drone.global_home[2])
    # Returns to global home x, y, and z
else:
    logger.SUCCESS("No model error detected!")

if bool(noise) != False:
    # TODO: Allow user to disable this:
    # @firebolt-ai Should we?
    logger.FATAL("A faulty sensor was detected on your drone! Sending signal to drone...")
    # drone.cmd_position(drone.global_home[0], drone.global_home[1], drone.global_home[2])
    # Returns to global home x, y, and z
else:
    logger.SUCCESS("No model error detected!")

if bool(external) != False:
    logger.FATAL("An external error was detected! Sending signal to drone...")
    # drone.cmd_position(drone.global_home[0], drone.global_home[1], drone.global_home[2])
    # Returns to global home x, y, and z
else:
    logger.SUCCESS("No external error detected!")
