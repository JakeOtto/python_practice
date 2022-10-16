# IRB: Interactive Ruby

The irb is a Ruby [REPL (read-evaluate-print loop)](http://en.wikipedia.org/wiki/Read–eval–print_loop) because it waits for you to enter a Ruby expression, reads it, evaluates it and prints the result of the evaluation back to the terminal. So, if we put `2 + 2` into irb, it will evaluate it using Ruby and show the result: 4.

````ruby
> 2 + 2
=> 4
````

## Getting Started

With your terminal open, type the following command:

````
irb
````

This will open up the interactive ruby console and you should see a prompt like this: ">". With irb, you can type ruby code that is instantly run in your terminal.

## Experimenting in IRB

IRB is very useful for playing with Ruby. Whenever you think "Hey, what would this code do?", try it in irb and see if it does what you think it should do. Sometimes you'll be surprised. For example, what will this code do?

````ruby
5 / 2
````

You may expect that it will evaluate to 2.5 but you'll be wrong.

````ruby
> 5 / 2
=> 2
````

This is not a mistake, it's a peculiarity of the Ruby language. We'll discuss why it evaluates to 2 instead of 2.5 shortly.

Don't assume that irb is only good for relatively simple snippets of code. You can put something really sophisticated into irb as well (and you will, as you learn more about Ruby).

In particular, you can enter blocks of code that span multiple lines. If a line cannot be evaluated because you haven't finished entering it yet, irb will wait for you to continue on the next line. Try hitting 'enter' after the plus sign, for example.

````ruby
> 2 +
> 2
=> 4
````

Since you pressed enter after the plus sign (line 3), it's obvious to Ruby that you haven't finished entering the expression to evaluate, so it will wait until you finish it on the line 4 and only then print the result ("4").

This also happens if you enter text into irb. A piece of text is called a "string" in Ruby (because it's a "string" of characters) and must be enclosed in quotes. If we enter a string into irb, it is just returned back to us.

````ruby
> "Hello, Makers!"
=> "Hello, Makers!"
````

If, however, we forget to close the string by omitting the double quote, irb will wait until you enter it because it will assume you're still entering the string. This is a very common source of confusion among beginners because it will look like the irb isn't responding. This is what's happening here:

````ruby
:001> 2 + 2
=> 4
:002 > "Hello, Makers
:002"> I forgot to close the quote
:002"> so even if I press 'enter', it doesn't do anything
:002"> 2+2
:002"> it doesn't print '4', because we're still typing
:002"> the string that began with 'Hello, Makers'
:002"> Ok, let's stop this nonsense and close the quote"
=> "Hello, Makers\nI forgot to close the quote\nso even if I press 'enter', it doesn't do anything\n2+2\nit doesn't print '4', because we're still typing\nthe string that began with 'Hello, Makers'\nOk, let's stop this nonsense and close the quote"
````

Note that lines 7 to 12 (when the string was still not "closed"), there was a quote character before the prompt (:002">) instead of a space (:001 >). This was an indication that irb is waiting for the closing quote.

When you want to quit irb, just type `exit`.

Advanced IRB
------------

You can control what happens when you start irb using a `.irbrc` file placed in your home directory, e.g.

```ruby
Dir['./lib/*.rb'].each { |f| require f }
```

will autoload ruby files from your lib directory


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Firb.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Firb.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Firb.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Firb.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Firb.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
