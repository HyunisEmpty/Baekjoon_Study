using System.Collections.Generic;
using System;

public class main {
	public static void Main() {
		
		string[] input = Console.ReadLine().Split();
		int n = int.Parse(input[0]);
		int k = int.Parse(input[1]);
		List<int> numbers = new List<int>();
		List<int> josephus = new List<int>();
		
		for(int i = 0; i < n; i++){
			numbers.Add(i+1);
		}
		
		int count = 0;
		int index = 0;
		
		while(josephus.Count != n){
			count += 1;
			
			if(count % k == 0){
				josephus.Add(numbers[index]);
				// Remove를 하면 리스트의 길이가 1 짧아 지므로 인덱스를 증가시키지 않음
				numbers.Remove(numbers[index]);
			}else{
				index += 1;
			}
			
			// numbers 리스트를 벗어나면 index를 0으로 초기화합니다.
			if(index == numbers.Count){
				index = 0;
			}
			
			
		}
		
		Console.WriteLine("<" + string.Join(", ", josephus) + ">");
		
	} 
}