package aoc2022;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class Item {
    private long worryLevel;

    public Item(int worryLevel) {
        this.worryLevel = worryLevel;
    }

    public long getWorryLevel() {
        return worryLevel;
    }

    public void setWorryLevel(long worryLevel) {
        this.worryLevel = worryLevel;
    }
}

class Test {
    private final int value;
    private int trueMonkey;
    private int falseMonkey;

    public Test(int value) {
        this.value = value;
    }

    public void testValue(int id, Item item, List<Monkey> monkeys) {
        monkeys.get(id).getItems().remove(item);
        if (item.getWorryLevel() % value == 0) {
            monkeys.get(trueMonkey).add(item);
        } else {
            monkeys.get(falseMonkey).add(item);
        }
    }

    public int getValue() {
        return value;
    }

    public void setTrueMonkey(int trueMonkey) {
        this.trueMonkey = trueMonkey;
    }

    public void setFalseMonkey(int falseMonkey) {
        this.falseMonkey = falseMonkey;
    }
}

class Monkey {
    private final int id;
    private final List<Item> items;
    private Test test;
    private int inspections;

    public Monkey(int id) {
        this.id = id;
        this.items = new ArrayList<>();
        this.inspections = 0;
    }

    public void add(Item item) {
        this.items.add(item);
    }

    public void operate(Item item, int productOfAll) {
        switch (this.id) {
            case 0 -> item.setWorryLevel((item.getWorryLevel() * 13) % productOfAll);
            case 1 -> item.setWorryLevel((item.getWorryLevel() + 7) % productOfAll);
            case 2 -> item.setWorryLevel((item.getWorryLevel() + 6) % productOfAll);
            case 3 -> item.setWorryLevel((item.getWorryLevel() + 5) % productOfAll);
            case 4 -> item.setWorryLevel((item.getWorryLevel() + 8) % productOfAll);
            case 5 -> item.setWorryLevel((item.getWorryLevel() * 5) % productOfAll);
            case 6 -> item.setWorryLevel((item.getWorryLevel() * item.getWorryLevel()) % productOfAll);
            case 7 -> item.setWorryLevel((item.getWorryLevel() + 2) % productOfAll);
        }
    }

    public void operate(Item item) {
        switch (this.id) {
            case 0 -> item.setWorryLevel((item.getWorryLevel() * 13) / 3);
            case 1 -> item.setWorryLevel((item.getWorryLevel() + 7) / 3);
            case 2 -> item.setWorryLevel((item.getWorryLevel() + 6) / 3);
            case 3 -> item.setWorryLevel((item.getWorryLevel() + 5) / 3);
            case 4 -> item.setWorryLevel((item.getWorryLevel() + 8) / 3);
            case 5 -> item.setWorryLevel((item.getWorryLevel() * 5) / 3);
            case 6 -> item.setWorryLevel((item.getWorryLevel() * item.getWorryLevel()) / 3);
            case 7 -> item.setWorryLevel((item.getWorryLevel() + 2) / 3);
        }
    }

    public void inspect(List<Monkey> monkeys, int productOfAll) {
        Item item = items.get(0);
        this.operate(item, productOfAll);
        test.testValue(this.id, item, monkeys);
        this.inspections++;
    }

    public void inspect(List<Monkey> monkeys) {
        Item item = items.get(0);
        this.operate(item);
        test.testValue(this.id, item, monkeys);
        this.inspections++;
    }

    public Test getTest() {
        return test;
    }

    public void setTest(Test test) {
        this.test = test;
    }

    public List<Item> getItems() {
        return items;
    }

    public int getInspections() {
        return inspections;
    }
}


public class Day11 {

