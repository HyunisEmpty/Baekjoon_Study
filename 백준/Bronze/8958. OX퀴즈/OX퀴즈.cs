using System;

public class main {
	public static void Main() {
		
		int test_case = int.Parse(Console.ReadLine());
		
		for(int test = 0; test < test_case; test++){
			int bonus = 1;
			int score = 0;
			bool flag = false;
			string input = Console.ReadLine();
			
			for(int i = 0; i < input.Length; i++){
				char word = input[i];
				
				// 단어가 O인 경우
				if(word == 'O'){
					// 첫번째 O 혹은 이전이 X였던 경우
					if(flag == false){
						score += bonus;
					}else{
						bonus += 1;
						score += bonus;
					}
					flag = true;
				}else{
					bonus = 1;
					flag = false;
				}
			}
			Console.WriteLine(score + " ");
		}
		
	}
}