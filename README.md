

# TURNABOUTS TO TAME TRAFFIC? `term-world` CITIZENS' TAKES ARE TEPID

**Reported by `The Reporter` from `Ix` on  `26 September 2022`**

(Ix) - Given the recent influx of individuals into `term-world`, traffic has been impossibly inundated, incensing impatient idlers who are, in a word, irate. The irritating impact of this impotent infrastructure was immediately identified by our incredible Mayor when he involved himself with an important inspection of the near-infinite incidence of intolerable wait times. He said in an insightful insider interview implicating inept engineers: "I'm incredulous! It's irresponsible, immoral, insidious!"

It was during this deep-dive that he delved into his daring directive to delete the downright dismal deadlock that has defiantly drawn speed demons and doddering Sunday drivers alike to a dead standstill. We've deliberately dedicated the space down below to the disclosure of his dynamic declaration:

"It's me, your Mayor! You, pen jockey, you're getting all this down, right? That was my catchphrase. It's very important. Please try and keep up. For me. Your Mayor. Anyway, where was I?"

"Ahem, in my capacity as your Mayor I've spent a tireless hour mulling over how we might fix this teeny-weeny little...er, what's a word that says, 'I see we have a problem here, but I'd rather not call it a problem'? Oh yeah, that's good...I, your Mayor, was mulling over how we might fix this teeny-weeny little traffic hiccup. And I, your Mayor, have come up with a brilliant solution!"

"You, my fair citizens, did such a wonderful job of enacting my incredible neighborhood economy proposal that I, your Mayor, figured that if you could handle that, then you could surely handle this! Hey, glasses, are you sure you're getting all this? It's important to butter the people up, you know. That's like, Mayor 101."

"Actually, I think that's everything. Let's see, we have a hiccup, you can fix it, yada yada...yeah, that should do. You got my catchphrase, right? Gotta have a soundbite for the people. Okay, good. Now scram."

## Overview

In this set of activities we cover:

* working collaboratively using Github
* branching
* merging
* issuing "Pull Requests"
* exploring a new programming concept, control statements in:
  * conditional statements
  * booleans
  * `while` loops

You'll complete several main tasks:

* Fixing four `Stoplight.py` files to work according to specifications below
* Repairing a `Car.py` to drive from point-to-point
* Returning a `Bus.py` to service (work order below)

### Supporting media

