<?php
// --------------- Codecademy. --------------- //
//                                             //
//     PATH: Computer Science.                 //
//     TRACK: Learn PHP.                       //
//     LESSON: PHP Classes.                    //
//                                             //
// --------------- Codecademy. --------------- //


// ------- Beverage 1. ------- //
class Beverage
{
    private $temperature, $color;
    protected $opacity;
    function __construct($temperature, $color)
    {
        $this->temperature = $temperature;
        $this->color = $color;
    }
    function getInfo()
    {
        return "This beverage is $this->temperature and $this->color.";
    }
}


// ------- Milk. ------- //
class Milk extends Beverage
{
    function setOpacity($opacity)
    {
        $this->opacity = $opacity;
    }
}


// ------- Beverage 2. ------- //
class Beverage2
{
    private $color;

    function setColor($color)
    {
        $this->color = strtolower($color);
    }
    function getColor()
    {
        return $this->color;
    }
}


// ------- Static things. ------- //
class AdamsUtils
{
    public static $the_answer = 42;
    public static function addTowel($string)
    {
        return $string . " and a towel.";
    }
}

$items = "I brought apples";

echo AdamsUtils::$the_answer;
echo AdamsUtils::addTowel($items);
