# ai-vacuum-cleaning-agent
̆Python program that implements an A* search to operate a vacuum cleaning agent

This program is adapted from an open-source implementation found here:
https://github.com/aimacode/aima-python

The imported files search.py and util.py are both taken directly from the
open-source repository. The class VacuumProblem is extended from the search.py
class Problem. No additional packages are required to run this program.

This program utilizes the A* search algorithm to implement the vacuum cleaning agent
problem. The initial state is a 5x5 grid, in which the starting space is at (1,1) and
the top five spaces are dirty. This program prints the optimal sequence of actions to
clean the five dirty squares, the path cost, and the number of nodes expanded upon using
algorithms h1 and h2.
