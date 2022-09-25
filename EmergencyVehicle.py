import os
import sys
import shutil
import narrator

from importlib import import_module
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class EmergencyVehicle(FixtureSpec):

    def __init__(self):
        super().__init__()
        #self. n = narrator.Narrator()
        self.curr_dir = check_flag("cwd")

    def __get_light(self, direction) -> any:
        stoplight = import_module(
            f"{direction}.Stoplight"
        )
        return stoplight.Stoplight()
    
    def __make_turn(self, direction) -> None:
        pass

    def use(self, direction: str = "north") -> None:
        # Do not alter
        move_to = None
        stoplight = self.__get_light(direction)
        stoplight.use()
        signal = str(stoplight)
        # Do not alter

        #------------------------
        if signal == "🔴" or signal == "🟡":
            pass
        elif signal == "🟢\n➡️":
            move_to = input("Direction to turn: ")
        elif signal == "🟢":
            move_to = direction
        #------------------------

        # Do not alter
        if move_to:
            shutil.move(
                f"{os.getcwd()}/EmergencyVehicle.py",
                os.path.join(
                    self.curr_dir,
                    move_to
                )
            )
        # Do not alter

def main():
    direction = input("Direction: ")

    cwd = check_flag("cwd")

    sys.path.append(cwd)

    obj = Car()
    obj.use(direction)

if __name__ == "__main__":
    main()