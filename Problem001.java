class Problem001 {
    public static void main(String[] args) {
        int number = 1, sum = 0;
        while (number < 1000) {
            if ((number % 3 == 0) || (number % 5 == 0)) {
                sum += number;
            }
            number++;
        }
        System.out.println(sum);
    }
}
