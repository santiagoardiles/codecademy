<?php
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

class Pajamas
{
    private $owner, $fit, $color;

    function __construct(
        $owner = "unclaimed",
        $fit = "fine",
        $color = "white"
    ) {
        $this->owner = StringUtils::secondCase($owner);
        $this->fit = $fit;
        $this->color = $color;
    }

    public function describe()
    {
        return "$this->owner's $this->color pajamas fit $this->fit.";
    }
}

$chicken_PJs = new Pajamas();

echo chicken_PJs->describe();
