# Conditionals

Sometimes, in real life, we might want to act only when certain conditions are met. For example, you might decide that you're only going for a picnic if it's not raining or that you'll only try to make a cake if you have all the ingredients.

<img alt="Flowchart representing the above decisions" src="../images/ifs_flowchart.svg" width="500">

<!-- OMITTED -->  

In programming, as in life, we need the ability to make decisions based on data.

## Video

Here's the (<!-- OMITTED -->)[video](https://youtu.be/jCcQ4F-nIYc) for this section.

## Learning Objectives

In this section, you'll learn

- How to let your program make decisions, using _if statements_

## Part One: If / Else

A really common way to implement this in python is to use an `if` statement.  Here's an if statement is to decide which of two Strings is returned.

```python
>>> name = "Pedro Luis Gonçalo da Costa"
>>> if(len(name) > 25):
>>> 	return "that's a very long name"
>>> else:
>>>   	return "that's not a very long name"
```

_This might seem like a silly example, because we could just count the letters in `name`. But imagine that you don't know what value `name` holds – maybe it came from a user and maybe it will be different for every user.

Ponder this example, and give it a go if you like:

``` python
>>> name = input("What is your name?: ") 
>>> if len(name) > 7:
>>>		print(f"{name.capitalize()} is a long name!")
>>>	else:
>>>		print(f"{name.capitalize} is a short name!")  
```

Let's break down the `if` statement. On the first line (after assigning `name`) we have `if(len(name) > 25):`. The part in brackets will _resolve_ to (return) either `true` or `false`. If it resolves to `true`, the code on the third line `"that's a long name"` is executed (and the remaining code is skipped). If `name.length > 25` resolves to `false`, the next line is skipped. Then we have a _catch all_ (else) clause. It covers all situations where `name.length > 25` resolves to false.

### Whitespace

Note that after every `if`, and every `else` we must terminate the line with a colon `:`, this in turn is followed by a new line that is tabbed in, like so:

```python
>>> if (some_condition == true):
... 	# this code executes
... else:
... 	# this code executes
```

This is because python is "Whitespace Dependant". This means that the indentations underneath blocks of code matter. Python will interpret the gap left at the start of the line to mean that the code on that line will execute only if the above line runs.

This can get a little confusing at the beginning, so there are some helpful extensions in VSCode to aid us, such as [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) which colourises the columns of our code.

Just remember, as a rule of thumb, if a line of python ends with a colon `:` then the next line will be indented.

Sort this code out:

``` python
>>> name = "Ahmed"

if name == "Ahmed":
print("Hi, Ahmed")
	elif name == "Brunhilde"
		print(Hi Brunhilde)
			else:
			print("What is your name?")
```

Press `tab` on your keyboard to quickly indent a line, and `shift + tab` to de-indent a line (move back)!

<!-- OMITTED -->

Open up your python REPL (`python3` - mac, `py` - windows) and try the following. Each line should resolve to either `true` or `false`.

```python
>>> len("hello") > 2
```

```python
>>> len("hello") > 10
```

```python
>>> "hello".count("l") > 1
```

```python
>>> "hello".count("o") > 2
```

Next try adding some conditions with a colon at the end.

``` python
>>> greeting = "Hello World"
>>> if "World" in greeting:
>>>		print(greeting)
```

``` python
>>> pi = 3.141
>>> if pi > 1:
>>>		print("Pi is greater than 1!")
```

## Part Two: Elif

In many situations there will be more than one thing that we wish to check, which means we need some more _branches_ on our `if` statement. These can be added using `elif`.

```python
>>> name = "Edward Smith"
>>> if(name.length > 25):
>>>   	return "That's a very long name"
>>> elif(name.length > 20):
>>>   	return "That's a long name"
>>> else:
>>>   	return "That's not a particularly long name"
```

Now open up your python REPL and try playing with some `if` statements. Try adding more and more branches. See what happens if you leave off the `else`. What happens when you *nest* your `if` blocks?! 

Try changing `num` around to see what you get.

``` python
>>> num = 64
>>> if num > 50:
>>>		if num % 2 == 0:
>>>			print(f"This number, {num}, is even and larger than 50!")
>>> 	elif num % 3 == 0:
>>>			print(f"This number, {num}, is divisible by 3 and larger than 50!")
>>>		else:
>>>			print(f"This number {num} is odd, and not divisible by 3!")
>>>	else:
>>> 	print(f"This number, {num}, is too small!")
```

### Not Equal

In Python, as in many programming languages =, sometimes we want to check if something **does not** evaluate to something else.

A quick way to do this is with the `!=` operator, sometimes called the not operator or bang operator.

``` python
>>> name = "June"
>>> if name != "Will":
...		print("You aren't Will! Who are you?")
...	else:
...		print("You must be Will!")
```

A quick and easy way of reversing the condition.

## Reflect and Review

In this section we covered `if` statements and how they can be used in a program to make decisions.

> At this point, you might be getting sick of having to write out every line of code, every time. You'll see how to avoid that in the next section.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
- What is meant by conditional
- How the `if` and `elif` branches of an if statement work
- How the `else` branch of an if statement works


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=07_conditionals.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F08_control_flow.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F07_conditionals.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F07_conditionals.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F07_conditionals.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F07_conditionals.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F07_conditionals.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