[![YouTube thumbnail](http://img.youtube.com/vi/1BdOC0gbGAM/hqdefault.jpg)](https://youtube.com/playlist?list=PLJvBsjwXNdlFqLI3pyJdbHCF_i5Su6oYS)

## Completing `traffic-circle` content

Each file contains more specific instructions _particular to that file_. The general specifications appear below.

### `Stoplight.py` files

Each directional folder features a `Stoplight.py` file. Each works a slightly different way, but they're all in need of serious repair to put them back in working order.

**Every stoplight uses a version of the variable light; this variable can be used to store one of the following four emoji values (as a single character string) to represent the light's current status: 🟢🟡🔴⚫.**

#### `north`

A standard stoplight, cycling through each light once.

* If the light was 🔴, it becomes 🟢
* If the light was 🟢, it becomes 🟡
* If the light was 🟡, it becomes 🔴

#### `south`

A typical pattern for less-used roads, flashing red.

* If the light was 🔴, it becomes ⚫
* If the light was ⚫, it becomes 🔴

#### `south-west`

A simple light to sense a crosswalk signal.

* If the crosswalk signal is ✔️, the light becomes 🔴
* If the crosswalk signal is ❌, the light becomes 🟢

**This stoplight uses the variable `crosswalk`; this variable can be used to store one of the following two emoji values (as a single character string) to represent if the crosswalk signal is active(✔️) or not active(❌).**

#### `east`

A light with a timed turn signal.

* If the light was 🔴, it becomes 🟢 with a turn signal (➡️)
  * The signal picture is handled for you, all you need to do is complete the logic
  * The timing is also handled for you -- again, the logic is the key here
* When the turn signal expires after `5` seconds, the light stays 🟢
* If the light was 🟢, it becomes 🟡
* If the light was 🟡, it becomes 🔴

**This light uses `turn` and `hold`, these variables are both `Boolean` values (i.e., `True` or `False`).**

#### `west`

Another, simpler, timed light in which green and red last for `5` seconds. Here, the timing is also handled for you -- all you need to do is string the logic together.

* If the light was 🟡, it becomes 🔴
* After holding for `5` seconds, a 🔴 becomes a 🟢
* After holding for `5` seconds, a 🟢 becomes a 🔴

**This light uses `timeout`, this is a `Boolean` value (i.e., `True` or `False`).**

#### `north-west`

A full crosswalk light system in which the light slowly becomes red after a crosswalk signal has been activated

* If the crosswalk signal is ❌ and the light is 🟢, the crosswalk becomes ✔️
* If the crosswalk signal is ✔️ and the light is 🟢, the light becomes 🟡
* If the crosswalk signal is ✔️ and the light is 🟡, the light becomes 🔴
* If the crosswalk signal is ✔️ and the light is 🔴, the light becomes 🔴 and the crosswalk signal becomes ❌

**This stoplight uses the variable `crosswalk`; this variable can be used to store one of the following two emoji values (as a single character string) to represent if the crosswalk signal is active(✔️) or not active(❌).**

#### `north-east`

A dual-direction light system that detects which way traffic is coming from and switches the lights accordingly. There are two directions of lights to control the traffic. The first set of controls are for the lights and traffic coming from the north and south of the light as represented by the `northlight` and `northtraffic` variables. The second set of controls are for the lights and traffic coming from the east and west of the light as represented by the `eastlight` and `easttraffic` variables.

* If there is traffic coming from one direction that has a 🔴 while the other side has no traffic and a 🟢, the light without traffic should switch to a 🟡.
* If there is traffic coming from one direction that has a 🔴 while the other side has no traffic and a 🟡, the light that has traffic should switch to 🟢 and the one that does not should switch to 🔴.
  * The lights should flip from 🟢 to 🔴 so that the lights switch back and forth.

**This light uses `northlight` and `eastlight` with the 🟢🟡🔴 signals, and `northtraffic` and `easttraffic` with the traffic(✔️) and no traffic(❌) signals**

### The `Car.py` and `Bus.py`

Each vehicle behaves slightly differently.

#### `Car.py`

* Goes through any 🟢 light
* Stops if lights are 🔴 or 🟡
* At a 🟢➡️, the `Car.py` should prompt the driver for a new direction
  * Directions are limited to `north`, `south`, `east`, and `west`

#### `Bus.py`

* Goes through any 🟡 or 🟢 light and keeps doing so until it hits a 🔴
* Stops if lights are 🔴

The `Bus.py` also previews some content we'll get to in time. However, you can know that the process
by which the `Bus` should move forward is (in this order):

```python
direction = Bus.__get_direction()
stoplight = Bus.__get_light(direction)
Bus.__report(direction, stoplight)
```

This file uses a `while` loop which _repeats_ procedures. Minus some small logic, the above is pretty much the full functionality of the vehicle.

### Collaborative reflection

**Create one branch called `reflection` to capture your work on this section of the assignment; all members should contribute to the same branch.**

All of the above tasks completed, finish the collaborative reflection located in the `office`.

## Making an improvement proposal

This assignment begins your opportunity to propose and improve the world of `term-world` at-large. For this assignment, proposals may include making graphics to improve the `bodega` site experience, creating new items or actions in the `traffic-circle` itself or another assignment-related improvement not contemplated in the prior narrow categories.

To make an improvement proposal, you must _create an issue_ on this repository. Do so by:

* clicking the `Issues` tab at the top of the page.
* clicking the green `New Issue` button
* selecting the `Improvement Proposal` template 

**You must fill out the entire template and wait for Mayoral approval before starting the improvement.**

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
