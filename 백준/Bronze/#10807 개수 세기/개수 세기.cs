using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		int n = int.Parse(Console.ReadLine());
		string numbers_str = Console.ReadLine();
		string[] numbers = numbers_str.Split();
		string target = Console.ReadLine();
		int count = 0;
		
		foreach(string number in numbers){
			if(number == target){
				count += 1;
			}
		}
		
		Console.WriteLine(count + "");
		
	}
}