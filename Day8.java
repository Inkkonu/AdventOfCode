import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day8 {

    public static int p1(List<String> data){
        return 0;
    }

    public static int p2(List<String> data){
        return 0;
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<String> data = new ArrayList<>();
        Scanner scanner = new Scanner(new File("input.txt"));
        while (scanner.hasNextLine()) {
            data.add(scanner.nextLine());
        }
        System.out.println("Partie 1 : " + p1(data));
        System.out.println("Partie 2 : " + p2(data));
    }
}
