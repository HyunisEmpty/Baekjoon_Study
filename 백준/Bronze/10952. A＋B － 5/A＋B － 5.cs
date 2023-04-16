using System;

public class main {
	public static void Main() {
		
		bool flag = true;
		
		while(flag){
			string input = Console.ReadLine();
			string[] numbers = input.Split();
			
			int a = int.Parse(numbers[0]);
			int b = int.Parse(numbers[1]);
			
			if(a == 0 && b == 0){
				flag = false;
			}else{
				Console.WriteLine($"{a+b}");
			}
		}
		
	}
}