using System;

public class main {
	public static void Main() {
		
		// N과 X를 입력받는다. 
		string str = Console.ReadLine();
		string[] words = str.Split();
		int n = Convert.ToInt32(words[0]);
		int target_number = Convert.ToInt32(words[1]);
		
		// 수열 A를 입력받는다.
		string input = Console.ReadLine();
		string[] numbers = input.Split();
		
		// 정답을 담을 배열 정의 
		int[] arr = new int[0];
		
		string answer = "";
		
		for(int i = 0; i < n; i++){
			int number = Convert.ToInt32(numbers[i]);
			if(number < target_number){
				// 배열 크기 증가
				Array.Resize(ref arr, arr.Length + 1);
				// 추가할 값 할당 
				arr[arr.Length - 1] = number;
			}
		}
		
		string number_str;
		
		for(int i = 0; i < arr.Length; i++){
			number_str = Convert.ToString(arr[i]);
			if(i == 0){
				answer += number_str;
			}else{
				answer += " " + number_str;
			}
		}
		
		Console.WriteLine(answer);
		
	}
}