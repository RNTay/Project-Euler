class Problem002 {
    public static void main(String[] args) {
        int a = 0, b = 1, sum_even_terms = 0;
        int c = a + b;
        while (c < 4000000) {
            if (c % 2 == 0) {
                sum_even_terms += c;
            }
            a = b;
            b = c;
            c = a + b;
        }
        System.out.println(sum_even_terms);
    }
}
