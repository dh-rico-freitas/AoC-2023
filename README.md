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

### Ideas:
1- Replace text nubmers by digits and use the same get_number function
   used in puzzle 1. 
 
   Lot of unnecesary work. Risk of some overlapping numbers messing the
   conversion (eighThree)

2- Get the index of all the starting possition of number words and individual
   digits. 

   Also lot of repeated work.

3- Make a function that walk the string looking for any of the possible first
   characters.
   Check if the substring starting in this possition is a number.
   On succes return the number converted to int, on failure continue.

   I could compile a table of firsts, seconds, thirds ... characters, 
   use that instead of checking for the string, but I think this is a good
   middle ground.

4- Go to read Skiena. 

5- 1-4 from above using regex.

### Let's try idea 3.

I have to handcraft the NUMBERS dict, but from there all is automatic,
and I could modify this for othere languages. Is there a little issue
if in some language one number is a prefix of other.

I like the flexibility, but dislike the extra complexity of making a 
dict of first letters. I'd like to test if this make a dent on performance.

### Take 2. 
Let's try idea 2 and see if it performance is too worst.

Add some argparse boilerplate to choose what function use
time the results. 

Idea 3. is around 10x faster than 2., so it wasn't a bad idea to implement
it in that way. But the second code is far cleaner
(except for the serch function name).
Maybe I should try to fix that.

### Take 3. 

I like the get_number_simple interface, but it's not trivial
to recreate in get_number. At this point, OO seems razonable,
two different implementations with different initialization,

Let's see.

The new implementation is OOP to reuse some code, same performance
difference.
Also I changed the cli flag to call one or other version.
The simple seems like a better baseline.

That's all for this problem.

## day 2 - puzzle 1

Let's define a parse function with simple str.split methods and some
comprehension magic.

## day 2 - puzzle 2
I was tempted to extract the minimum data needed, but I tought I'll need
the full data in part 2. I was right! Now this should be easy.

I was right. A little reduce and that's it.

## day 3 - puzzle 1
Well, that scalated quickly. 

I need a function that find a number (a series of consecutives digits)
and generate the index of the neighbours of it.

### First attempt
Full imperative approach with all the loops. 

Some mangling with off by one errors, but a strightforward implementation.
Loop line by line finding strikes of digits, sent the limits to an auxiliar
function that generate the coordinates of a bounding box, filter out
invalid coords and search for symbols in the board.

## day 3 - puzzle 2
Let's see what can I save from part 1.

Too sleepy to follow. 

# 12-08
Almost a week without time to this.

I will skip that day 3 puzzle 2 for now. 

## day 4 - puzzle 1

Easy to parse data, if n is the number of correct numbers, then 
for n> 0  p = 2^(n-1), for n = 0, p = 0, wherre p is points.

List are small, sets seems like an overkill, but, _alas_, it's a nice
overkill.

## day 4 - puzzle 2

I can keep all the parsing from part 1. 

I have to keep a record of number of copies.
I could try to make a nice algorithm, but let's start by brute
forcing it.

### first attempt

pythonese pesudo code:

Parse all data and calculate a list of number of matching numbers N.

lenght = len(N)

Create a list of the same lenght full of ones. C.

for i, n in enumerate(N):
   for j in range(i+1, min(length, N+i+1)):
      C[j] += C[i]

print(sum(C))

And this run in 24 ms. That's enough speed for me.

Let's keep going.


## day 5 - puzzle 1

OK. seems easy. Let's keep brute-forcing it. 

For each seed I will check if it's in the map range and convert it acordlingly.
If not, just pass it.

A function apply_map like:

def apply_map(s, map_):

   for dest_start, source_start, length in map_:
      if source_start <= s < source_start + length:
         return dest_start - source_start + s 
   return s


And I can use it like map(lambda x, apply_map(x, map_), seeds).

Well. Just don't use generators in loops, it get weird.

