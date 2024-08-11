public class prac{
    public static void main(String[] args){
        double[] inputs = {1,2,9};
        double[] weights = {2.3,2.4,3.5};
        double bias = 2.0;
        double outputs = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias;
        System.out.println(outputs);
    }
}