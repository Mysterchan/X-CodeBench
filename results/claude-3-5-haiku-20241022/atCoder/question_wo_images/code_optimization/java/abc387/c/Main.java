import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    final long L = sc.nextLong();
    final long R = sc.nextLong();
    
    long result = countSnake(R) - countSnake(L - 1);
    System.out.println(result);
  }
  
  private static long countSnake(long n) {
    if (n < 10) return 0;
    
    String s = String.valueOf(n);
    int len = s.length();
    long count = 0;
    
    // Count all snake numbers with fewer digits
    for (int d = 2; d < len; d++) {
      count += countSnakeWithDigits(d);
    }
    
    // Count snake numbers with same number of digits <= n
    count += countSnakeWithDigitsUpTo(s);
    
    return count;
  }
  
  private static long countSnakeWithDigits(int digits) {
    long count = 0;
    // First digit can be 1-9
    for (int first = 1; first <= 9; first++) {
      // Remaining digits can be 0 to (first-1)
      count += pow(first, digits - 1);
    }
    return count;
  }
  
  private static long countSnakeWithDigitsUpTo(String s) {
    int len = s.length();
    int firstDigit = s.charAt(0) - '0';
    long count = 0;
    
    // Count numbers with smaller first digit
    for (int d = 1; d < firstDigit; d++) {
      count += pow(d, len - 1);
    }
    
    // Count numbers with same first digit but smaller suffix
    count += countSmallerSuffix(s, 1, firstDigit);
    
    return count;
  }
  
  private static long countSmallerSuffix(String s, int pos, int maxDigit) {
    if (pos >= s.length()) {
      return 1; // The number itself is a snake number
    }
    
    int currentDigit = s.charAt(pos) - '0';
    long count = 0;
    
    if (currentDigit >= maxDigit) {
      // Current number is not a snake number
      // Count all numbers with digits at position pos being 0 to maxDigit-1
      count = pow(maxDigit, s.length() - pos);
    } else {
      // Current digit is valid
      // Count numbers with smaller digit at this position
      count = (long) currentDigit * pow(maxDigit, s.length() - pos - 1);
      
      // Recursively count for same digit at this position
      count += countSmallerSuffix(s, pos + 1, maxDigit);
    }
    
    return count;
  }
  
  private static long pow(long base, int exp) {
    long result = 1;
    for (int i = 0; i < exp; i++) {
      result *= base;
    }
    return result;
  }
}