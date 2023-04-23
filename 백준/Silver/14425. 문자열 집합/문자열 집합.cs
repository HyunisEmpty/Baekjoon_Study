using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string[] command = Console.ReadLine().Split();
		int n = int.Parse(command[0]);
		int m = int.Parse(command[1]);
		
		List<string> database = new List<string>();
		
		int count = 0;
		
		for(int i = 0; i < n; i++){
			database.Add(Console.ReadLine());
		}
		
		for(int i = 0; i < m; i++){
			string target = Console.ReadLine();
			foreach(string data in database){
				if(data == target){
					count += 1;
				}
			}
		}
		
		Console.WriteLine(count + "");
		
	}
}