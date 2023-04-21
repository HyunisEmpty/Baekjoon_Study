using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		int n = int.Parse(Console.ReadLine());
		List<int> queue = new List<int>();
		
		for(int i = 0; i < n; i++){
			string input = Console.ReadLine();
			string[] command = input.Split();
			
			if(command[0] == "push"){
				queue.Add(int.Parse(command[1]));
			}
			if(command[0] == "pop"){
				if(queue.Count != 0){
					Console.WriteLine(queue[0] + "");
					queue.Remove(queue[0]);	
				}else{
					Console.WriteLine("-1");
				}
			}
			if(command[0] == "size"){
				int length = queue.Count;
				Console.WriteLine(length + "");
			}
			if(command[0] == "empty"){
				if(queue.Count == 0){
					Console.WriteLine("1");
				}else{
					Console.WriteLine("0");
				}
			}
			if(command[0] == "front"){
				if(queue.Count == 0){
					Console.WriteLine("-1");
				}else{
					Console.WriteLine(queue[0]);
				}
			}
			if(command[0] == "back"){
				if(queue.Count == 0){
					Console.WriteLine("-1");
				}else{
					Console.WriteLine(queue[queue.Count - 1]);
				}
			}
		}
		
	}
}