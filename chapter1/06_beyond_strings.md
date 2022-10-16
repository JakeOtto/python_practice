# Beyond Strings

In the first three sections of this chapter we've played with some strings and you've seen that there are a whole load of methods which can be called upon any string, such as...

```python
>>> 'hello'.upper()
'HELLO'
```

But what if you want to do maths or something else that cannot be done with strings? Well, in addition to strings, there are a bunch of other data types and each one has it's own selection of methods.  Some examples of those datatypes are:

- integers
- floats
- Booleans
- lists
- dictionaries

Lists and Dictionaries are complex data types that are introduced in the next chapter. The rest are explained below.

## Video

Here's the [video](<!-- OMITTED -->) for this section.

## Learning Objectives

In this section, you will learn
- What floats are and how they are used
- What integers are and how they are used
- What Booleans are and how they are used

## Integers

Integers are whole numbers (not decimals) and they can be used in all the ways that you might expect...

```python
>>> 1 + 1
2
>>> 10 / 2
5.0
>>> 3 * 3
9
>>> 5 - 1
4
```

You can find more methods in the [Python docs](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

Note that when you divide an integer by another integer, the return value won't be an integer.  For example...

```python
>>> 10 / 3
3.3333333333333335
>>> 1 / 2
0.5
>>> 6 / 3
2.0
>>> 5 / 5
1.0
>>> 5 / 4
1.25
```

The results here are all what we call a float - read on to find out about those!

## Floats

Floats are decimal values. They're called floats because the decimal point can 'float' to any position.  I.e. You might need a number like `11.11` with the decimal point right in the middle or you might need a number like `100000000.1` where the decimal point is all the way to the right hand side... and so on.

As with integers, you can do all the basic mathematical stuff with floats - try that now.

Floats also have their own methods, which you can find in the [Python docs](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float).

### Challenge

What happens if you mix and match integers and floats? What type of number do you get back? How can you tell?

## Booleans

Booleans are a special data type named after George Boole and there are only two different values of a Boolean: `True` and `False`.

Python methods that return Booleans typically start with "is". For example `2.0.is_integer()` and `"this is not empty".isspace()`.

Booleans are simple, but they can be combined in complex ways using logical operators.  Here are some simple examples using the logical operators `and`, `or` and `not`.

```python
>>> # to return true, both sides must be true
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> # to return true, only one side needs to be true
>>> True or False
True
>>> False or True
True
>>> True or True
True
>>> False or False
False
>>> # returns the opposite of what's given
>>> not True
False
>>> not False
True
```

Yes, these are slightly useless examples contrived to show you how booleans and two logical operators work. In reality, you won't write code like that. Below you'll find a more realistic example, where the program is checking if a password is between 8 and 12 characters

```python
>>> 7 < len(password) and not password.isalpha()
# would return true or false
```
## Reflect and Review

In this section, you learned about integers, floats and Booleans.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

- What integers are and how they are different to floats
- What Booleans are plus how the `and`, `or` and `not` logical operators work


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=06_beyond_strings.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F07_conditionals.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F06_beyond_strings.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F06_beyond_strings.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F06_beyond_strings.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F06_beyond_strings.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F06_beyond_strings.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
