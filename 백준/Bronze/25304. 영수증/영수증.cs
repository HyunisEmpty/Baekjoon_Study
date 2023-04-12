using System;

public class main {
	public static void Main() {
		
		// 총 결제 금액을 입력받는다.
		string total_cost_str = Console.ReadLine();
		long total_cost = Convert.ToInt64(total_cost_str);
		
		// 구매한 상품의 종류를 입력받는다.
		string goods_kind_str = Console.ReadLine();
		long goods_kind = Convert.ToInt64(goods_kind_str);
		
		// 종류의 수만큼, 물품의 가격 * 믈픔의 수를 계산하여 총 가격에 더한다. 
		long cost_sum = 0;
		for(long i = 0; i < goods_kind; i++){
			string input = Console.ReadLine();
			string[] inputs = input.Split();
			
			long cost = Convert.ToInt64(inputs[0]);
			long count = Convert.ToInt64(inputs[1]);
			
			cost_sum = cost_sum + cost * count;
		}
		
		if(total_cost == cost_sum){
			Console.WriteLine("Yes");
		}else{
			Console.WriteLine("No");
		}
	}
}