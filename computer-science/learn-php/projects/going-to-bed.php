<?php
// --------------- Codecademy. --------------- //
//                                             //
//     PATH: Computer Science.                 //
//     TRACK: Learn PHP.                       //
//     PROJECT: Going to Bed.                  //
//                                             //
// --------------- Codecademy. --------------- //

// String utilities.
class StringUtils
{
    public static function secondCase($string)
    {
        if (strlen($string) != "") {
            $string = strtolower($string);
            if (strlen($string) >= 2) {
                $string[1] = strtoupper($string[1]);
            }
            return $string;
        } else {
            return $string;
        }
    }
}

// Pajamas class.
class Pajamas
{
    private $owner, $fit, $color;

    // Constructor.
    function __construct(
        $owner = "Santiago",
        $fit = "fine",
        $color = "white"
    ) {
        $this->owner = StringUtils::secondCase($owner);
        $this->fit = $fit;
        $this->color = $color;
    }

    // Sets a new fit.
    public function setFit($new_fit)
    {
        $this->fit = $new_fit;
        return $this->fit;
    }

    // Gets description.
    public function describe()
    {
        return "$this->owner's $this->color pajamas fit $this->fit.";
    }
}

// Buttonable pajamas class.
class ButtonablePajamas extends Pajamas
{
    private $button_state = "unbuttoned";

    // Reusing `describe` function from `Pajamas`.
    public function describe()
    {
        return parent::describe() . " They also have buttons which are currently $this->button_state.";
    }

    // Method for toggling the buttons.
    public function toggleButtons()
    {
        $this->button_state = "buttoned";
    }
}


// Testing `Pajamas` class.
$chicken_PJs = new Pajamas("CHICKEN", "just right", "purple");
$chicken_PJs->setFit("super tight");
echo $chicken_PJs->describe();
echo "\n";


// Testing `ButtonablePajamas` class.
$moose_PJs = new ButtonablePajamas("moose");
$moose_PJs->toggleButtons();
echo $moose_PJs->describe();
