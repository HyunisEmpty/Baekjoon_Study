using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		List<int> numbers = new List<int>();
		
		for(int i = 0; i < 10; i++){
			int number = int.Parse(Console.ReadLine());
			numbers.Add(number % 42);
		}
		
		List<int> uniqueNumbers = numbers.Distinct().ToList();
		
		Console.WriteLine(uniqueNumbers.Count + "");
		
	}
}