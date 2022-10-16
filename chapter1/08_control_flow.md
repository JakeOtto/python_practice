# Control Flow

If you were asked you to print `'Hello World'`, to the terminal, you might find this a quick and simple step. If you were asked to print `'Hello World'` to the terminal a thousand times, you might (quite rightly) think this to be a rather time consuming, and no doubt, excruciatingly boring task.

Sometimes we want to execute sections of code repeatedly. When all is said and done, is not the purpose of programming to make our job of manually inputting instruction easier? For repetitive tasks, such as searching meticulously through a big set of data, or adding a single value to a large list; we can use loops.

Loops are a way of giving an instruction in python, and executing some code to either a *finite* amount of iterations, or to continue doing a task until a *condition* is met.

## Video

Here's the (<!-- OMITTED -->)[video](https://youtu.be/jCcQ4F-nIYc) for this section.

## Learning Objectives

In this section, you'll learn

- How to let your program automate decisions, using _for loops_
- How to let your program automate decisions, using _while loops_
- How to use slice notation to manipulate loops

## Part One: For Loops

Let's go back to our earlier example. If I asked you to print `'Hello World'` to the terminal, you might write something like this:

``` python
>>> print('Hello World')
```

And you would be right. But if you needed to execute that line multiple times, it would be quicker, and easier, to nest that `print()` method in a loop. Specifically, a `for` loop:

```python
>>> for i in range(5):
... 	print('Hello World')
```

How did that go in your terminal? Let's break down what is happening in this `for` loop. Give these examples a go in your python REPL:

``` python
>>> for number in range(10):
...     print(number)
... 
0
1
2
3
4
5
6
7
8
9
```

After we use the keyword `for` we use a `loop variable`, sometimes called an `index variable`. In our first example we simply used the letter `i`, you will see this a lot in the Python documentation and online. Commonly, the `i` stands for index.

But we can use any standard variable naming convention we like, as it is, in fact just another type of variable. This is why in the second example we use `number` to store each number as it iterates (loops over) through the `range(10)`.

Lets start using for loops to mutate, or change, some of our data!

``` python
>>> num = 10
>>> for i in range(5):
...		num = num + 5
... 	print(num)
>>> # ???
```

What was the last number in the terminal? What about mutating a `String`?

``` python
>>> name = input("Enter your name!: " )
>>> for char in name:
...		print("Give me a " + char + " !") 
>>> #???
```

Because a `String` is a type of sequence, it can be iterated through. This sort of iteration will become much more handy when we begin to look at more complex data structures like lists and dictionaries.

For now, although it's fun to print lot's of things to the terminal, there isn't much use for our for loops, but as the progression in development is built upon the transfer, manipulation and extrication of data - it is good practice to get familiar with the `for` loop.

Try these out:

``` python
>>> hamlet = "To be, or not to be: that is the question: Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles, and by opposing end them?"
>>> for x in hamlet.split(" "):
...		print(x)
...		if x == ":" or x == ",":
...			print("\n\n") # "\n" = a new line
```

The method `range()` can take multiple arguments to interesting effect; remember _start, stop, and step_ values from the previous section on slice notation:

``` python
>>> for i in range (0, 10, 2):
...     print(i)
... 
0
2
4
6
8
```

Where the first argument is the beginning value, the second is the stopping value (not including it), and the third is the step. With that in mind, how might we just print the odd values from 1 - 31?

``` python
>>> for i in range(#?, #?, #?):
... 	print(i)
...
```

We will come back to _start, stop and step_ values again when we look in a bit more detail at slice notation further on in the course.

## Part Two: While Loops

For loops are very useful when we want to loop through something a *finite* amount of times, or when the length of a piece of data is known. 

But what about when we do not know how long it might take to find something, or if we need a condition to be met?

This is where `while` loops become useful.

Consider this example:

``` python
# I am creating an rpg style game in python
# I have a favourite number - 77
# In order for the player to pass to the next level they must 'roll' 77 or higher out of a 100 sided dice.
>>> from random import randint
>>> favourite_num = 77
>>> 
>>> rand_num = randint(0, 100)
>>> 
>>> while rand_num != favourite_num:
...     print(f"The random roll is: {rand_num}")
...     rand_num = randint(0, 100)
```

The program will run the loop `while` the condition is not met. We can use while loops to iterate continuously until a condition has or has not been met.

The conditions work in just the same way as our `if` statements from before, so we can make our conditions very specific if need be:

``` python
>>> weather = "overcast"
>>> 
>>> city = "lisbon"
>>> 
>>> count = 0
>>> 
>>> while weather == "overcast" and city == "lisbon" and count < 5: 
...     count += 1
...     print(f"The weather is still {weather} in fair {city}") 
... 
```

Notice how the above example has that variable `count` in. That was to make sure we didn't get caught in an infinite loop - if you don't set your conditions correctly, you can trap your program into running forever. 

To get out of it make sure to press the `control + C` keys on your keyboard. Try it here:

``` python
>>> while True:
...		print("This will run foreverrrrrr!")
...     # Hit `ctrl + c`!
...
```



## Reflect and Review

In this section we covered `for` loops and `while` loops and how they can be used in a program to make decisions.

> Loops really come into their own when we have more of an understanding of iterable data structures like Lists and Dictionaries, and we will be making much more use of them in those sections.


**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
- What is meant by a loop?
- How the `for` and `while` loops differ? Why would you use one over the other?
- How to escape an infinite loop!
- How the start, stop and step values works to iterate at specific points.


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=08_control_flow.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F09_executing_python_files.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
