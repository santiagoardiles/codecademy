package classes;

public class Dog {

    // Instance fields.
    String breed;
    boolean hasOwner;
    int age;

    // Constructor.
    public Dog(String dogBreed, boolean dogOwned, int dogYears) {

        breed = dogBreed;
        hasOwner = dogOwned;
        age = dogYears;
    }

    // Main.
    public static void main(String[] args) {

        Dog fido = new Dog("poodle", false, 4);
        Dog nunzio = new Dog("shiba inu", true, 12);
        boolean isFidoOlder = fido.age > nunzio.age;
        int totalDogYears = nunzio.age + fido.age;

        // Printing.
        System.out.println("Two dogs created: a " + fido.breed + " and a " + nunzio.breed);
        System.out.println("The statement that fido is an older dog is: " + isFidoOlder);
        System.out.println("The total age of the dogs is: " + totalDogYears);
    }
}
