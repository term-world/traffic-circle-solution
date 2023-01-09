import narrator

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    flag = check_flag("north_west_light")
    crosswalk = check_flag("north_west_crosswalk")
    self.state = flag if flag else "🔴"
    self.cross = crosswalk if crosswalk else "❌"

  def __str__(self) -> str:
    return f"{self.state} {self.cross}"

  def use(self) -> None:
    # Do not alter
    light = self.state
    crosswalk = self.cross
    # Do not alter

    #----------------------
    if light == "🟢" and crosswalk == "✔️":
      light = "🟡"
    elif light == "🟡" and crosswalk == "✔️":
      light = "🔴"
    elif light == "🔴" and crosswalk == "✔️":
      light = "🟢"
      crosswalk = "❌"
    elif light == "🟢" and crosswalk == "❌":
      crosswalk = "✔️"
    #----------------------
    
    # Do not alter
    self.state = light
    self.cross = crosswalk
    set_flag("north_west_light", self.state)
    set_flag("north_west_crosswalk", self.cross)
    # Do not alter

def main():
  stoplight = Stoplight()
  stoplight.use()
  print(stoplight)

if __name__ == "__main__":
  main()