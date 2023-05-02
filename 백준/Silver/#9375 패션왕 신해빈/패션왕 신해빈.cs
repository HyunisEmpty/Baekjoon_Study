using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		int test_case = int.Parse(Console.ReadLine());
		int type;
		Dictionary<string, int> clothes = new Dictionary<string, int>();
		string[] input;
		int all_type;
		
		for(int test = 0; test < test_case; test++){
			
			type = int.Parse(Console.ReadLine());
			clothes.Clear();
			all_type = 1;
			
			for(int i = 0; i < type; i++){
				
				input = Console.ReadLine().Split();
				
				if(clothes.ContainsKey(input[1])){
					clothes[input[1]] += 1;
				}else{
					clothes.Add(input[1], 2);
				}
				
			}
			
			foreach(int val in clothes.Values){
				all_type = all_type * val;
			}
			
			Console.WriteLine(all_type-1);
			
		}
	} 
}