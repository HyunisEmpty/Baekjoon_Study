using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		long[] padovan = new long[100];
		for(int i = 0; i < 100; i++){
			if(i < 3){
				padovan[i] = 1;
			}else{
				padovan[i] = padovan[i - 2] + padovan[i - 3];
			}
		}
		
		int test_case = int.Parse(Console.ReadLine());
		int n;
		for(int test = 0; test < test_case; test++){
			n = int.Parse(Console.ReadLine());
			Console.WriteLine(padovan[n-1]);
		}
		
	}
}