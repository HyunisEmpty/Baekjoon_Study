using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		string[] input = Console.ReadLine().Split();
		int site_type = int.Parse(input[0]);
		int target_site_type = int.Parse(input[1]);
		
		Dictionary<string, string> sites = new Dictionary<string, string>();
		string[] input_site;
		string site;
		string password;
		
		for(int i = 0; i < site_type; i++){
			input_site = Console.ReadLine().Split();
			site = input_site[0];
			password = input_site[1];
			sites.Add(site, password);
		}
		
		for(int i = 0; i < target_site_type; i++){
			site = Console.ReadLine();
			Console.WriteLine(sites[site]);
		}
		
	} 
}