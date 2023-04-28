using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		int target_count = int.Parse(Console.ReadLine());
		int count = 0;
		bool flag = true;
		bool reverse_flag = false;
		
		int base_number = 1;
		
		while(flag){
			
			for (int i = 0; i < base_number; i++){
				count += 1;
				
				if(count == target_count){
					if(reverse_flag){
						Console.WriteLine((1 + i) + "/" + (base_number - i));
					}else{
						Console.WriteLine((base_number - i) + "/" + (1 + i));
					}
					flag = false;
					break;
				}
				
			}
			
			if(reverse_flag){
				reverse_flag = false;
			}else{
				reverse_flag = true;
			}
			
			base_number += 1;
			
		}
 		
	} 
}