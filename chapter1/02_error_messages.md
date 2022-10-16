# Error Messages Are Your Friends

We ended the previous section on a cliffhanger, trying to decipher the meaning of an error message. In this short section, you'll see how to break it down and extract useful information.

## Video

Here's the [video](<!-- OMITTED -->) for this section.
## Learning Objectives

By the end of this section, you'll be able to:

- Find the useful bits of information in a basic error message
- Welcome error messages as helpful feedback :)

## Dissecting Your First Error Message

You probably got something a lot like this at the end of the last section. Did you figure out what it means?

```python
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> 
```

Because we didn't use quotation marks, Python doesn't recognise `hello` as a `string`. Instead, `hello` is interpreted as the name of a variable, or method, or something Python should know about (more about those later) which has not yet been defined. I.e. Python doesn't know what that `hello` thing is, only that it's not a string!

Let's break this error message down. We'll ignore the first line for now and move on to the second line, which is _trying_ to tell us where the error is:

```python
  File "<stdin>", line 1, in <module>
```

Right now, none of that is going to make any sense. That's ok - when we get to putting Python code in files this bit is going to get a lot more useful.

The last line tells us what the error is:

```python
NameError: name 'hello' is not defined
```

In plain English, Python is referring to `hello` as a `name` because, without the quotation marks, it looks like the name of a variable and we're being told that there is nothing with that name.

> Try it out: if we do the same thing, but say goodbye instead, what changes?

## Another Error

Now do this to generate one more error message and try to figure out what it is telling you.

```python
> 1 + "a"
```
## Reflect and Review

In this section, we picked apart an error message to find the useful information. Hopefully, you'll welcome the next one you see as a helpful old friend :)

**Please pause at this point to reflect and review your learning...**

- How much of each error message was actually useful to you?
- Can you resolve to say "That's interesting!" next time you see an error message?


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=02_error_messages.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F03_functions.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
