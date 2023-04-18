using System;

public class main {
	public static void Main() {
		
		string input = Console.ReadLine();
		input = input.Trim();
		string[] words = input.Split();
		
		string length;
		if(words[0] == ""){
			length = "0";
		}else{
			int length_int = words.Length;
			length = Convert.ToString(length_int);	
		}
		
		Console.WriteLine(length);
		
	}
}