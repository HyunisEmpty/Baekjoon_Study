using System;

public class main {
	public static void Main() {
		
		int n = int.Parse(Console.ReadLine());
		
		string answer = "int";
			
		for(int i = 0; i < n/4; i++){
			answer = "long " + answer;
		}
		
		Console.WriteLine(answer);
		
	}
}