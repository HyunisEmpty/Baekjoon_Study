using System;

public class main {
	public static void Main() {
		
		int n = int.Parse(Console.ReadLine());
		
		int answer = 1;
		
		for(int i = 1; i < n+1; i++){
			answer = answer * i;
		}
		
		Console.WriteLine(answer);
		
	}
}