    public static int p1(List<String> data) {
        List<Monkey> monkeys = new ArrayList<>();
        Test t = null;
        for (String s : data) {
            if (s.startsWith("Monkey")) {
                String[] parts = s.split(" ");
                Monkey m = new Monkey(Integer.parseInt(parts[1].substring(0, parts[1].length() - 1)));
                monkeys.add(m);
            } else if (s.startsWith("  Starting")) {
                String[] parts = s.split(":");
                parts = parts[1].split(",");
                for (String s2 : parts) {
                    Item item = new Item(Integer.parseInt(s2.replace(" ", "")));
                    monkeys.get(monkeys.size() - 1).add(item);
                }
            } else if (s.startsWith("  Test")) {
                t = new Test(Integer.parseInt(s.split(" ")[5]));
            } else if (s.startsWith("    If true")) {
                String[] parts = s.split(" ");
                t.setTrueMonkey(Integer.parseInt(parts[parts.length - 1]));
            } else if (s.startsWith("    If false")) {
                String[] parts = s.split(" ");
                t.setFalseMonkey(Integer.parseInt(parts[parts.length - 1]));
                monkeys.get(monkeys.size() - 1).setTest(t);
            }
        }

        for (int i = 0; i < 20; i++) {
            for (Monkey monkey : monkeys) {
                int nItems = monkey.getItems().size();
                for (int j = 0; j < nItems; j++) {
                    monkey.inspect(monkeys);
                }
            }
        }

        monkeys.sort(Comparator.comparingInt(Monkey::getInspections));

        return monkeys.get(monkeys.size() - 1).getInspections() * monkeys.get(monkeys.size() - 2).getInspections();
    }

    public static long p2(List<String> data) {
        List<Monkey> monkeys = new ArrayList<>();
        Test t = null;
        for (String s : data) {
            if (s.startsWith("Monkey")) {
                String[] parts = s.split(" ");
                Monkey m = new Monkey(Integer.parseInt(parts[1].substring(0, parts[1].length() - 1)));
                monkeys.add(m);
            } else if (s.startsWith("  Starting")) {
                String[] parts = s.split(":");
                parts = parts[1].split(",");
                for (String s2 : parts) {
                    Item item = new Item(Integer.parseInt(s2.replace(" ", "")));
                    monkeys.get(monkeys.size() - 1).add(item);
                }
            } else if (s.startsWith("  Test")) {
                t = new Test(Integer.parseInt(s.split(" ")[5]));
            } else if (s.startsWith("    If true")) {
                String[] parts = s.split(" ");
                t.setTrueMonkey(Integer.parseInt(parts[parts.length - 1]));
            } else if (s.startsWith("    If false")) {
                String[] parts = s.split(" ");
                t.setFalseMonkey(Integer.parseInt(parts[parts.length - 1]));
                monkeys.get(monkeys.size() - 1).setTest(t);
            }
        }

        int productOfAll = 1;
        for (Monkey monkey : monkeys) {
            productOfAll *= monkey.getTest().getValue();
        }

        for (int i = 0; i < 10000; i++) {
            for (Monkey monkey : monkeys) {
                int nItems = monkey.getItems().size();
                for (int j = 0; j < nItems; j++) {
                    monkey.inspect(monkeys, productOfAll);
                }
            }
        }

        monkeys.sort(Comparator.comparingInt(Monkey::getInspections));

        return (long) monkeys.get(monkeys.size() - 1).getInspections() * monkeys.get(monkeys.size() - 2).getInspections();
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<String> data = new ArrayList<>();
        Scanner scanner = new Scanner(new File("input.txt"));
        while (scanner.hasNextLine()) {
            data.add(scanner.nextLine());
        }
        scanner.close();
        long start = System.nanoTime();
        System.out.println("Part 1 : " + p1(data));
        System.out.println("Time for part 1 : " + String.valueOf((System.nanoTime() - start)/1000000000.0) + "s"); // 7.93 ms
        start = System.nanoTime();
        System.out.println("Part 2 : " + p2(data));
        System.out.println("Time for part 2 : " + String.valueOf((System.nanoTime() - start)/1000000000.0) + "s"); // 28.54 ms
    }


}
