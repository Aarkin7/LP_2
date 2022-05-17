#include<iostream>
#include<list>
#include<queue>
using namespace std;


class Graph{

	int V;
	list<int> *l;

public:
	Graph(int v){
		V = v;
		l = new list<int>[V];
	}

	void addEdge(int i,int j,bool undir=true){
		l[i].push_back(j);
		if(undir){
			l[j].push_back(i);
		}
	}
	void bfs(int source){

		queue<int> q;
		bool *visited = new bool[V]{0};

		q.push(source);
		visited[source] = true;

		while(!q.empty()){
			//Do some work for every node
			int f = q.front();
			cout<<f <<endl;
			q.pop();

			//PUsh the nbrs of current node inside q if they are not already visited
			for(auto nbr : l[f]){
				if(!visited[nbr]){
					q.push(nbr);
					visited[nbr] = true;
				}
			}
		}
	}
	
	

};

int main(){
	Graph g(7);
	g.addEdge(0,1);
	g.addEdge(1,2);
	g.addEdge(2,3);
	g.addEdge(3,5);
	g.addEdge(5,6);
	g.addEdge(4,5);
	g.addEdge(0,4);
	g.addEdge(3,4);
	g.bfs(1);
	return 0;
}


// TC for adjacency list: O(V+E) 
//TC for adjacency matrix: O(V^2)
// V -> No of nodes
// E -> No of edges

// S.No        	BFS	DFS
// 1.	BFS stands for Breadth First Search.	DFS stands for Depth First Search.
// 2.	BFS(Breadth First Search) uses Queue data structure for finding the shortest path.	DFS(Depth First Search) uses Stack data structure.
// 3.	BFS can be used to find single source shortest path in an unweighted graph, because in BFS, we reach a vertex with minimum number of edges from a source vertex.	In DFS, we might traverse through more edges to reach a destination vertex from a source.
// 4.	BFS is more suitable for searching vertices which are closer to the given source.	DFS is more suitable when there are solutions away from source.
// 5.	BFS considers all neighbors first and therefore not suitable for decision making trees used in games or puzzles.	DFS is more suitable for game or puzzle problems. We make a decision, then explore all paths through this decision. And if this decision leads to win situation, we stop.
// 6.	The Time complexity of BFS is O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.	The Time complexity of DFS is also O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.
// 7.	Here, siblings are visited before the children	Here, children are visited before the siblings
// 8.	In BFS there is no concept of backtracking. 	DFS algorithm is a recursive algorithm that uses the idea of backtracking
// 9.	BFS is used in various application such as  bipartite graph, and shortest path etc.	DFS is used in various application such as acyclic graph and topological order etc.
// 10.	BFS requires more memory. 	DFS requires less memory. 


//The space complexity for BFS is O(w) where w is the maximum width of the tree



