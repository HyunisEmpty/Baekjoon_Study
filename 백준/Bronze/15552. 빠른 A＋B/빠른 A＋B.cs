using System;
using System.Text;

public class main {
	public static void Main() {
		
		string test_case_str = Console.ReadLine();
		int test_case = Convert.ToInt32(test_case_str);
		
		StringBuilder answer = new StringBuilder();
		
		for(int i = 0; i < test_case; i++){
			string input = Console.ReadLine();
			string[] inputs = input.Split();
			
			int a = Convert.ToInt32(inputs[0]);
			int b = Convert.ToInt32(inputs[1]);
			
			answer.Append(a + b + "\n");
		}
		
		Console.WriteLine(answer.ToString());
	}
}