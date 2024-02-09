public class BubbleSort {
    void swap(int array[], int i, int j){
        int temp = array[i];
        array[i]=array[j];
        array[j]=temp;
    }
    void bubbleSort(int array[]){

        int n = array.length;
        for (int i=0;i<n-1;i++){
            for (int j=0;j<n-i-1;j++){
                if(array[j]>array[j+1]){
                    swap(array,j,j+1);
                }

            }
        }
    }
    void printArray(int array[]){
        int n = array.length;
        for (int i=0;i<n;i++){
            System.out.print(array[i]+" ");
        }
        System.out.println();
    }
    // test
    public static void main(String args[]){
        BubbleSort bs = new BubbleSort();
        int array[] = {9,8,7,6,5,4,3,2,1};
        bs.bubbleSort(array);
        System.out.println("Sorted array: ");
        bs.printArray(array);
    }
}