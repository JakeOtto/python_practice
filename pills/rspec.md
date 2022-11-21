# rspec: Ruby Specifications

RSpec is a tool used to write tests that ensure your program does what it needs to do. RSpec stands for "Ruby Specification". The RSpec tool lets you write down specifications for you program in a ruby file.

## Test Driven Development: using `RSpec` tests to write code

When you've had some experience you'll be able to write your own tests but, to begin with, you'll use the tests that we wrote for you.

Your goal is to make all the tests pass. And you can achieve this just by running `rspec` in the terminal, reading the error message you get and improving your code.

You might have another way of doing it. For instance: in the drills to chapter one, you are given the specifications of the code in the comments of the ruby file.

```Ruby
# TASK: define a method that returns a string that is the same as a given string, but converted to upper-case characters.
# EXAMPLE INPUT/OUTPUT:
# when the string is 'hello world'
# the method should return 'HELLO WORLD'
def block_caps_a_string(string)
  # your code goes here
end
```

But, if you were to rely only on this, then a human being would have to read it and manually check input and output for the method (maybe with a puts command). This would be very time consuming. And this test might have to be repeated if the codebase changed.

We can automate the tests by using `rspec`. When we run the tests, a human being only needs to read the code when some of the tests fail.

I will try this out with a file that contains:

```ruby
# File: lib/mystery_method.rb

# run the tests by typing rspec in the terminal
# pass the tests by writing a method
```

It would be nice to have the specifications written in the comments, but I can manage in this extreme case because the tests will give me those specifications.

The process I will use is to repeatedly run `rspec` in the terminal. At first: there will be an error (the so-called 'red' phase). For instance:

```diff
- NoMethodError:
-      undefined method `greet'
```

From this error, I will be able to figure out what to do: define a method called `greet`. (The first error actually gives more detail about what is wrong with the program. But there is no need to get everything worked out after the first test).

After several iterations of this process (run `rspec`, modify the code), I eventually end up with all tests passing (the so-called 'green' phase).

```diff
Finished in 0.01215 seconds (files took 0.41292 seconds to load)
+ 4 examples, 0 failures
```

Work done. I now have code that meets the specifications. You can watch me do the whole thing in a [video](https://www.youtube.com/watch?v=rC6thOxM2BM).

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Frspec.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Frspec.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Frspec.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Frspec.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Frspec.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
