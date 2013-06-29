# Do not import any modules. If you do, the tester may reject your submission.
 
# Constants for the contents of the maze.
 
# The visual representation of a wall.
WALL = '#'
 
# The visual representation of a hallway.
HALL = '.'
 
# The visual representation of a brussels sprout.
SPROUT = '@'
 
# Constants for the directions. Use these to make Rats move.
 
# The left direction.
LEFT = -1
 
# The right direction.
RIGHT = 1
 
# No change in direction.
NO_CHANGE = 0
 
# The up direction.
UP = -1
 
# The down direction.
DOWN = 1
 
# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'
 
 
class Rat:
    """ A rat caught in a maze. """
 
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType
 
        Creates an instance of a Rat with variables symbol, row, col, num_sprouts_eaten.
 
        >>> Rat('P', 1, 4)
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
         
 
    def __str__(self):
        """ (Rat) -> str
 
        This method returns the string representation of a rat.
 
        >>> r1 = Rat('z', 1, 2)
        print(r1)
        >>> "z at (1, 2) ate 0 sprouts."
        """
        return '{0} at {1}, {2} ate {3} sprouts'.format(str(self.symbol),
                 str(self.row), str(self.col), str(self.num_sprouts_eaten))
 
 
    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType
 
        This method sets the rats location in the maze.
 
        >>> r1 = Rat('r1', 0, 0)
        >>> r1.row
        0
        >>> r1.col
        0
        >>> r1.set_location(2, 4)
        >>> r1.row
        2
        >>> r1.col
        4
        """
        self.row = row
        self.col = col
 

    def get_location(self):
        """ (Rat) -> (int, int)
 
        Return the index of the rat in the form (row, col).
 
        >>> r1 = Rat('r1', 0, 0)
        >>> r1.get_location()
        (0, 0)
        """
        return (self.row, self.col)
 

    def eat_sprout(self):
        """ (Rat) -> NoneType
 
        Increases the num_of_sprouts eaten by 1.
         
        >>> r1 = Rat('r1', 1, 2)
        >>> r1.num_sprouts_eaten
        0
        >>> r1.eat_sprout()
        >>> r1.num_sprouts_eaten
        1
         
        """
        self.num_sprouts_eaten += 1
     
 
class Maze:
    """ A 2D maze. """
 
 
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
 
        Initilizes a maze. A maze is a 2 dimensional array of symbols representing
        walls, hallway, sprouts, or rats. Notice the rat symbols do not appear in the
        2 dimensional array maze.
 
        >>> Maze([['#', '#', '#', '#', '#', '#', '#'], 
          ['#', '.', '.', '.', '.', '.', '#'], 
          ['#', '.', '#', '#', '#', '.', '#'], 
          ['#', '.', '.', '@', '#', '.', '#'], 
          ['#', '@', '#', '.', '@', '.', '#'], 
          ['#', '#', '#', '#', '#', '#', '#']], 
          Rat('J', 1, 1),
          Rat('P', 1, 4))
        """
        num_sprouts = 0
 
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == SPROUT:
                    num_sprouts += 1
         
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = num_sprouts
    
 
    def __str__(self):
        res = ""
        rows = len(self.maze)
        cols = len(self.maze[0])
        for i in range(rows):
            for j in range(cols):
                char = self.get_character( i, j )
                res += char
            res += "\n"
        res += str(self.rat_1)
        res += "\n"
        res += str(self.rat_2)
        return res

    
    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool
 
        Checks if the corresponding row and col index is a wall. Returns True
        if and only if there is a wall at that location.
 
        >>> m1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
          ['#', '.', '.', '.', '.', '.', '#'], 
          ['#', '.', '#', '#', '#', '.', '#'], 
          ['#', '.', '.', '@', '#', '.', '#'], 
          ['#', '@', '#', '.', '@', '.', '#'], 
          ['#', '#', '#', '#', '#', '#', '#']], 
          Rat('J', 1, 1),
          Rat('P', 1, 4))
        >>> m1.is_wall(0, 0)
        True
        >>> m1.is_wall(1, 1)
        False
        """
        return self.maze[row][col] == WALL
 
 
    def get_character(self, row, col):
        """ (Maze, int, int) -> str
 
        Return thecharacter in the maze at the given row and col. If there is
        a rat at that location then its character should be return rather than
        the symbol representation
 
        >>> m1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
          ['#', '.', '.', '.', '.', '.', '#'], 
          ['#', '.', '#', '#', '#', '.', '#'], 
          ['#', '.', '.', '@', '#', '.', '#'], 
          ['#', '@', '#', '.', '@', '.', '#'], 
          ['#', '#', '#', '#', '#', '#', '#']], 
          Rat('J', 1, 1),
          Rat('P', 1, 4))
        >>> m1.get_character(0, 0)
        WALL
        >>> m1.get_character(1, 1)
        HALL
        >>> m1.get_character(3, 3)
        SPROUT
        """
        if self.rat_1.get_location() == (row, col):
            return self.rat_1.symbol
        elif self.rat_2.get_location() == (row, col):
            return self.rat_2.symbol
        else:
            return self.maze[row][col]
 
 
    def set_character(self, row, col, maze_char):
        """ (Maze, int, int, ) -> NoneType
 
        Update the char in the maze to maze_char in the location Maze[row][col]
 
        maze_char can only be be: WALL, HALL, or SPROUT
        >>> m1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
          ['#', '.', '.', '.', '.', '.', '#'], 
          ['#', '.', '#', '#', '#', '.', '#'], 
          ['#', '.', '.', '@', '#', '.', '#'], 
          ['#', '@', '#', '.', '@', '.', '#'], 
          ['#', '#', '#', '#', '#', '#', '#']], 
          Rat('J', 1, 1),
          Rat('P', 1, 4))
        >>> m1.set_char(1, 1, WALL)
        >>> m1
        [['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']] 
        
        """
        self.maze[row][col] = maze_char
         
 
    def move(self, rat, vert_direction, horiz_direction):
        """ (Maze, Rat, int, int) -> bool
 
        Move the rat in the given direction.
         
        Move UP if vert_direction == -1.
        Move DOWN if vert_direction == 1.
        Move LEFT if horiz_direction == -1.
        Move RIGHT if horiz_direction == 1.
        If either parameter is 0, NO CHANGE in that direction.
        """
        new_x_location = rat.row + vert_direction
        new_y_location = rat.col + horiz_direction
        # Check if the attempted space is a wall
        if self.get_character(new_x_location, new_y_location)  == WALL:
            return False
        else:
            # Check if the mouse ate a sprout and set that spot to hall
            if self.get_character(new_x_location, new_y_location) == SPROUT:
                rat.eat_sprout()
                self.set_character(new_x_location, new_y_location, HALL)
                self.num_sprouts_left -= 1
            #Move the mouse
            rat.set_location(new_x_location, new_y_location)
            return True
 
     
    
         
if __name__ == "__main__":
 
    Jen = Rat(RAT_1_CHAR,1,4)
    print(Jen)
     
    Jen.set_location(2,5)
    Jen.eat_sprout()
    print(Jen)
 
    Paul = Rat(RAT_2_CHAR, 3, 5 )
 
    test = Maze([['#', '#', '#', '#', '#', '#', '#'], 
      ['#', '.', '.', '.', '.', '.', '#'], 
      ['#', '.', '#', '#', '#', '.', '#'], 
      ['#', '.', '.', '@', '#', '.', '#'], 
      ['#', '@', '#', '.', '@', '.', '#'], 
      ['#', '#', '#', '#', '#', '#', '#']], 
      Jen,
      Paul)
 
    print(test)
