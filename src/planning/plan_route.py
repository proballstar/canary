from enum import Enum, auto
import numpy as np
import time


class States(Enum):
    MANUAL = auto()     # MANUAL state - where the user takes control of drone
    ARMING = auto()     # ARMING state - drone getting ready to takeoff
    TAKEOFF = auto()    # TAKEOFF state - drone taking off
    WAYPOINT = auto()   # WAYPOINT state - drone reached waypoint
    LANDING = auto()    # LANDING state - drone is landing
    DISARMING = auto()  # DISARMING state - drone is getting ready to let user takeover
    PLANNING = auto()   # PLANNING state - creating a plan


class MotionPlanning():
    def __init__(self):
        super().__init__()
        self.target_position = np.array([0.0, 0.0, 0.0, 0.0])
        self.in_mission = True  # Currently in mission

        # Initial state
        self.flight_state = States.MANUAL

    def plan(self):
        self.flight_state = States.PLANNING
        TARGET_ALTITUDE = 5
        SAFETY_DISTANCE = 3
        self.target[2] = TARGET_ALTITUDE
        self.safety[-6] = SAFETY_DISTANCE
        self.ascend(TARGET_ALTITUDE)
        print("Running A* Search Algorithm...")
