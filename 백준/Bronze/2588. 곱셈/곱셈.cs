using System;

public class main {
	public static void Main() {
		
		string num1_str = Console.ReadLine();
		string num2_str = Console.ReadLine();
		
		int num1_int = int.Parse(num1_str);
		int num2_int = int.Parse(num2_str);
		
		for(int i = 0; i < 3; i++){
			int number = Convert.ToInt32(num2_str[2 - i] - '0');
			Console.WriteLine(num1_int * number);
		}
		
		Console.WriteLine(num1_int * num2_int);
		
	}
}