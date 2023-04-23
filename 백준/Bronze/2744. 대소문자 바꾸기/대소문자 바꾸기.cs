using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string input = Console.ReadLine();
		string answer = "";
		
		for(int i = 0; i < input.Length; i++){
			char target_char = input[i];
			
			if(target_char == Char.ToLower(target_char)){
				answer += Char.ToUpper(target_char);
			}else{
				answer += Char.ToLower(target_char);
			}
		}
		
		Console.WriteLine(answer);
		
	}
}