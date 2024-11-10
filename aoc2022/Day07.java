package aoc2022;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

abstract class DirectoryContent {
    private String name;

    public DirectoryContent(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public abstract int getSize();

    public abstract int sumFileUnder(int threshold);
}

class MyFile extends DirectoryContent {
    private int size;

    public MyFile(String name, int size) {
        super(name);
        this.size = size;
    }

    @Override
    public int getSize() {
        return size;
    }

    @Override
    public int sumFileUnder(int threshold) {
        return 0;
    }
}

class MyDirectory extends DirectoryContent {
    private MyDirectory parent;
    private List<DirectoryContent> content;

    public MyDirectory(String name, MyDirectory parent) {
        super(name);
        this.parent = parent;
        this.content = new ArrayList<>();
    }

    public void addElement(DirectoryContent c) {
        this.content.add(c);
    }

    public MyDirectory findChild(String name) {
        DirectoryContent c = this.content.stream().filter(cont -> name.equals(cont.getName())).findAny().orElse(null);
        return (MyDirectory) c;
    }

    @Override
    public int getSize() {
        int total = 0;
        for (DirectoryContent c : content) {
            total += c.getSize();
        }
        return total;
    }

    public MyDirectory getParent() {
        return this.parent;
    }

    @Override
    public int sumFileUnder(int threshold) {
        int total = 0;
        int itSize = this.getSize();
        if (itSize <= threshold) {
            total += itSize;
        }
        for (DirectoryContent c : content) {
            total += c.sumFileUnder(threshold);
        }
        return total;
    }
}

public class Day07 {

    public static int p1(List<String> data) {
        MyDirectory root = new MyDirectory("/", null);
        MyDirectory current_repo = root;
        for (String line : data.subList(1, data.size())) {
            String[] parts = line.split(" ");
            if (parts[0].equals("$")) {
                if (parts[1].equals("ls")) {
                    ;
                } else {
                    if (parts[2].equals("..")) {
                        current_repo = current_repo.getParent();
                    } else {
                        current_repo = current_repo.findChild(parts[2]);
                    }
                }
            } else {
                if (parts[0].equals("dir")) {
                    current_repo.addElement(new MyDirectory(parts[1], current_repo));
                } else {
                    current_repo.addElement(new MyFile(parts[1], Integer.parseInt(parts[0])));
                }
            }
        }
        return root.sumFileUnder(100000);
    }

    public static int p2(List<String> data) {
        MyDirectory root = new MyDirectory("/", null);
        List<MyDirectory> allDirectories = new ArrayList<>();
        allDirectories.add(root);
        MyDirectory current_repo = root;
        for (String line : data.subList(1, data.size())) {
            String[] parts = line.split(" ");
            if (parts[0].equals("$")) {
                if (parts[1].equals("ls")) {
                    ;
                } else {
                    if (parts[2].equals("..")) {
                        current_repo = current_repo.getParent();
                    } else {
                        current_repo = current_repo.findChild(parts[2]);
                    }
                }
            } else {
                if (parts[0].equals("dir")) {
                    MyDirectory d = new MyDirectory(parts[1], current_repo);
                    current_repo.addElement(d);
                    allDirectories.add(d);
                } else {
                    current_repo.addElement(new MyFile(parts[1], Integer.parseInt(parts[0])));
                }
            }
        }
        int fullSize = 70000000;
        int freeSpaceNeeded = 30000000;
        int currentFreeSpace = fullSize - root.getSize();
        List<MyDirectory> bigEnough = allDirectories.stream().filter(d -> d.getSize() >= freeSpaceNeeded - currentFreeSpace).toList();
        MyDirectory smallest = bigEnough.get(0);
        for (MyDirectory d : bigEnough) {
            if (d.getSize() <= smallest.getSize()) {
                smallest = d;
            }
        }
        return smallest.getSize();
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<String> data = new ArrayList<>();
        Scanner scanner = new Scanner(new File("aoc2022/input.txt"));
        while (scanner.hasNextLine()) {
            data.add(scanner.nextLine());
        }
        System.out.println("Partie 1 : " + p1(data));
        System.out.println("Partie 2 : " + p2(data));
    }
}
