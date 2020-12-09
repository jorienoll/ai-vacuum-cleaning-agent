from search import *

class VacuumProblem(Problem):
    def __init__(self, initial, goal=()):
        #Inherits class Problem.
        super().__init__(initial, goal)
        self.total_cost = 0

    def actions(self, state):
        # Returns the possible actions the agent can perform in a given state.

        actions = ['left', 'right', 'up', 'down', 'suck']
        x, y = state[0]

        # If the vacuum is on the left edge of 5x5 grid, remove action move left.
        if x == 1:
            actions.remove('left')
        # If the vacuum is on the rught edge of 5x5 grid, remove action move right.
        if x == 5:
            actions.remove('right')
        # If the vacuum is on the bottom edge of 5x5 grid, remove action move down.
        if y == 1:
            actions.remove('down')
        # If the vacuum is on the top edge of 5x5 grid, remove action move up.
        if y == 5:
            actions.remove('up')
        # If the square is not dirty, remove action suck.
        if (x, y) not in state[1]:
            actions.remove('suck')

        return actions

    def result(self, state, action):
        # Return the state that results from executing an action in original state.

        new_state = list(state)
        x, y = state[0]

        # If the vacuum moves left, change the (x, y) location by decrementing x coordinate.
        if action == 'left':
            x -= 1
        # If the vacuum moves right, change the (x, y) location by incrementing x coordinate.
        elif action == 'right':
            x += 1
        # If the vacuum moves down, change the (x, y) location by decrementing y coordinate.
        elif action == 'down':
            y -= 1
        # If the vacuum moves up, change the (x, y) location by incrementing y coordinate.
        elif action == 'up':
            y += 1
        # If the vacuum performs suck, change state of s1. Remove current location (x, y)
        # from array of dirty squares.
        else:
            new_state[1] = list(state[1])
            new_state[1].remove((x, y))
            new_state[1] = tuple(new_state[1])

        # Set new state after executing actions.
        new_state[0] = list(state[0])
        new_state[0] = [x, y]
        new_state[0] = tuple(new_state[0])

        return tuple(new_state)

    def goal_test(self, state):
        #Return True if the state is a goal.

        return state[1] == self.goal

    def path_cost(self, c, state1, action, state2):
        # Return the cost of a solution path that arrives at state2 from state1 via action,
        # assuming cost c to get up to state1.

        self.total_cost = 1 + c + 2 * len(state2[1])
        return self.total_cost

    def remaining_dirty(self, count, state):
        # Return cost of remaining dirty spaces.

        # Calculate the cost of remaining dirty spaces.
        cost = 0
        for dirty in state[1]:
            countX, countY = count
            x, y = dirty

            if abs(y - countY) < 0 and abs(x - countX) < 0 and count != dirty:
                cost += 1

        return cost

    def clean_next(self, state):
        # Return the next dirty square to be cleaned by finding the closest dirty square.

        # Choose the next dirty square by calculating the distance to the nearest dirty square.
        closest = [[0,0], 5000]
        for dirty in state[1]:
            dirty_distance = distance(state[0], dirty)

            if  dirty_distance < closest[1]:
                closest = [dirty, dirty_distance]
                
        return closest
        
    def h1(self, node):
        # Return the heuristic value for a given state using h1.

        # Get the location and distance of the next dirty square to be cleaned.
        nearest_dirty, dirty_distance = self.clean_next(node.state)        

        # Calculate the cost of h(1).
        return self.remaining_dirty(tuple(nearest_dirty), node.state) - dirty_distance

    def h2(self, node):
        # Return the heuristic value for a given state using h2.

        # Get the location and distance of the next dirty square to be cleaned.
        nearest_dirty, dirty_distance = self.clean_next(node.state)        

        # Calculate the cost of h(1).
        return self.remaining_dirty(tuple(nearest_dirty), node.state)

# ___________________________________________________________________________________________________________
# Main method inputs and solves a problem using Class VacuumProblem, which inputs the initial state location
# vertex and vertices of dirty squares.

problem = VacuumProblem(((1,1),((1,5),(2,5),(3,5),(4,5),(5,5))))

print("__________________________________________________________________________________________________________")
print("H1(n): ")
# Print the optimal action sequence to solve problem using A* search using heuristic funciton h1.
print("Optimal path:", astar_search(problem, problem.h1, True).solution())

# Print the optimal path's cost. 
print("Optimal path cost:", problem.total_cost)

print("")
print("H2(n): ")
# Print the optimal action sequence to solve problem using A* search using heuristic function h2.
print("Optimal path:", astar_search(problem, problem.h2, True).solution())

# Print the optimal path's cost. 
print("Optimal path cost:", problem.total_cost)
print("__________________________________________________________________________________________________________")