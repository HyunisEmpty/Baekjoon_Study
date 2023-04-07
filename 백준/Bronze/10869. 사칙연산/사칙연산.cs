using System;

public class main {
	public static void Main() {
		
		string str = Console.ReadLine();
		string[] numbers = str.Split();
		int a = Convert.ToInt32(numbers[0]);
		int b = Convert.ToInt32(numbers[1]);
		
		Console.WriteLine(a + b);
		Console.WriteLine(a - b);
		Console.WriteLine(a * b);
		double answer = a / b;
		Console.WriteLine(System.Math.Truncate(answer));
		Console.WriteLine(a % b);
		
	}
}