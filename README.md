A simple maze solver
==================

Solved a maze posted on [StackOverflow](http://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image), using Breadth-first search.

The post asked to solve the following image:
![image](https://raw.githubusercontent.com/liloboy/simple-maze-solver/master/original.jpg)

As suggested in the answers I used [GIMP](http://www.gimp.org/) to:
* Convert image to grayscale (not yet binary), adjusting weights for the colors so that final grayscale image is approximately uniform.
* Convert image to binary by setting appropriate threshold.
* Make sure threshold is selected right. Use the Magic Wand Tool with 0 tolerance, point sample, contiguous, no anti-aliasing. Check that edges at which selection breaks are not false edges introduced by wrong threshold. In fact, all interior points of this maze are accessible from the start.
* Add artificial borders on the maze to make sure virtual traveler will not walk around it.
* Implement breadth-first search and run it from the start, searching for the end.

Obtaining:
![image](https://raw.githubusercontent.com/liloboy/simple-maze-solver/master/binary.gif)

The output of [solve_maze.py](https://github.com/liloboy/simple-maze-solver/blob/master/solve_maze.py):
![image](https://raw.githubusercontent.com/liloboy/simple-maze-solver/master/solved.png)

