using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string[] input = Console.ReadLine().Split();
		int[] basket = new int[int.Parse(input[0])];
		int test = int.Parse(input[1]);
		
		for(int i = 0; i < int.Parse(input[0]); i++){
			basket[i] = i + 1;
		}
		
		for(int i = 0; i < test; i++){
			string[] basket_input = Console.ReadLine().Split();
			int basket_1 = basket[int.Parse(basket_input[0])-1];
			int basket_2 = basket[int.Parse(basket_input[1])-1];
			int basket_extra = 0;
			
			basket[int.Parse(basket_input[0])-1] = basket_2;
			basket[int.Parse(basket_input[1])-1] = basket_1;
		}
		
		string answer = string.Join(" ", basket);
		Console.WriteLine(answer);
		
	}
}