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


class Drone():
    def __init__(self):
        super().__init__()
        self.target_position = np.array([0.0, 0.0, 0.0, 0.0])
        self.in_mission = True  # Currently in mission

        # Initial state
        self.flight_state = States.MANUAL

    def arming(self):
        self.flight_state = States.ARMING
    
    def takeoff(self):
        self.flight_state = States.TAKEOFF
