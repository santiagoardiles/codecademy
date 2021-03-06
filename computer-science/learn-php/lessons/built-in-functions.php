<?php
// --------------- Codecademy. --------------- //
//                                             //
//     PATH: Computer Science.                 //
//     TRACK: Learn PHP.                       //
//     LESSON: PHP Built-in Functions.         //
//                                             //
// --------------- Codecademy. --------------- //


// ------- Exercise 1. ------- //
$first = "Welcome to the magical world of built-in functions.";

$second = 82137012983;

echo gettype($first);
echo gettype($second);

echo var_dump($first);
echo var_dump($second);


// ------- Exercise 2. ------- //
echo strrev(".pu ti peeK .taerg gniod er'uoY");
echo strtolower("SOON, tHiS WILL Look NoRmAL.");
echo str_repeat("\nThere's no place like home.\n", 3);


// ------- Exercise 3. ------- //
function calculateDistance($num1, $num2)
{
    return abs($num1 - $num2);
}

function calculateTip($num)
{
    return round($num + $num * 0.18);
}


// ------- Exercise 4. ------- //
echo getrandmax();
echo "\n";
echo rand();
echo "\n";
echo rand(1, 52);

