# Checking for Properly Nested Brackets
This assignment is drawn from the [ACM's](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery) Intercollegiate Programming Contest (the ICPC), an annual tournament in which teams of three students from colleges and universities across the world compete to see how quickly they can write programs to solve specific tasks.

During the actual contest, teams submit their code to an automated judge who runs their code against several (secret) test cases to verify whether it produces the correct output. The real contest has both time pressure and penalties for incorrect/incomplete submissions, but you don't have to worry about that here.

Your submission will be a single-file python program that runs correctly on all the test inputs for the following task. It should read input from the `input.txt` file and write the solution to an output file named `output.txt`.

## Nesting a bunch of Brackets
In this problem, we consider expressions containing opening brackets and closing brackets that are either properly or improperly nested. 
```
( a + $ ( b = ) ( a ) )    # this is properly nested

( a + $ ) b = ) ( a ( )    # this is not
```

There will be several pairs of brackets, so we have to impose a second condition on the expression: the matching brackets should be of the same kind. Consequently `(())` is OK, but `([))` is not. The pairs of brackets are:
```
(  )
[  ]
{  }
<  >
(*  *)
```
The two characters `(*` should be interpreted as one symbol (or token), not as an opening bracket `(` followed immediately by an asterisk, and similarly for `*)`. The combination `(*)` should be interpreted as `(*` followed by `)`.

Write a program that checks whether expressions are properly nested. If the expression is **not** properly nested your program should determine the position of the offending bracket &mdash; that is, the position at which the expression can be determined as improperly nested. Don’t forget &mdash; `(*` counts as one, as does `*)`. The characters that are not brackets also count as one.

**Input**

The input is a text file. Each line contains an expression to be checked followed by and end-of-line marker. No line contains more than 3000 characters. The input ends with a standard end-of-file marker.

**Output**

The output is a textfile named `output.txt`. Each line contains the result of the check of the corresponding inputline. That is, ‘YES’ (in upper case), if the expression is OK, or (if it is not OK) ‘NO’ followed by a space and the position of the error.

Sample Input
```
(*a++(*) 
(*a{+}*)
```
Sample Output
```
NO 6
YES
```
 

Sample Input 2 (input.txt)
```
(*a++(*)
(*a{+}*)
    <************)>
    ()(***)(**)
   ()(***)(*)
({{}{}}[{(){}[]}
   ([))
 ()(**)
    ()*
 aaaaaaa
    aaa(aaaa
 *******
(([(
 ```
Sample Output 2 (output.txt)
```
NO 6
YES
NO 17
YES
NO 10
NO 17
NO 6
YES
YES
YES
NO 13
YES
NO 4
```

## Hints
In earlier readings, you were introduced to the concept of <a title="Using Lists as Stacks" href="https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks" target="_blank">Using Lists as Stacks</a>. This problem would lend itself nicely to such a strategy. Also, carefully consider whether a `while` loop or a `for` loop is more beneficial for accomplishing this task.

## Submitting your work
To submit your solution for grading, you will need to create a github [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). Refer to the `PR Workflow` article in your course content for details.
