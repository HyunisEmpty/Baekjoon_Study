using System;

public class main {
	public static void Main() {
		
		int n = int.Parse(Console.ReadLine());
		
		for(int i = 0; i < n; i++){
			string input = Console.ReadLine();
			string[] numbers = input.Split();
			
			int a = int.Parse(numbers[0]);
			int b = int.Parse(numbers[1]);
			int sum = a + b;
			int count = i + 1;
			
			string answer = $"Case #{count}: {a} + {b} = {sum}";
			
			Console.WriteLine(answer);
		}
		
	}
}