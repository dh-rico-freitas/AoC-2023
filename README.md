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

## day 5 - puzzle 2
How bad can be to brute force this? Let's try.

Well, that was too bad. 
Back to the sketch pad.

Idea, reverse the mapping and walk lands from 0 to inf searching if
the seed used is one of the provided.

8s. It ain't much but it's honest job.

## day 6 - puzzle 1
Loop through all posible times( actually 1 to t-1, the zero and t don't move at all).

Works ok

## day 6 - puzzle 2
Minimal changes to puzzle 1. 

Finish in less than 4s.

## day 7 - puzzle 1
I need to keep the original hand to same-type order.

The key function is a little hacky, but I thing python sorted cached the
results (I have to check) but it's prety fast.

## day 7 - puzzle 2
I don't know if this is pretty easy or pretty difficult.

Can I simply sum the number of J to the card with the highest number?

2345J -> 2J 345  a pair
234JJ -> 2JJ 34  three of a kind
23JJJ -> 2JJJ 3  four of a kind
2JJJJ -> 2JJJJ   five of a kind

2234J -> 22J 34  three of a kind

Yes, this is the simplest solution.

# 12-09
New day. I think it will be a short one. Let's see.

I will retake puzzle 6.

## day 6 - puzzle 2 - take 2

I could spent some time going for the quadratic formula, but second
part could be hard in fp precision.

Anyway, knowing distance is a quadratic ecuation in press time, with
zeros at 0 and T (the race time) I could just loop until a first winning
time, and then substract 2 times that to the total Time.

In the worst case it will halve the time, and if the prior is uniform,
it should reduce time to 1/3.

It actually works better than that. From 3.9s to 0.34s 

## day 6 - puzzle 2 - take 3
I have a nother idea!
Instead of a sequential search use a nonlinear binary search.
An standar binary search will overshoot many guesses.
But in this case we known the exact equation, we can exploit that:

Our next guess will be:

x^(1/2) = (a^(1/2) + b^(1/2)) / 2 

Sqaring both sides:

x = (a + b + 2 (ab)**(1/2)) / 4 = ( (a+b)/2 + (ab)^(1/2) ) / 2

Our new candidate is the average between the aritmetic mean and the
geometric mean.
Well, that's .
I don't thin a couple less loops will offset the extra time of sqrt.

Let's try both.

Well. that's was better than expected.

```
Version 1 run in 3.85257869400084s: 49240091
Version 2 run in 0.3386094570159912s: 49240091
Version 3 run in 5.6405027862638235e-05s: 49240091
Version 4 run in 3.2215029932558537e-05s: 49240091
```

4 orders of magnitude by simply making a linear search doesn't impress
me too much. That the sqrt version is faster does.

Let's see how many recursion steps it do.

I was using the target value as stop criteria, but I need an int time,
stopping difference between max and min time is better in this cas.

Also, there is only one step difference between linear and sqr candidates. 

Instead of using the generic function I will do a linear search inlining
the next candidate function.

Unexpectdly that worked well enough. 
Next step, lets drop all the old versions and try to make a full custom
non reusable function with all possible inlined.

That works in 10μs.

That's the final attempt.
The alternative would be to resolve the equation directly, but that will
put me in the need to be careful with floating point precision.


## day 7 - puzzle 2 - take 2
I just hang this at mid work. My original Idea was pretty neat. 
Just reorder CARDS values and add a little logic around J.

The only mistake I made is handle the case where there are 5 J.

I never upload 07-1.py.


## day 8 - puzzle 1

Just brute force it. 

I used regex for parsing. Nice problem. Let me use some itertools magic.

## day 8 - puzzle 2

Nice. Easy to modify part 1.

Well. Not so nice, I went to lunch and it keep running.
I need to think.

I have a coupple of questions.

Every path (maybe with the exception of the longest)
has to had cycles.

If every cycle have only one Z and one A, and the Z is in the last possition
the total length will be the least common multiple of the cycles length.

But a cycle could happen in any place.

This sequence

AAA -> BBB -> ZZZ -> BBB 

Will have a valid stop at any odd number of steps.

Ok. Let's take that. First, identify cycles.

Let's make some data exploration.

There is only one Z in each path and they are just before the A. 
Bingo, easy solution (mostly wrong in the general case, but, who cares):

Search length of all cycles.
Just loop until get to the start. 
Register those numbers.

Then calculate the lcm and that's it.

Worked. I'm not much happy with this.

This could've be a very very difficult problem.


## day 8 - puzzle 1
I loved this problem. I got a very nice, compact and clear solution in
nine logical line of code, two of them used to read the input.


## day 8 - puzzle 2
Seems too easy... Let's see.

I was right!
Only a map more to reverse the list of numbers.
