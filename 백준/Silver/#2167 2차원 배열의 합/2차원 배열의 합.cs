using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string[] input;
		input = Console.ReadLine().Split();
		int row_size = int.Parse(input[0]);
		int col_size = int.Parse(input[1]);
	
		int[,] numbers = new int[row_size, col_size];
		
		// 입력된 문자열을 배열에 값으로 변환하는 반복문
		int count;
		for(int i_for = 0; i_for < row_size; i_for++){
			count = 0;
			string[] input_arr = Console.ReadLine().Split();
			
			foreach(string number in input_arr){
				numbers[i_for,count] = int.Parse(number);
				count += 1;
			}
		}
		
		int test_case = int.Parse(Console.ReadLine());
		int i;
		int j;
		int x;
		int y;
		int sum;
		for(int test = 0; test < test_case; test++){
			sum = 0;
			input = Console.ReadLine().Split();
			i = int.Parse(input[0])-1;
			j = int.Parse(input[1])-1;
			x = int.Parse(input[2])-1;
			y = int.Parse(input[3])-1;
			
			for(int row = i; row <= x; row++){
				for(int col = j; col <= y; col++){
					sum += numbers[row, col];	
				}
			}
			
			Console.WriteLine(sum);
			
		}
 		
	} 
}