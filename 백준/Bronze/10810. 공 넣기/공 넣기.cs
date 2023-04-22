using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string input = Console.ReadLine();
		string[] inputs = input.Split();
		
		int[] basket = new int[int.Parse(inputs[0])];
		int command = int.Parse(inputs[1]);
		
		for(int i = 0; i < int.Parse(inputs[0]); i++){
			basket[i] = 0;
		}
		
		for(int i = 0; i < command; i++){
			string number = Console.ReadLine();
			string[] numbers = number.Split();
			for(int j = int.Parse(numbers[0])-1; j < int.Parse(numbers[1]); j++){
				basket[j] = int.Parse(numbers[2]);
			}
		}
		
		string answer = "";
		for(int i = 0; i < int.Parse(inputs[0]); i++){
			if(i != int.Parse(inputs[0])-1){
				answer += basket[i] + " ";
			}else{
				answer += basket[i];
			}
		}
		
		Console.WriteLine(answer);
		
	}
}