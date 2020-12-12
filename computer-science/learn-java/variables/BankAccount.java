// Variables: Review.
package variables;

public class BankAccount {
    public static void main(String[] args) {
        double balance = 1000.75;
        double amountToWithdraw = 250;

        // Iteration 1.
        double updatedBalance = balance - amountToWithdraw;

        // Iteration 2.
        double amountForEachFriend = updatedBalance / 3;

        // Iteration 3.
        int ticketPrice = 250;
        boolean canPurchaseTicket = amountForEachFriend >= ticketPrice;

        System.out.println(canPurchaseTicket);

        // Iteration 4.
        System.out.println("I gave each friend " + amountForEachFriend + "...");
    }
}
