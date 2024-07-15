# The Last Cowboy
#### Video Demo: https://youtu.be/ZAVpwm0gQ4U
#### Description: Game project for CS50P using Pygame

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/cochisealfonso/project">
    <img src="readme_images/cowboy_icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">The Last Cowboy</h3>

  <p align="center">
    CS50P Final Project created using PyGame
    <br />
    <a href="https://youtu.be/ZAVpwm0gQ4U">View Demo</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">How to Play</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Game Screen Shot][product-screenshot]

This is a final project submission for Harvard's CS50P: Introduction to Programming with Python. It is a simple Space Invader-like game, but with a different orientation (horizontal), with the enemies approaching from right to left.

The game is implemented using Pygame.

### Source Files

There are three (3) classes made for this game, `bullet.py`, `enemy.py`, and `player.py`. Each of these classes has its own `XPos` and `YPos` component, which is their position on the screen.

<br />

`~\bullet.py`

The bullet class contains the `fire()` function. This is the function that determines whether the bullet should start to move from the current position of the player all the way to the right-end of the screen.

<br />

`~\enemy.py`

The enemy class contains the `spawn()` function. This randomly spawns the enemies at a random `YPos` or Y-axis. All of the enemies are determined to be spawned at a fixed `XPos`.

<br />

`~\player.py`

The enemy class contains the `move()` function. This determines the keys that moves the player's character and the speed of its movement. This also determines the boundaries where the character is allowed to move.

<br />

`~\project.py`

This is the main file of the game. This contains the `main()`, `set_window()`, `collision()`, and the  `show_score()` functions.

`set_window()` - This sets the size, caption, icon, and background image to be displayed in the window.

`collision()` - This computes the distance of the position of the bullet and the position of the enemy. When the distance reaches a certain value, it returns a boolean value, indicating that a collision has occurred.

`show_score()` - This function simply displays the current score of the player.

The `main()` function is where all of these are initialized and executed. It starts with initializing __Pygame__. We then initialize the screen and window that will be displayed followed by all the images needed.

The function then instatiates the `player`, `bullet`, and four (4) `enemies`.

All of the needed variables are then named and assigned initial values.

The succeeding code are separated by three while loops using the `running` variable. These screens are the Intro, Main Game, and the End Game screen.

The __Intro__ displays the instructions on how to control the character and how to fire a bullet.

After hitting the ENTER key, the game starts and the __Main Game__ screen is displayed.

The __End Game__ screen only triggers when the game ends, that is, when an enemy reaches the rope. It will then display the score of the player and the game can be closed from there.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

![Pygame Logo][pygame-logo]

__Pygame__ is a set of Python modules designed for writing games. It is written on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language. Pygame is highly portable and runs on nearly every platform and operating system.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Pygame requires Python; if you don't already have it, you can download it from [python.org](https://python.org)

The best way to install pygame is with the pip tool (which is what python uses to install packages). Note, this comes with python in recent versions. We use the --user flag to tell it to install into the home directory, rather than globally.

   ```sh
   python3 -m pip install -U pygame --user
   ```
### Installation


1. Clone the repo

   ```sh
   git clone https://github.com/cochisealfonso/project.git
   ```
2. Run the game

   ```sh
   python .\project.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## How to Play


The player only has __one (1)__ bullet to shoot.

The player can move __UP__, __DOWN__, __LEFT__, or __RIGHT__ using `W A S D` keys.

To shoot a bullet, hit the `SPACE BAR`.

The player can only re-shoot a bullet when it either hits an enemy or it reaches the end of the screen.

Each enemy can be killed by a bullet, and every kill is __one (1) point__.

When the enemy reaches the rope, the game ends.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Cochise - cochisedelacruz@gmail.com

Project Link: [https://github.com/cochisealfonso/project](https://github.com/cochisealfonso/project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Special thanks to all the resources that made this project possible.

* [CS50P](https://cs50.harvard.edu/python/2022/)
* [Python](https://www.python.org/)
* [Pygame](https://www.pygame.org/)
* [freeCodeCamp](https://www.freecodecamp.org/)
* [Flaticon](https://www.flaticon.com/)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: readme_images/game_screenshot.png
[pygame-logo]: readme_images/pygame_logo.png