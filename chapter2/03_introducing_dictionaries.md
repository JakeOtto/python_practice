#  Dictionaries

 Dictionaries are a bit like Lists, because they also allow you to store a collection of things.  Dictionaries, however, allow you to associate a label with each of your items, which can help to make your data a little easier to understand.  Consider the list below...

``` python
> ['pippa', 25, 'percy', 'swimming', 'football', 327]
```

What exactly does each element correspond to? It's hard to tell without labels and that's where  Dictionaries come in. Most programming languages include something along the lines of a Dictionary. They might use a different name, like HashMap or Hash, but the basic concept is always the same.

## Video

Here's the (<!-- OMITTED -->)[video](https://youtu.be/XYw5GQEoNqk) for this section.

## Learning Objectives

In this section, you will learn

- How to create a Dictionary, in  python
- How to read values stored in Dictionary
- How to add key-value pairs to a Dictionary
- How to execute some simple Dictionary methods

## Part One: Creating a Dictionary

 Dictionaries are made up of key-value pairs. The _key_ is a label and the _value_ is the piece of data that you wish to store. They look like this.

``` python
>>> person = {
>>>   "name":"Guido van Rossum",
>>>   "nationality":"Netherlands",
>>>   "favorite_programming_language" : " python"
>>> }
>>> person
 {"name":"Guido van Rossum", "nationality":"Dutch", "favorite_programming_language":" python"}
```

**Note that for Lists we use square brackets, but for Dictionaries we use curly braces.**

Now open a python REPL and create a few  Dictionaries of your own. You'll inevitably make a mistake at some point and  python will show you an error message. Try to understand it – new error messages can be learning opportunities!

After you've created a few  Dictionaries, try using something other than a String for the keys. What works? What doesn't work?


## Part Two: Reading Individual Values

Once you have a dictionary, you can read an individual _value_ using its _key_.

``` python
>>> # first create and assign the person dictionary, as above, then...
>>> person['name']
"Guido van Rossum"
>>> person['nationality']
'Dutch'
```

Do this a few times to get some practice.

## Part Three: Adding Key-Value Pairs

If you already have a dictionary and wish to add new key-value pairs, you can do so using the `[]` method.

``` python
>>> # first create and assign the person dictionary, as above, then...
>>> # add a key-value pair
>>> person["birthday"] = "31 January"
>>> # add another key-value pair
>>> person["favourite_colour"] = "Purple"
>>> # observe that the dictionary has changed
>>> person
{"name":"Guido van Rossum", "nationality":"Dutch", "favorite_programming_language":" python", "birthday":"31 January", "favourite_colour":"Purple}
```

Now you do the same! Create a new dictionary and add some key-value pairs as shown above. Better still, do that a few times so that you start to build some familiarity with the `[]` method.

## Part Four: More Dictionary Methods

In section 2 we learned about `list` methods, which are methods that you can call on any `list`.  We also saw how you can find new list methods using the  python docs.

In this section, you'll learn some `Dictionary` methods which, unsurprisingly, you can call on any `Dictionary` and, of course, you can find new `Dictionary` methods using the  python docs.  For Python version 3.10.6, you'll find them [here](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).  If you're using another version, go to the same link and then edit the URL to reflect the version you're using.

Recall the requirement below...

> Allow you to see a list of all the services for which a password has been stored

To meet this requirement, we'll need a method that returns all the dictionary keys.

If you feel like a challenge, try to find the method that returns all the `Dictionary` keys as a `List`, using the  python docs (or google).  The solution is below.

<details>
  <summary>Solution</summary>
  <img src="./images/dictionary_keys.png"></img>
</details>
<br>

Now get some practice with that method and the ones listed below, some of which will require an argument – use the python docs to find out more.

- `values()`
- `get()`
- `items()`
- `pop()`
- `pop_item()`
- `clear()`
- `shiftset_default('takes an arg!')`

## Reflect and Review

In this section, you learned about how to create and manipulate  Dictionaries.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain, in writing or to a peer:
- What a Dictionary is
- How to create a Dictionary
- How to add key-value pairs to a Dictionary
- How to retrieve a value from a Dictionary
- How to retrieve all the keys from a Dictionary
- The use of one other dictionary method that you experimented with


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=03_introducing_dictionaries.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F04_introducing_classes.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
