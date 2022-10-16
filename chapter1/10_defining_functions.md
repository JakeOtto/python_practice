# Defining Functions

Unlike some languages, Python does not come with hundreds of different in built functions. This means that very often we have to create our very own functions in order to fulfill the needs of our program.

So, whilst it is good practice to check to see whether or not Python already has a function you can use [(the Python docs are a good place to start)](https://docs.python.org/3/), it is rather common practice to make our own.

### Methods vs Functions: A Reminder

What is the difference between a method and a function?

Methods _belong_ to specific objects, like strings and are _called on_ those objects.

Calling a method on a string looks like this.

```python
>>> "Calling a method".upper()
'CALLING A METHOD'
```

Functions don't _belong_ to anything and are not _called on_ anything.

Calling a function looks like this.

```python
>>> len("Calling a function")
18
```

## Custom Functions

Imagine that, as part of a program you're building, you need to calculate an employee's monthly salary after tax. The calculation would involve several steps...

- Find their gross annual salary
- Calculate their national insurance contribution
- Calculate the income tax deduction
- Calculate their pension contribution
- Check if they're paying off a student loan. If they are, make the correct deduction.
- Add a bonus, if they get one

And many of these steps could be further broken down into multiple sub-steps.

If you had to do this, every time that you needed to show someone's net monthly salary, it would get tiresome and the codebase would get bloated. What if you could wrap all those steps in a custom function and then just call that function when you need to do those calculations?

Your codebase would be more concise, less repetitive and, last but not least, that long series of calculations would get it's own meaningful name (the function's name).

## Video

Here's the (<!-- OMITTED -->)[video](https://youtu.be/Sn7OCUMJQg4).

## Learning objectives

In this section, you will learn how to:
- Define your own functions

## Part One: Your First Functions

Let's start with something simple. Do this in a Python REPL...

``` python
>>> def say_hello():
>>>    return "hello"

>>> say_hello()
hello
```

To define a function, we use the `def` keyword. Then follows the function's name, some parenthesis (round brackets `()`) and then a colon `:`. Like an `if` statement, a function definition (first line) ends with the `:` colon. 

On the next line is where we write the function body, indicated by a tab in. Remember, Python is 'Whitespace Dependant' - the line underneath the definition is one column to the right. This, again, is similar to the `if` statement.

Right now, the `hello()` function does not take any arguments, we can tell that because the parentheses are empty `()`, so it cannot be used to greet a specific person by name. Let's fix that. Try this in a REPL.

```Python
>>> def hello(person):
>>>    return "hello, " + person
```

Now it takes one argument, a person's name, and uses concatenation to return a personal greeting. Nice! Notice how function signature (the first line) references `person` which then appears later, on line 2, when we do the concatenation. This is a variable that will hold whatever name we provide when executing the function.

If we do this...

``` python
>>> hello("Mina")
```

`"Mina"` is assigned to the `person` variable and `hello, Mina` is returned.

If we do this...

```Python
>>> hello("Bakary")
```

`"Bakary"` is assigned to the `person` variable and `hello, Bakary` is returned.

If we do this...

```Python
hello("Rabiah")
```

`"Rabiah"` is assigned to the `person` variable and `hello, Rabiah` is returned.

And so on :)

### Multiple arguments

So far, the functions we've defined only take a single argument (input) each. What if you needed to provide multiple arguments? The answer is simple, put them all in the parentheses and separate them with commas.

**Try it out now**

```python
def hello_everyone(name1, name2, name3):
  return "hello " + name1 + ", " + name2 " and " + name3
```

## Over to You

In a new file, define and execute some functions, one for each task below...

- Concatenate all the names of everyone in your family
- Add two numbers
- Calculate the number of seconds in X weeks, where X is a numerical argument

## Reflect and Review

In this section we learned how to define functions.

**Please pause at this point to reflect and review your learning...**

In a few sentences, describe:
- The benefit of being able to define your own functions
- The syntax / structure of a function


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=10_defining_functions.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F11_putting_chapter_1_into_practice.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
