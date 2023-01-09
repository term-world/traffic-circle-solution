import narrator
import random

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    northlight = check_flag("north_north_east_light")
    eastlight = check_flag("east_north_east_light")
    northtraffic = check_flag("north_north_east_traffic")
    easttraffic = check_flag("east_north_east_traffic")
    self.north = northlight if northlight else "🟢"
    self.east = eastlight if eastlight else "🔴"
    self.northtraffic = northtraffic if northtraffic else "❌"
    self.easttraffic = easttraffic if easttraffic else "❌"

  def __str__(self) -> str:
    return f"  North Light: {self.north}   East Light:{self.east}\nNorth Traffic: {self.northtraffic}  East Traffic:{self.easttraffic}"

  def use(self) -> None:
    # Do not alter
    northlight = self.north
    eastlight = self.east
    northtraffic = random.choice(["✔️","❌","❌","❌","❌"]) if northlight != "🟡" or eastlight != "🟡" else "❌"
    easttraffic = random.choice(["✔️","❌","❌","❌","❌"]) if northlight != "🟡" or eastlight != "🟡" else "❌"
    # Do not alter

    #----------------------
    if eastlight == "🟡":
      eastlight = "🔴"
      northlight = "🟢"
    elif northlight == "🟡":
      eastlight = "🟢"
      northlight = "🔴"
    elif northtraffic == "❌" and easttraffic == "✔️"and northlight == "🟢":
      northlight = "🟡"
    elif northtraffic == "✔️" and easttraffic == "❌" and eastlight == "🟢":
      eastlight = "🟡"
    #----------------------
    
    # Do not alter
    self.north = northlight
    self.east = eastlight
    self.northtraffic = northtraffic
    self.easttraffic = easttraffic
    set_flag("north_north_east_light", self.north)
    set_flag("east_north_east_light", self.east)
    set_flag("north_north_east_traffic", self.northtraffic)
    set_flag("east_north_east_traffic", self.easttraffic)
    # Do not alter

def main():
  obj = Stoplight()
  obj.use()
  print(obj)

if __name__ == "__main__":
  main()