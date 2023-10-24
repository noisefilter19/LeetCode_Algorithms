public class HelloRecursively {
    private void hello(int n) {
        System.out.println(n);
        if (n < 1) {
            System.out.println("End");
        } else {
            hello(n-1);
        }
    }
    
    public static void main(String[] args) {
        HelloRecursively h = new HelloRecursively();
        h.hello(200);
    }
}
