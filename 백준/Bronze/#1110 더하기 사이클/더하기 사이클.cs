using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string number = Console.ReadLine();
		string original_number;
		
		// number의 10의 자리와 1의 자리값을 저장할 변수 선언
		string new_number;
		
		string next_number;
		int count = 0;
		
		int number_10;
		int number_1;
		
		if(number.Length == 1){
			number = "0" + number;
		}
		
		original_number = number;
		
		while(true){
			
			count += 1;
			
			number_10 = Convert.ToInt32(number[0].ToString());
			number_1 = Convert.ToInt32(number[1].ToString());
						
			new_number = Convert.ToString(number_10 + number_1);
			
			if(new_number.Length == 1){
				new_number = "0" + new_number;
			}
			
			// 1회 순환으로 만들어진 숫자
			next_number = number[1].ToString() + new_number[1].ToString(); 
			
			if(next_number == original_number){
				Console.WriteLine(count + "");
				break;
			}else{
				number = next_number;
			}
			
		}
		
	} 
}