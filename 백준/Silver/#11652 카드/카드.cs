using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		Dictionary<string, int> cards = new Dictionary<string, int>();
		
		int test_case = int.Parse(Console.ReadLine());
		string card;
		for(int test = 0; test < test_case; test++){
			card = Console.ReadLine();
			
			// 딕셔너리에 이미 카드가 있는 경우 
			if(cards.ContainsKey(card)){
				cards[card] += 1;
			}else{
				cards.Add(card, 0);
			}
			
		}
		string max_key = "";
		int max_value = -1;
		foreach(string key in cards.Keys){
			if(cards[key] > max_value){
				max_value = cards[key];
				max_key = key;
			}else if(cards[key] == max_value){
				if(long.Parse(max_key) > long.Parse(key)){
					max_value = cards[key];
					max_key = key;
				}
			}
		}
		
		Console.WriteLine(long.Parse(max_key));
		
	}
}