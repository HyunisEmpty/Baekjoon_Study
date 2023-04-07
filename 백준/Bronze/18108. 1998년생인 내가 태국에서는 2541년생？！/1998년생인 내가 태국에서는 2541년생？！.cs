using System;

public class main {
	public static void Main() {
		
		string input = Console.ReadLine();
		int year = Convert.ToInt32(input);
		year -= 543;
		string answer = Convert.ToString(year);
		
		Console.WriteLine(answer);
		
	}
}