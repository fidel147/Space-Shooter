# Space Shooter

A small 2D space shooter built with Python and Pygame. Pilot the ship, destroy incoming meteors, and survive as long as possible while your score increases.

## Features

- Player movement with keyboard controls
- Laser shooting with a short cooldown
- Meteor spawning, movement, rotation, and collisions
- Animated explosions with sound effects
- Background music and an elapsed-time score

## Requirements

- Python 3.10 or newer
- Pygame 2.5 or newer

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/fidel147/Space-Shooter.git
cd Space_Shooter
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Run the game

Run this command from the repository root so the game can find its image and audio assets:

```bash
python scr/main.py
```

## Controls

| Action | Key |
| --- | --- |
| Move | Arrow keys |
| Shoot | Space |
| Quit | Escape or close the game window |

## Project structure

```text
Space_Shooter/
├── audio/                 # Music and sound effects
├── images/                # Sprites, font, and explosion frames
├── scr/
│   ├── main.py            # Game setup and main loop
│   ├── player.py          # Player, laser, and meteor sprites
│   ├── explosion.py       # Animated explosion sprite
│   └── settings.py        # Asset paths and game settings
├── requirements.txt
└── README.md
```

## Credits

Created by Fidele ZOGBE as a Pygame learning project.
