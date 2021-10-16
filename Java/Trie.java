import java.util.Scanner;
import java.util.Stack;

class Node{
  boolean word_end;
  Node[] children = new Node[26];

  Node(){
    word_end = false;
    for(int i = 0;i < 26;i++){
      children[i] = null;
    }
  }
}

class Trie{
  private static Node root;

  static void insert(String str){
    Node current = root;
    for(int i = 0;i < str.length();i++){
      char ch = str.charAt(i);
      if(current.children[ch-'a'] == null){
        current.children[ch-'a'] = new Node();
      }
      current = current.children[ch-'a'];
    }
    current.word_end = true;
    System.out.println("String inserted");
  }

  static void search(String str){
    Node current = root;
    for(int i = 0;i < str.length();i++){
      char ch = str.charAt(i);
      if(current.children[ch-'a'] == null){
        System.out.println("Word does not exist");
        return;
      }
      else{
        current = current.children[ch-'a'];
      }
    }
    if(current.word_end){
      System.out.println("Word found");
    }
    else{
      System.out.println("Word does not exist");
    }
  }


  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int choice = 0;
    root = new Node();

    while(choice != 3){
      System.out.println("Select one operation : 1) Insert\t2) Search\t3) Exit");
      choice = sc.nextInt();
      switch(choice){
        case 1:
          System.out.print("Enter a string to insert - ");
          String str = sc.next();
          insert(str);
          break;
        case 2:
          System.out.print("Enter a string to search -");
          String st = sc.next();
          search(st);
          break;
        default:
          break;
        }
    }

  }
}
