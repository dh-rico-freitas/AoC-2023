# AoC-2024
My attemp to save Christmast.

*If you don't know what is this about go to
[Advent of Code 2023](https://adventofcode.com/2023/).*

I don't own any right on the puzzles themselves.

Each puzzle will be solved in a file named ``dd-p.py`` where *dd* is two digit
day and p is puzzle number (1-2).

The input data will be saved in input/ with the same name format with the
correspondin extension (most probably .txt).

# 12-03
2 days late, but half sunday to make for it!

## day 1 - puzzle 1

Who let the junnior do the job?

This could be solved by regex, but I will use that as a last resort.

Only comment, read the problem to the end instead of half guessing the question.


## day 1 - puzzle 2

WHO let the F** JUNNIOR do the job?

Ideas:
* Replace text nubmers by digits and use the same get_number function
  used in puzzle 1. 

  Lot of unnecesary work. Risk of some overlapping numbers messing the
  conversion (eighThree)

* Get the index of all the starting possition of number words and individual
  digits. 

  Also lot of repeated work.

* Make a function that walk the string looking for any of the possible first
  characters.
  Check if the substring starting in this possition is a number.
  On succes return the number converted to int, on failure continue.

* Go to read 

* All from above using regex.
