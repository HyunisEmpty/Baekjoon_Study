import java.util.Scanner;

class Main {
	public static void main(String args[]) {
			
		Scanner sc = new Scanner(System.in);
		String inputaSTR = sc.nextLine();
		String[] array = inputaSTR.split(" ");
		
		
		int all_sum = 0;
		for(int i = 0; i < array.length; i++) {
			int val1 = Integer.valueOf(array[i]).intValue();
			all_sum += val1;
		}
		
		System.out.println(all_sum);
	}
}