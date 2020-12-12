// Classes: Constructors.
package classes;

public class Store {

    // Instance fields are declared here.
    String productType;
    int inventoryCount;
    double inventoryPrice;

    // Constructor method.
    public Store(String product, int count, double price) {

        productType = product;
        inventoryCount = count;
        inventoryPrice = price;
    }

    // Main method.
    public static void main(String[] args) {

        Store lemonadeStand = new Store("lemonade", 3, 3);
        Store cookieShop = new Store("cookies", 12, 3.75);

        // Printing.
        System.out.println(lemonadeStand);
        System.out.println(lemonadeStand.productType);

        System.out.println(cookieShop);
        System.out.println(cookieShop.productType);
    }
}
