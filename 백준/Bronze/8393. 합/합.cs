using System;

public class main {
	public static void Main() {
		
		string input = Console.ReadLine();
		int n = Convert.ToInt32(input);
		
		int answer = 0;
		for(int i = 1; i < n+1; i++){
			answer += i;
		}
		
		Console.WriteLine(answer);
		
	}
}