package j5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
/**
 * ccc19j5
 */
public class ccc19j5 {
  static final ArrayList<String[]> inputRules = new ArrayList<String[]>();
  static int steps;
  static String initStr;
  static String finStr;
  static String[] output = new String[15];
  static final HashMap<String, String> memo = new HashMap<String, String>();

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    for (int i = 0; i<3; i++){
      String rule = sc.nextLine();
      inputRules.add(rule.split(" "));
    }
    
    steps = sc.nextInt();
    initStr = sc.next();
    finStr = sc.next();
    sc.close();
    
    solve(0, initStr);

    for (int i=0; i<steps; i++){
      System.out.println(output[i]);
    }
  }

  public static boolean solve(int currentStep, String currentString) {
    if (memo.containsKey(currentString+currentStep)) {
      output[currentStep] = memo.get(currentString+currentStep);
      if (currentString.equals(finStr)) {
        return true;
      }
      return false;
    }
    
    for (int i=0; i<3; i++) {
      int ruleLength = inputRules.get(i)[0].length();
      int strLength = currentString.length();
      
      if (strLength >= ruleLength) {
        for (int j=0; j < strLength - ruleLength + 1; j++) {
          String sliced = currentString.substring(j, j+ruleLength);
          String rule = inputRules.get(i)[0];

          if (sliced.equals(rule)) {
            String before = currentString.substring(0, j);
            String after = currentString.substring(j+ruleLength);
            String newString = before + inputRules.get(i)[1] + after;
            String newStringFormatted = (i+1) + " " + (j+1) + " " + newString;

            memo.put(currentString+currentStep, newStringFormatted);  

            if (newString.equals(finStr)) {
              output[currentStep] = newStringFormatted;
              return true;
            }

            if (currentStep + 1 < steps) {
              boolean finished = solve(currentStep + 1, newString);
              if (finished) {
                output[currentStep] = newStringFormatted;
                return true;
              }
            }
          }
        }
      }
    }
    return false;
  }
}



// String str = initStr;
    // for (int i = 0; i < steps; i++) {
    //   String str_2 = substution(str);
    //   int startIndex = str.indexOf(inputRules.get(ruleNumber-1)[0]) + 1;
    //   System.out.println(ruleNumber + " " + startIndex + " " + str_2);
    //   str = str_2;
    // }
  // }

  // public static String substution(String str){
  //   int length = str.length();
  //   String newStr = checkAndReplace(str);

  //   if (!newStr.equals(str)) {
  //     return newStr;
  //   }
  //   if (length < 2) return str;

  //   String half1 = str.substring(0, (int)Math.ceil(str.length()/2));
  //   String half2 = str.substring((int)Math.ceil(str.length()/2));
  //   String newHalfs = substution(half1) + half2;
  //   if (newHalfs.equals(str)) {
  //     newHalfs = half1 + substution(half2);
  //   }
  //   return newHalfs;
  // }

  // public static String checkAndReplace(String str) {
  //   for (int i = 0; i < 3;  i++){
  //     String rule = inputRules.get(i)[0];
  //     if (str.equals(rule)){
  //       ruleNumber = i+1;
  //       return str.replaceFirst(rule, inputRules.get(i)[1]);
  //     }
  //   }
  //   return str;
  // }