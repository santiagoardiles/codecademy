<?php
// Codecademy
// Learn PHP
// Lessons: Introduction to PHP functions


// ------- Iteration 1. ------- //
function calculateArea($width, $height)
{
    return $width * $height;
}

echo calculateArea(100, 200);


// ------- Iteration 2. ------- //
function calculateVolume($width, $height, $depth)
{
    return $width * $height * $depth;
}

echo calculateVolume(100, 200, 300);


// ------- Iteration 3. ------- //
function calculateTip($mealCost, $tipPercent = 20)
{
    return $mealCost + ($mealCost * $tipPercent / 100);
}

echo calculateTip(100);
echo calculateTip(100, 35);


// ------- Iteration 4. ------- //
$string_one = "you have teeth";
$string_two = "toads are nice";
$string_three = "brown is my favorite color";

function convertToQuestion(&$str)
{
    $str = "Do you think " . $str . "?\n";
}

convertToQuestion($string_one);
convertToQuestion($string_two);
convertToQuestion($string_three);

echo $string_one;
echo $string_two;
echo $string_three;


// ------- Iteration 5. ------- //
$language = "PHP";
$topic = "scope";

function generateLessonName($concept)
{
    global $language;
    return $language . ": " . $concept;
}

echo generateLessonName($topic);
