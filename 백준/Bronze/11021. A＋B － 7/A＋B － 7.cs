using System;

public class main {
	public static void Main() {
		string input = Console.ReadLine();
		int test_case = Convert.ToInt32(input);
		for(int i = 0; i < test_case; i++){
			int counter = i + 1;
			string str = Console.ReadLine();
			string[] words = str.Split();
			int A = Convert.ToInt32(words[0]);
			int B = Convert.ToInt32(words[1]);
			Console.WriteLine("Case #{0}: " + (A + B), counter);
		}
	}
}