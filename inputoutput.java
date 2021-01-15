package firstproject;
import java.util.Scanner; //used for input

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String scanned1 = sc.next(); //string
		int scanned2 = sc.nextInt(); //int
		boolean scanned3 = sc.nextBoolean(); //boolean
		double scanned4 = sc.nextDouble(); //float 
	
		int x = Integer.parseInt(scanned1);
	
		System.out.println(x);
		
		
	}

}
