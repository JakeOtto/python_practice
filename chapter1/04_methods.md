# Methods

In the previous section, you learned that Python comes with a range of useful built in functions and that you can define your own functions to avoid repetition. In this section, you'll learn about methods

Methods are functions that _belong_ to, and _are called on_, specific objects like strings or integers.

## Video

Here's the [video](<!-- OMITTED -->) for this section.

## Learning Objectives

In this section, you will learn:
- What methods are
- How to use methods
- Where to find information about Python methods
- How methods are different to functions

## Part One: What is a Method?
Methods are a _lot_ like functions except they belong to a specific things (the technical term being objects), such as strings or integers and they're executed using dot syntax and parentheses, like this.

```python
>>> word = "Python"
>>> word.upper()
'PYTHON'
```

Above, we called the `upper` method on the string `"Python"` which returned `'PYTHON'`. Note the dot `.` between `word` and `upper`.


Here's another example using `lower` on the string `"PYTHON"`.

```python
>>> word = "PYTHON"
>>> word.lower()
'python'

```

Side note: the original string is not changed by `lower`

```
>>> word = "PYTHON"
>>> word.lower()
'python'
>>> word
"PYTHON"
```

### Now Try This

* Does `upper` change the original string or does it work like `lower`?

* What happens when call `upper()` without it's parenthesis?
``` python
>>> 'welcome to python'.upper
>>> # ???
```

## Part Two: String Methods

In Python there are a lot of string methods but, don't worry, you won't have to learn all of them! In fact, you're only likely to remember a handful and, for the rest, you'll use the Python docs (which you'll see very soon).

### Time to Play in the Python REPL

Hopefully, you're already in the Python REPL and have followed along with the above. If not, open it up now and try the `string` methods below by calling each one on a `string` of your choosing. For example

```python
>>> " my Nanna was called Brenda and baked delicious bread! ".capitalize()
```

What do they do? As you play with these methods, try creating some variables to hold the return values and then see what happens when you call a method on a variable. One of them is not a real method, so you'll get an error message – be ready to find the useful information in it.

- `capitalize`
- `lower`
- `isascii`
- `invert`
- `isalpha`
- `title`
- `strip`

## Part Three: Method Chaining

If you wanted to use both `strip` and `upper` to transform `"  hello "` into `"HELLO"`, you could do this in two steps, using a variable (called `stripped_greeting`) to hold the intermediate result.

```python
>>> greeting = "  hello "
>>> stripped_greeting = greeting.strip()
>>> stripped_greeting.upper()
'HELLO'
```

You can also do this in one line, using method chaining.

```python
>>> greeting = "  hello "
>>> greeting.strip().upper()
'HELLO'
```

This works, because `strip` returns `"hello"`, which means we then call `upper` on that new `string` to get the final return value of `"HELLO"`.

### Exercise

Here are four lines of code. Note down what you think each one will do. When you have noted down all four answers, run them in IRB to find out.

```python
# Don't run these until you've said what you think will happen

# Example 1
>>> len("hello")

# Example 2
>>> 5.lower()

# Example 3
>>> "heLLo ".lower().strip()

# Example 4
>>> len("hello").upper()
```

<details>
  <summary>I don't understand why Python works that way (Click here for an explanation)</summary>
  <h4>Example 1</h4>
  <div><code>len("hello")</code> returns <code>5</code> - an integer representing the number of characters in <code>"hello"</code>.</div>
  <h4>Example 2</h4>
  <div><code>5.lower()</code> throws an error because <code>lower</code> is a string method and cannot be used on an integer.</div>
  <h4>Example 3</h4>
  <div><code>"heLLo ".lower().strip()</code> returns "hello" because <code>"heLLo ".lower()</code> returns the String <code>"hello "</code> on which we then call <code>strip</code> to remove spaces at the start and end.</div>
  <h4>Example 4</h4>
  <div><code>len("hello").upper()</code> throws an error because <code>len("hello")</code> returns 5 on which we then call <code>upper</code>, a method that can only be called on strings.</div>
</details>

### Exercises 2

Say out loud what value will be returned to the terminal before running each example:

``` python
# Example 1
>>> hobby = "bouldering"
>>> hobby[-1]
# ???

# Example 2
>>> hamlet = "To be, or not to be!"
>>> hamlet[-1]
# ???

# Example 3
>>> macbeth = "Tomorrow, tomorrow and tomorrow, creeps in this petty pace from day to day to the last syllable of recorded time."
>>> macbeth[0:8]
# ???
>>> 

# Example 4
>>> romeo = "What light through yonder window breaks?"
>>> romeo[-14:-1].upper()
# ???
```

## Part Five: the Python Docs

The Python docs catalogue all the methods which are contained within the Python standard library. So, for example, you can find [all the `String`-specific methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).

Python strings actually belong to a family of data types called `sequences`. This means that for some string features you'll need to look at the [sequence docs](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

In each case, there's an explanation of what the method does and, if you're lucky, a clear example of the method in action – [`strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) is a good example of that.

> In section one you found a list of some other Python data types. Find the Python docs page for one of those now.

## Reflect and Review

In this section, you learned about String methods and method chaining.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

- What methods are
- How to use `String` methods
- How method chaining works
- Where to learn about Python's string methods


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=04_methods.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F05_further_string_manipulation.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
