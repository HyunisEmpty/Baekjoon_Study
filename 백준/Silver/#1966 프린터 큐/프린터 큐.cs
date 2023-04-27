using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		int test_case = int.Parse(Console.ReadLine());
		
		for(int test = 0; test < test_case; test++){
			
			string[] input = Console.ReadLine().Split();
			int n = int.Parse(input[0]);
			int target_index = int.Parse(input[1]);
			
			// 문자열 형으로 입력받은 배열을 정수형으로 변환하여 정수형 배열에 저장 합니다.
			string[] numbers_str = Console.ReadLine().Split();
			List<int> numbers = new List<int>();
			
			for(int i = 0; i < n; i++){
				numbers.Add(Convert.ToInt32(numbers_str[i]));
			}
			
			// 원하는 수가 몇번째로 출력되는지를 확인, 최대값의 저장
			int count = 0;
			int max;
			
			while(true){
				max = numbers.Max();
				
				
				if(numbers[0] == numbers.Max()){
					// 우선순위가 높은 값이 제거 되는 경우
					
					count += 1;
					if(target_index == 0){
						Console.WriteLine(count);
						break;
					}else{
						target_index -= 1;
					}
					
					numbers.Remove(numbers[0]);
				}else{
					// 우선순위 높은 값이 아닌 경우
					
					if(target_index == 0){
						target_index = numbers.Count - 1;
					}else{
						target_index -= 1;
					}
					
					numbers.Add(numbers[0]);
					numbers.Remove(numbers[0]);
				}
				
			}
			
		}
		
	} 
}