using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	
	public static void Dfs(Stack<int> d_stack, List<string> d_answer_list, Dictionary<int, List<int>> d_tree_dic, HashSet<int> d_set){	
		
		int d_parent_node = d_stack.Pop();
		string d_parent_node_str = Convert.ToString(d_parent_node);
		d_answer_list.Add(d_parent_node_str);
			
		foreach(int child_node in d_tree_dic[d_parent_node]){
			// 자식 노드가 만약 방문한전 없는 노드라면
			if(!d_set.Contains(child_node)){
				d_stack.Push(child_node);
				// 자식 노드에게 접근하는 순간 다른 노드에서 접근할 수 없도록 한다.
				d_set.Add(child_node);
				Dfs(d_stack, d_answer_list, d_tree_dic, d_set);
			}
		}
	}
	
	public static void Main() {
		
		int[] input_int = Console.ReadLine().Split().Select(int.Parse).ToArray();
		int node_count = input_int[0];
		int edge_count = input_int[1];
		int root_node = input_int[2];
		
		Dictionary<int, List<int>> tree_dic = new Dictionary<int, List<int>>();
		
		// 부모가 누구인지 정의 되지 않은 무방향 그래프를 딕셔너리를 통해 구현
		for(int i = 0; i < edge_count; i++){
			input_int = Console.ReadLine().Split().Select(int.Parse).ToArray();
			
			int node_x = input_int[0];
			int node_y = input_int[1];
			
			if(tree_dic.ContainsKey(node_x)){
				tree_dic[node_x].Add(node_y);
			}else{
				tree_dic.Add(node_x, new List<int> { node_y });
			}
			
			if(tree_dic.ContainsKey(node_y)){
				tree_dic[node_y].Add(node_x);
			}else{
				tree_dic.Add(node_y, new List<int> { node_x });
			}
			
		}
		
		// 모든 키(부모)에 해당 하는 값(자식)을 오름차순으로 정렬해야한다.
		foreach(int key in tree_dic.Keys){
			tree_dic[key].Sort();
		}
		
		// 집합을 통해 사이클 구조를 방지하며 트리형태로 구현.
		HashSet<int> bfs_set = new HashSet<int>();
		bfs_set.Add(root_node);
		HashSet<int> dfs_set = new HashSet<int>();
		dfs_set.Add(root_node);
		
		// BFS, DFS를 구현하기 위한 스택과 큐
		Queue<int> bfs_queue = new Queue<int>(new[] { root_node });
		Stack<int> dfs_stack = new Stack<int>(new[] { root_node });
		
		
		if(tree_dic.ContainsKey(root_node)){
			// DFS
			List<string> dfs_answer_list = new List<string>();
			while(dfs_stack.Count != 0){
				main.Dfs(dfs_stack, dfs_answer_list, tree_dic, dfs_set);
			}


			// BFS
			List<string> bfs_answer_list = new List<string>();
			int bfs_parent_node;
			string bfs_parent_node_str;
			while(bfs_queue.Count != 0){

				bfs_parent_node = bfs_queue.Dequeue();

				bfs_parent_node_str = Convert.ToString(bfs_parent_node);
				bfs_answer_list.Add(bfs_parent_node_str);

				foreach(int child_node in tree_dic[bfs_parent_node]){
					// 자식 노드가 만약 방문한전 없는 노드라면
					if(!bfs_set.Contains(child_node)){
						bfs_queue.Enqueue(child_node);
						// 자식 노드에게 접근하는 순간 다른 노드에서 접근할 수 없도록 한다.
						bfs_set.Add(child_node);
					}
				}
			}


			// DFS 출력 
			string dfs_answer = string.Join(" ", dfs_answer_list);
			Console.WriteLine(dfs_answer);


			// BFS 출력 
			string bfs_answer = string.Join(" ", bfs_answer_list);
			Console.WriteLine(bfs_answer);
		}else{
			Console.WriteLine(root_node);
			Console.WriteLine(root_node);
		}
	} 
}