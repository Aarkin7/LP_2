class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_') # to get x&y coordinates
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]] # 1st left then right then up then down
        children = []
        for i in val_list:  # runs for 4 times
            child = self.shuffle(self.data,x,y,i[0],i[1])   # after swapping the position of _
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children # children contains all possible combinations
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)  # stores a copy of the given matrix
            temp = temp_puz[x2][y2]  #x2,y2 are the coordinates of an adjacent cell
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp   # swapping their positions
            return temp_puz
        else:   # if x2,y2 are out of bounds
            return None
            

    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:   # root is a matrix
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size  # the size is 3 by default
        self.open = []
        self.closed = []

    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")  # enter 3 space separated numbers
            puz.append(temp)
        return puz

    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        

    def process(self):
        """ Accept Start and Goal Puzzle state"""
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")        
        goal = self.accept()

        start = Node(start,0,0)  #level, fvl, start is an object
        start.fval = self.f(start,goal)
        print('start fval = ',start.fval)
        """ Put the start node in the open list"""
        self.open.append(start)  
        print("\n\n")
        while True:
            cur = self.open[0]
            
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:  # cur.data is a matrix
                
                for j in i:  # j is the ith row
                    print(j,end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):  # if the current matrix is equal to the goal matrix, break the loop
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal) # fval to store the hueristic value
                self.open.append(i)
            self.closed.append(cur)
            
            del self.open[0]

            """ sort the opne list based on fval """
            self.open.sort(key = lambda x:x.fval,reverse=False)


puz = Puzzle(3)
puz.process()

'''output

Enter the start state matrix

1 2 3
_ 4 6
7 5 8
Enter the goal state matrix

1 2 3
4 5 6
7 8 _
start fval =  3




  |
  |
 \'/

1 2 3
_ 4 6
7 5 8

  |
  |
 \'/

1 2 3
4 _ 6
7 5 8

  |
  |
 \'/

1 2 3
4 5 6
7 _ 8

  |
  |
 \'/

1 2 3
4 5 6     <---------- expected matrix
7 8 _


'''




# Time Complexity 
# Considering a graph, it may take us to travel all the edge to reach the destination cell from the source cell [For example, consider a graph where source and destination nodes are connected by a series of edges, like – 0(source) –>1 –> 2 –> 3 (target)
# So the worse case time complexity is O(E), where E is the number of edges in the graph

# Auxiliary Space In the worse case we can have all the edges inside the open list, so required auxiliary space in worst case is O(V), where V is the total number of vertices.

# Limitations 
# Although being the best path finding algorithm around, A* Search Algorithm doesn’t produce the shortest path always, as it relies heavily on heuristics / approximations to calculate – h

# Applications 
# This is the most interesting part of A* Search Algorithm. They are used in games! But how?
# Ever played Tower Defense Games ? 
# Tower defense is a type of strategy video game where the goal is to defend a player’s territories or possessions by obstructing enemy attackers, usually achieved by placing defensive structures on or along their path of attack. 
# A* Search Algorithm is often used to find the shortest path from one point to another point. You can use this for each enemy to find a path to the goal.
# One example of this is the very popular game- Warcraft III 

# What if the search space is not a grid and is a graph ?
# The same rules applies there also. The example of grid is taken for the simplicity of understanding. So we can find the shortest path between the source node and the target node in a graph using this A* Search Algorithm, just like we did for a 2D Grid.



# Summary 
# So when to use BFS over A*, when to use Dijkstra over A* to find the shortest paths ? 
# We can summarise this as below-
# 1) One source and One Destination- 
# → Use A* Search Algorithm (For Unweighted as well as Weighted Graphs)
# 2) One Source, All Destination – 
# → Use BFS (For Unweighted Graphs) 
# → Use Dijkstra (For Weighted Graphs without negative weights) 
# → Use Bellman Ford (For Weighted Graphs with negative weights)
# 3) Between every pair of nodes- 
# → Floyd-Warshall 
# → Johnson’s Algorithm