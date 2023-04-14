using System;

public class main {
	public static void Main() {
		
		string n_str = Console.ReadLine();
		int n = Convert.ToInt32(n_str);
		
		string numbers_str = Console.ReadLine();
		string[] numbers = numbers_str.Split();
		
		int min = 0;
		int max = 0;
		
		for(int i = 0; i < numbers.Length; i++){
			int a = Convert.ToInt32(numbers[i]);
			
			if(i == 0){
				min = a;
				max = a;
			}else{
				if(a < min){
					min = a;
				}
				if(max < a){
					max = a;
				}
			}	
		}
		
		Console.WriteLine(min + " " + max);	
		
	}
}