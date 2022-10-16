# Functions

In section 1, we saw that it's possible to join two `string`s, or _concatenate_ them, using `+`, like so...

```python
>>> "Hello, " + "World!"
'Hello, World!'
```

Being able to concatenate `string`s is super useful. For example, you might have a person's first name assigned to one variable and their surname assigned to another. In that case, you could return their full name by concatenating those two variables.

```python
>>> first_name + surname
'Guido van Rossum'
```

/** EDU interpolation, using f-strings, is a new python feature and may not be widely used but it does generalise to other languages so I'd vote that we keep it - Eddie **/

It's also possible to build strings using _interpolation_. This technique allows you to insert content into strings. Here's an example where the `name` is interpolated into a string – the content to insert is placed inside `{}`. NOTE: This string must be declared using an "f" at the beginning - these are known as "f-strings".

```python
>>> name = 'Mina'
>>> f"Hello #{name}, how are you today?"
'Hello #Mina, how are you today?'
```

Here's another example.

```python
>>> date = '3/8/2022'
>>> f"The date today is {date}"
'The date today is 3/8/2022'
```

But we can do much, _much_, more than concatenate and interpolate Strings!

In this section, we'll go beyond concatenation (and interpolation) and you'll learn the building blocks that will be used in your first real program - a password validator.

## Video

Here's the [video](/** @TODO */) for this section.

## Learning Objectives

In this section, you will learn:

- What _functions_ are
- What arguments are
- Why functions are useful
- Where to learn about Python's built in functions

## Part One: What are Functions?

Functions are like little machines that take inputs, called arguments, and provide outputs, called return values.

Here are some analogies:
- A toaster, which takes bread as an input and returns toast.
- A blender, which takes fruit as an input and returns a smoothie.
- A printer, which takes paper and some text data as inputs and returns a document, with the text data printed on it.

It's possible to create your own functions and you'll learn how to do that later on in this chapter. Python, however, comes with some built in functions for things that lots of people are likely to find useful. We'll start by learning how to use some of those functions.

To use a function you type out it's name, followed by parentheses and you put any arguments (inputs) inside the parentheses.

```python
functionName(argument)
```

Here's an example where I use the `len` function to get the length of a string.

```python
>>> len("This is a very very long string. How long, you ask? Let's find out!")
67
```

Note that if you don't add the parentheses, you just get the function returned back to you.

```python
>>> len
<built-in function len>
```

The return value of `len`, an _integer_, which is a data type used to represent whole numbers (not decimals). If you wanted to convert an integer intro a string, for some reason, you could use the `str` function, like this.

```python
>>> str(67)
'67'
```

And if you wanted to convert it back to an integer you can do this.

```python
>>> int('67')
67
```

You can also assign return values to variables.

```python
>>> word = 'hippopotamus'
>>> wordLength = len(word)
>>> wordLengthAsString = str(wordLength)
>>> wordLengthAsString
'12'
```

## Exercises

Try the following functions in your Python REPL. The goal is to build some muscle memory for executing functions. You don't need to memorise what each one does.

- `type`, which takes anything as an argument and returns its _data type_. Try it with a string and then an integer.
- `print`, which takes anything as an argument and prints it to the terminal. Try it with a string and then an integer. It'll seem useless at the moment but will soon become your best friend.
- `abs`, which takes a number as an argument and always returns a positive value. Try it with both positive and negative numbers.

The full list of Python's built in functions is [here](https://www.w3schools.com/python/python_ref_functions.asp), but many of them rely on concepts we've not yet covered so bookmark it for later but don't spend a lot of time trying to use them right now.

## Reflect and Review

In this section, you learned about functions and arguments.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

- What functions are
- What arguments are
- How to use a function
- Why functions are useful
- Where to learn about Python's built in functions


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=03_functions.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F04_methods.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
