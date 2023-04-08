using System;

public class main {
	public static void Main() {
		
		string input = Console.ReadLine();
		string[] numbers = input.Split();
		
		long a = Convert.ToInt64(numbers[0]);
		long b = Convert.ToInt64(numbers[1]);
		long c = Convert.ToInt64(numbers[2]);
		
		string answer = Convert.ToString(a + b + c);
		
		Console.WriteLine(answer);
		
	}
}