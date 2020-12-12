// Variables: Mad Libs.
package projects;

public class MadLibs {
    // Description: Creates a not so crazy story.
    // Author: Santiago Ardiles.
    // Date: 20.06.2020

    public static void main(String[] args) {
        int number = 7;
        String name1 = "Santiago";
        String name2 = "Andrés";
        String adjective1 = "excellent";
        String adjective2 = "happy";
        String adjective3 = "cool";
        String verb1 = "running";
        String noun1 = "dog";
        String noun2 = "avocado";
        String noun3 = "elephants";
        String noun4 = "airplane";
        String noun5 = "capybaras";
        String noun6 = "submarine";
        String place1 = "Madagascar";

        // Story's template.
        String story = "This morning " + name1 + " woke up feeling " + adjective1 + ". 'It is going to be a "
                + adjective2 + " day!' Outside, a bunch of " + noun1 + "s were protesting to keep " + noun2
                + " in stores. They began to " + verb1 + " to the rhythm of the " + noun3 + ", which made all the "
                + noun4 + "s very " + adjective3 + ". Concerned, " + name1 + " texted " + name2 + ", who flew " + name1
                + " to " + place1 + " and dropped " + name1 + " in a puddle of frozen " + noun5 + ". " + name1
                + " woke up in the year " + number + ", in a world where " + noun6 + "s ruled the world.";

        System.out.println(story);
    }
}
