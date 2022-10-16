# Further String Manipulation

_String manipulation_ means to _change a string_ which, so far, we've achieved in four ways.

1. Concatenation
2. Interpolation
3. Built in functions
4. String methods

In this section, you'll learn about two more ways of manipulating strings: slicing and indexing.

## Indexing

To access an individual character in any given string, you can use its index (position) and the square brackets, `[]`.

Here's an example of how to get the first character in `banana pancakes`.

``` python
>>> food = "banana pancakes"
>>> food[0]
'b'
```

**Shouldn't that be `food[1]`??**

Python, as with many programming languages, indexes strings (and other sequences) starting at 0. We call this `Zero Indexing`.

If we called `len()` on our food string, we'd see there are 15 characters including the space but, indexing from zero, this is what their indices look like.

``` 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
b a n a n a   p a n c  a  k  e  s
```

So if we want to just print the `p` of `pancakes`, we count up from 0 to that position - index 7:

``` python
>>> food = 'banana pancakes'
>>> food
'banana pancakes'
>>> food[7]
'p'
```

If `0` is the first position in the sequence, what happens when we use `-1` or `-2` or even `-5`?

``` python
>>> word = "Flux"
>>> word[-1]
'x'
>>> word = "Eviscerate"
>>> word[-2]
't'
>>> question = "How do you do?"
>>> question[-5]
'u'
```

## Slice Notation

What if you want to access more than one character? That's where slice notation comes in. Using slice notation you can slice out part of a string.

Confusingly, perhaps, slice notation also uses square brackets but instead of providing just one number, we provide two: the _start-index_, the _stop-index_.

Let's see this in action with our delicious `"banana pancakes"` example!

``` 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
b a n a n a   p a n c  a  k  e  s
```

If we just want `"banana"` we can use the _start-index_ value of `0` and the _stop-index_ value of 6:

``` python 
>>> food = 'banana pancakes'
>>> food[0:6]
'banana' 
```

**Did you expect that to return `'banana '`, with a space on the end?**

Here's another index related trap - the _stop-index_ is not inclusive. I.e. The slice ends before the _stop-index_.

### Exercise

* How would you slice out `pancakes`?

<details>
  <summary>Reveal the answer</summary>
  <code>>>> food[1:15]</code>
</details>

### Further examples

``` python
>>> sentence = "Where in the world did I leave my keys?"
>>> sentence[0:10]
'Where in t'
>>> sentence[0:12]
'Where in the'
>>> sentence[5:18]
' in the world'
```

These tools are really useful for strings but really become powerful when you learn how to use them with other datatypes.

Have a play around with square bracket slice notation in the Python REPL. What happens when you omit either a _start, stop_ value?

## Reflect and Review

In this section, you learned how to access individual characters and slices of a string.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

- What is meant by zero-indexing
- How to access the first character in a string
- How to access the second character in a string
- How to access the last character in a string
- How to slice several characters from a string


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=05_further_string_manipulation.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F06_beyond_strings.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F05_further_string_manipulation.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F05_further_string_manipulation.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F05_further_string_manipulation.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F05_further_string_manipulation.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F05_further_string_manipulation.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
