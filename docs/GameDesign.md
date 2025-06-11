# Ball Blaster - Game Design Document

## Overview
Ball Blaster is a lightweight arcade shooter meant to demonstrate how to build a
complete indie-style game using Python and Pygame. The player controls a blue
ball that must fend off an endless wave of enemy squares. The gameplay is fast
paced and suitable for quick play sessions.

## Core Mechanics
- **Movement:** The player ball can move in four directions using the arrow keys
  or the W, A, S, D keys.
- **Shooting:** Press the Space bar to fire bullets upward. Bullets can destroy
enemy squares on contact.
- **Enemies:** Squares spawn at the top of the screen and travel downward. If an
enemy collides with the player, the player loses one life.
- **Scoring:** Each destroyed enemy is worth one point. Every 10 points
  increases the level and slightly speeds up enemy spawn frequency and
  movement speed.
- **Lives:** The player starts with three lives. When all lives are lost, the
  game ends and the score is displayed.

## Art and Assets
This demo intentionally keeps graphics minimal. Shapes are drawn directly in
Pygame without relying on external image files, making the project easy to run
anywhere.

## Extending the Game
The code is designed to be short and easy to read. You can build on it by adding
more enemy types, power-ups, sounds, or even a start menu.
