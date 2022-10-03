import java.util.Scanner;

class Main {
	public static void main(String args[]) {
		
		int all_sum = 0;
			
		Scanner sc = new Scanner(System.in);
		String inputaSTR1 = sc.nextLine();
		String inputaSTR2 = sc.nextLine();
		
		int val1 = Integer.valueOf(inputaSTR1).intValue();
		int val2 = Integer.valueOf(inputaSTR2).intValue();
		all_sum = val1 + val2;
		System.out.println(all_sum);
	}
}