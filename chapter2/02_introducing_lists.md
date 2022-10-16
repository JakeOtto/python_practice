# Lists

A List is a _sequence_, or array, of items. Lists are extremely useful and commonly used in many different programming languages (normally known as arrays). In this section, you'll learn about how to use them, in Python.

## Video

The video for this section is in two parts...

- [Here's the first part](https://youtu.be/I_oMPekZLwM)
- [Here's the second part](https://youtu.be/NB6dau9kr6Q)

## Learning Objectives

In this section, you will learn:
- How to create Lists in Python
- How to add items to a List
- How to read / retrieve a single item in a List

## Part One: Creating a List

A List of the numbers 1 to 9 would look like this.

``` python
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Try creating some lists in a python REPL now.

Python lists can contain anything – Strings, Integers, Floats, Booleans – you can even create lists of lists, but let's not do _that_ yet!

## Part Two: Adding Items to a List

If you want to add things to a list, you can use the `.append()` method.

```python
>>> my_list = []
[]
>>>> my_list.append("hello")
['hello']
>>> my_list.append("world")
["hello", "world"]
```

## Part Three: Accessing Items in a List

You can access elements in lists based on their position. To do that, use the `[]` method, combined with the item's index. Note that the index of the first item in a python list is 0, not 1.

```python
>>> # create a list
>>> my_list = ["hello", "world"]
["hello", "world"]
>>> # access the first element
>>> my_list[0]
"hello"
>>> # access the second element
>>> my_list[1]
"world"
```

> What happens if you create a list of two items called `my_list` and then do `my_list[3]`? Try it now.

> What happens if you try to do `my_list[-1]`? Try that as well!

Remember our section on `slice` notation and square brackets in Chapter 1? We used _start, stop and step_ values to take slices from Strings - well you can do the same with Lists:


``` python
>>> track_list = ["Sympathy For The Devil", "Leech", "Dragonaut", "Green Machine", "Sound & Vision"]
>>> track_list[0]
'Sympathy For The Devil'
>>> track_list[0:2]
['Sympathy For The Devil', 'Leech']
>>> track_list[0:4]
['Sympathy For The Devil', 'Leech', 'Dragonaut', 'Green Machine']
>>> track_list[0:4:2]
['Sympathy For The Devil', 'Dragonaut']
```

## Part Four: A List of Passwords?

Could we use a list to store a list of passwords? Probably, yes, we could. Would it be the best option, probably not, no. Let's find out why.

We could build a list that just contained passwords, like this.

```python
>>> passwords = ["password", "123456", "qwerty"]
["password", "123456", "qwerty"]
```

That would be fine, but there's no record of which service each password is for. So we could build a list that contained passwords and their associated services.

```python
>>> passwords = ['acebook', '12345678!', 'makersbnb', 'qwertyu123!']
["acebook", "12345678!", "makersbnb", "qwertyu123!"]
>>> # We could do something like this...
>>> >>> passwords[::2]
['acebook', 'makersbnb']
```

But this is going to get messy very quickly – for example, some passwords might look like service names, and vice versa, which will get confusing in the middle of a long list. A further option would be to build a nested list – a list of lists and, at first, this might seem tempting but remember the [Law of Instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument)!

```python
>>> # a nested list where each sub-list contains a service name and password
>>> passwords = [["acebook", "12345678!"], ["makersbnb", "qwertyu123!"]]
[["acebook", "12345678!"], ["makersbnb", "qwertyu123!"]]
```

It's a little better since each password is now stored alongside the name of a service, but to find the password for a specific service, we'd have to search through the list of lists, which is not very efficient. We can do much better than a list of lists, by using a Dictionary, which is what we'll do in the next section.

If we think of variables and lists as boxes, where lists are boxes that contain multiple items; you could think of using square brackets as 'opening up' the box to retrieve something inside.

So if you have a nested list, a list within a list, you simply have to use two square brackets to open up the box inside the box:

``` python
>>> passwords = [["acebook", "12345678!"], ["makersbnb", "qwertyu123!"], ["willslazeremporium", "pewpew123"]]
>>> passwords[0]
['acebook', '12345678!']
>>> passwords[0][0]
'acebook'
>>> passwords[1]
['makersbnb', 'qwertyu123!']
>>> passwords[1][0]
'makersbnb'
>>> passwords[2]
['willslazeremporium', 'pewpew123']
>>> passwords[2][1]
'pewpew123'
```

It can get messy quite quickly, lists within lists, so be careful not to over complicate your data structures!

## Part Five: List Methods

So, we won't use a list for storing the passwords but they will come in handy at some point so let's dig a bit deeper.

In Chapter 1, you learned about String methods, which can be called on any String. In this section, you'll learn about List methods, which can be called on any List. We'll start with some simple examples in this section, then in chapter 3 you'll see some more advanced methods.

Call each of these methods on a list of Integers `[1,2,3,4,5]`. Be sure to check the List after each one, to see if has been changed (or _mutated_).

- `clear()`
- `reverse()`
- `pop()`
- `index()`
- `sort()` (You may want to change the order first!)


Some of them will also work on a list of Strings `['cat', 'potato', 'python', 'senegal', 'purple']`.  Try them out!

You can find more [List methods](https://docs.python.org/3/tutorial/datastructures.html) in the Python Docs.

## Reflect and Review

In this section, we introduced the concept of a list and how to use it. We also learned how to create arrays, add items to arrays, and access items in lists. They're very useful but they are not the solution to every problem, just like the hammer is not the right tool for every job.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
- What a list is
- How to create a list
- How to add items to a list
- How to access items in a list


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=02_introducing_lists.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F03_introducing_dictionaries.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
