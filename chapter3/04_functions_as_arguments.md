# Functions as Arguments

In chapter 1, you learned that functions are like little machines that take inputs (arguments) and give back some outputs (return values). In this section, you'll see that the arguments can be other functions 🤯.

## Video

Here's the [video](<!-- OMITTED -->

```python
>>> def tenPercentTaxRate(grossPay):
...   return grossPay * 0.9
>>>
>>> def twentyPercentTaxRate(grossPay):
...   return grossPay * 0.8
>>>
>>> def fourtyPercentTaxRate(grossPay):
...   return grossPay * 0.8
>>>
>>> def payslip(grossPay, taxfunction):
...   # the second arg is a function
...   # to execute it, just add parentheses
...   # and the required argument
...   netPay = taxfunction(grossPay)
...   return "Your net salary this month was " + str(netPay)
>>>
```

Now we can combine the tax rate functions with payslip functions.

```
>>> payslip(100, tenPercentTaxRate)
90
>>> payslip(100, twentyPercentTaxRate)
80
>>> payslip(100, fourtyPercentTaxRate)
60
```

**You're strongly encouraged to try the above in your Python REPL :)**

## Part Four: Exercise II

### Weather Report
* Declare a function called `weatherReport` that takes a temperature and a function as its two arguments
* Declare two other functions, each of which takes a temperature as an argument
  - One is called `sunLover` and it returns 'great' if the temp is 25 Celsius, or above. Otherwise it returns 'not great'
  - One is called `snowLover` and it returns 'great' if the temp is 0, or below. Otherwise it returns 'not great'
* Combine the functions to generate customised weather reports

#### Expected Behaviour

```python
>>>  weatherReport(24, sunLover)
'not great'
>>>  weatherReport(25, sunLover)
'great'
>>>  weatherReport(1, snowLover)
'not great'
>>>  weatherReport(0, snowLover)
'not great'
```

## Looking Ahead

In the next two sections, you'll learn how to do interesting things to lists and dictionaries, using methods that take functions as arguments.

## Reflect and Review

In this section, you learned that functions can be used as arguments.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

- How to assign a function to a variable
- How to pass a function as an argument
- How to define a function that takes a function as an argument


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=04_functions_as_arguments.md&repository=makersacademy%2Fpython_foundations&redirect=chapter3%2F05_advanced_lists.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
