<?php
// --------------- Codecademy. --------------- //
//                                             //
//     PATH: Computer Science.                 //
//     TRACK: Learn PHP.                       //
//     PROJECT: Mad Libs.                  //
//                                             //
// --------------- Codecademy. --------------- //

function generateStory($singular_noun, $verb, $color, $distance_unit)
{
    $story = "\nThe ${singular_noun}s are lovely, ${color}, and deep.\nBut I have promises to keep,\nAnd miles to go before I ${verb},\nAnd ${distance_unit} to go before I sleep.\n";

    return $story;
}

echo generateStory("dog", "run", "white", "meters");
echo generateStory("cat", "walk", "black", "miles");
echo generateStory("parrot", "fly", "grey", "kilometers");
