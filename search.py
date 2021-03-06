# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        #Returns True if and only if the state is a valid goal state.

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
     """
     Search the deepest nodes in the search tree first.

     Your search algorithm needs to return a list of actions that reaches the
     goal. Make sure to implement a graph search algorithm.

     To get started, you might want to try some of these simple commands to
     understand the search problem that is being passed in:
     #here i inspired the code from another place
     print "Start:", problem.getStartState()
     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
     print "Start's successors:", problem.getSuccessors(problem.getStartState())
     """
     "*** YOUR CODE HERE ***"
     fringe = util.Stack()  # Fringe (Stack) to store the nodes along with their paths
     visited = set()  # A set to maintain all the visited nodes
     node = problem.getStartState()
     fringe.push((node, []))  # Pushing (Node, [Path from start-node till 'Node']) to the fringe
     while True:
         popped_element = fringe.pop()
         node = popped_element[0]
         path_to_node = popped_element[1]
         if problem.isGoalState(node):
             break

         else:
             if node not in visited:
                 visited.add(node)
                 successors_list = problem.getSuccessors(node)  # contain(nextpossible node,direcion to it,cost)
                 for successor in successors_list:
                     current_node_child = successor[0]
                     direction_to_child = successor[1]  # string
                     path_to_child_from_start = path_to_node + [direction_to_child]
                     fringe.push((current_node_child, path_to_child_from_start))
                     # print "Successors:", problem.getSuccessors(node)
     # print "Start:", problem.getStartState()
     # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
     return path_to_node
     util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    visited = set()
    node_and_corners = problem.getStartState()  # start node it self and cornersLeft
    fringe.push((node_and_corners, []))         #start node and path to it
    while True:
        popped_element = fringe.pop()
        node_and_corners = popped_element[0]  # node
        print 'state', node_and_corners
        node = node_and_corners[0]
        path_to_node = popped_element[1]
        if problem.isGoalState(node_and_corners):
          print "Goal condition true"
          break  #every time i am in a corner
        else:
          if node not in visited:
            visited.add(node)
            successors_list = problem.getSuccessors(node_and_corners)#contain(nextpossible node,direcion to it,cost)
            for successor in successors_list:
                current_node_child = successor[0][0]
                current_node_corners = successor[0][1]
                direction_to_child = successor[1] #string
                path_to_child_from_start = path_to_node+ [direction_to_child]
                fringe.push(([current_node_child,current_node_corners],path_to_child_from_start))
                #print "Successors:", problem.getSuccessors(node)
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    return path_to_node
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    visited = set()
    node = problem.getStartState() # start node it self
    fringe.push((node, [],0),0)  # start node and path to it
    while True:
        popped_element = fringe.pop()
        node = popped_element[0][0]
        path_to_node = popped_element[1]
        cost_to_node = popped_element[2]
        if problem.isGoalState(node):
            break
        else:
            if node not in visited:
                visited.add(node)
                successors_list = problem.getSuccessors(node)  # contain(nextpossible node,direcion to it,cost)
                for successor in successors_list:
                    current_node_child = successor[0][0]
                    direction_to_child = successor[1]  # string
                    cost_to_child = successor[2]  # string
                    cost_from_start_to_child = cost_to_node + cost_to_child
                    path_to_child_from_start = path_to_node + [direction_to_child]
                    fringe.push((current_node_child, path_to_child_from_start,cost_from_start_to_child),cost_from_start_to_child)
                    # print "Successors:", problem.getSuccessors(node)
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    return path_to_node
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    visited = set()
    node_and_corners = problem.getStartState()  # start node it self and cornersLeft
    fringe.push((node_and_corners,[],0), heuristic(problem.getStartState(), problem) + 0)  # start node and path to it
    while True:
        popped_element = fringe.pop()
        node_and_corners = popped_element[0]   #node
        print 'mlll',node_and_corners
        node = node_and_corners[0]
        path_to_node = popped_element[1]
        cost_to_node = popped_element[2]
        #print "node", node, "corn", corners,"path_",path_to_node,"cost",cost_to_node
        if problem.isGoalState(node_and_corners):
            break
        else:
            if node not in visited:
                visited.add(node)
                successors_list = problem.getSuccessors(node_and_corners)  # contain(nextpossible node,direcion to it,cost)
                for successor in successors_list:
                    current_node_child = successor[0][0]
                    current_node_corners = successor[0][1]
                    direction_to_child = successor[1]  # string
                    cost_to_child = successor[2]  # string
                    cost_from_start_to_child = cost_to_node + cost_to_child
                    path_to_child_from_start = path_to_node + [direction_to_child]
                    fringe.push(([current_node_child,current_node_corners], path_to_child_from_start,cost_from_start_to_child),cost_from_start_to_child+heuristic(current_node_child,problem))
                    # print "Successors:", problem.getSuccessors(node)
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    return path_to_node
    util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
