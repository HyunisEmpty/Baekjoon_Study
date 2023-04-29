using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		List<int> students = new List<int>();
		
		for(int i = 1; i < 31; i++){
			students.Add(i);
		}
 		
		int number;
		for(int i = 0; i < 28; i++){
			number = int.Parse(Console.ReadLine());
			students.Remove(number);
		}
		
		for(int i = 0; i < 2; i++){
			Console.WriteLine(students[i]);
		}
		
	} 
}