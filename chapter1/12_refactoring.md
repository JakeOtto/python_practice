# Refactoring

Right after all your tests go green, you should pause for a moment to consider how you got there and whether you could change your code to make it better in some way – this is the art of refactoring.

Whilst refactoring, we don't add any new features (such as new rules about what makes a valid password) but we might add new methods. Through refactoring, we try to end up with code that is:

- Correct, meaning that your tests still pass
- Clear, so that its easy to read
- Concise, with little or no repetition

The ultimate goal is to generate code that is easy to change because, if you can be sure of one thing in programming, it's that changes will be necessary! It might be that your client changes their mind, there was a misunderstanding, a new user need is discovered or maybe the application just continues to grow as planned. All of these scenarios involve changing, or building upon, the code that you already have.

## Video

Here's the [video](<!-- OMITTED -->)for this section.

## Learning Objectives

In this section, you will learn
- What _refactoring_ is
- When to refactor
- The benefits of refactoring
- A potential refactor of a password validator solution

## Part One: A Potential Solution

Some of you will have created something a lot like this, for your password validator.

```python
def valid(password):
  if len(password) < 8:
    return False
  elif "!" in password:
    return True
  elif "@" in password:
    return True
  elif "$" in password:
    return True
  elif "%" in password:
    return True
  elif "&" in password:
    return True
  else:
    return False
```

If so, bravo! You solved the problem perfectly well and now it's time to refactor. If you ended up with something else, please share your solution in Slack so that others, including your coach, can see it :)

# Part Two: Refactor

We're now going to do three things that will make this code a little easier to work with.

1. We'll create a new method that checks the length of the password
2. We'll create a new method that looks for the special characters
3. We'll use those two methods in our `if` statement

Along the way, we'll encounter a new thing: calling methods from inside other methods.

The first method will look like this and it will return either `True`, when the password is longer than 7 characters, or false, when it is shorter.

```python
def sufficient_length(password):
  # len(password) > 7 will evaluate to True or False
  return len(password) > 7
```

The second method will look like this. It will return either `True` or `False` depending on whether the password contains the special characters.

```python
def special_chars_included(password):
  if "!" in password:
    return True
  elif "@" in password:
    return True
  elif "$" in password:
    return True
  elif "%" in password:
    return True
  elif "&" in password:
    return True
  else:
    return False
```

And our `valid()` method would look like this.

```python
def valid(password):
  if sufficient_length(password) and special_chars_included(password):
    return True
  else:
    return False
```

I think it's an improvement because our rules are now contained within methods which have descriptive names. Also, now that the codebase is broken down into small pieces, we can combine them in novel ways to create new behaviour. For example, if we wanted to add a new `valid_weak` method that only checked for special characters, we could do that very easily.

```python
def valid_weak(password):
  if special_chars_included(password):
    return True
  else:
    return False
```

## Reflect and Review

In this section, we introduced the practice of refactoring. From now on, we'll expect you to refactor your code, as you go along, with a strong focus on readability and ease of change.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

- What refactoring is
- When you should use it
- The benefit of refactoring
- Which of the two above password validator solutions you prefer


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=12_refactoring.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F13_review_learning.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
