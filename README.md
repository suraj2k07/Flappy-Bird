# Pygame Flappy Bird Clone

## Overview

This is a simple clone of the classic **Flappy Bird** game implemented using the **Pygame** library in Python. The objective is to control a bird and navigate it through a series of vertical pipes without hitting them or the ground/ceiling. The game includes basic physics (gravity, flapping) and difficulty scaling over time.

---

## Features

-   **Physics Engine**: Implements gravity and jump mechanics for the bird's movement.
-   **Collision Detection**: Accurate rectangle-based collision detection for pipes, ceiling, and floor.
-   **Difficulty Scaling**: The pipe speed and score multiplier increase every **120 seconds**.
-   **Scoring System**: Tracks and displays the player's score.
-   **Restart/Quit**: Allows the user to restart the game or quit from the Game Over screen.
-   **Visuals**: Includes bird rotation to enhance user experience.

---

## Prerequisites

To run this game, you must have the **Pygame** library installed.

1.  **Install Pygame**:
    ```bash
    pip install pygame
    ```
2.  **Required Asset**:
    -   A file named `bird.png` must be present in the same directory as the Python script.

---

## Installation and Execution

1.  **Save the Code**: Save the provided Python code into a file named `flappy_bird.py`.
2.  **Add the Image**: Ensure your `bird.png` image is in the same folder.
3.  **Run the Game**: Open your terminal or command prompt, navigate to the directory where you saved the files, and execute the script:

    ```bash
    python flappy_bird.py
    ```

---

## How to Play

1.  **Start**: The game begins immediately upon launch.
2.  **Flap**: Press the **SPACEBAR** or the **UP Arrow** key to make the bird flap upwards.
3.  **Scoring**: You earn **10 points** for successfully passing through the gap of a pipe. This score is multiplied by the current **Speed/Difficulty** level.
4.  **Game Over**: The game ends if the bird:
    -   Collides with the top or bottom pipe.
    -   Hits the top (ceiling) or bottom (floor) of the screen.
5.  **Restart**: On the **GAME OVER** screen, press the **SPACEBAR** to start a new game, or **ESC** to quit.
