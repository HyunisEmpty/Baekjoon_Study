using System.Collections.Generic;
using System.Linq;
using System;

public class main {
	public static void Main() {
		
		int test_case = int.Parse(Console.ReadLine());
		// 괄호가 들어갈 리스트 인스턴스 생성
		List<string> ps_list = new List<string>();
		
		for(int test = 0; test < test_case; test++){
			
			string input = Console.ReadLine();
			// 반복문이 처음 시작할때 리스트의 모든 값을 제거한다. 
			ps_list.Clear();
			
			// 입력받은 문자열의 값을 하나씩 가지고 온다. 
			for(int i = 0; i < input.Length; i++){
				ps_list.Add(Convert.ToString(input[i]));
				
				// 리스트의 길이가 2 이상이라면 마지막 값과 그 전값이 ()인지 확인한 후 제거한다.
				if(ps_list.Count >= 2){
					if((ps_list[ps_list.Count-2] == "(") && (ps_list[ps_list.Count-1] == ")")){
						ps_list.RemoveAt(ps_list.Count - 1);
						ps_list.RemoveAt(ps_list.Count - 1);
					}
				}
				
			}
			
			// 모든 연산이 끝난후 리스트에 값이 없으면 Yes 있으면 No를 출력한다. 
			if(ps_list.Count != 0){
				Console.WriteLine("NO");
			}else{
				Console.WriteLine("YES");
			}
			
		}
		
	} 
}