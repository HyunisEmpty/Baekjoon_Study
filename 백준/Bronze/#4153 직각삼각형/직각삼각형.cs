using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		bool flag = true;
		
		while(flag){
			string input = Console.ReadLine();
			int[] numbers = input.Split().Select(int.Parse).ToArray();

			Array.Sort(numbers);
			int a = numbers[0] * numbers[0];
			int b = numbers[1] * numbers[1];
			int c = numbers[2] * numbers[2];
			
			if(a + b + c == 0){
				break;
			}

			if(a + b == c){
				Console.WriteLine("right");
			}else{
				Console.WriteLine("wrong");
			}	
		}
		
	} 
}