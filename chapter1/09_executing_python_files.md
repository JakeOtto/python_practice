<!-- OMITTED -->

This can get a little confusing at the beginning, so there are some helpful
extensions in VSCode to aid us, such as
[indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
which colourises the columns of our code.

# Executing Python Files

The best approach to building programs is to build iteratively. You start by writing something very small and very simple, then you tweak or add to it, executing the code after every small change so that you can get feedback, perhaps in the form of error messages, from your computer.  If you have to write your program in it's entirety every time, you're going to get annoyed very quickly and revert to some less than ideal practices. Plus, you'll soon want to build programs over days, months or years.

So we need to be able to write code in files and execute it from those files. Let's give that a try now.

## Video

Here's the (<!-- OMITTED -->)[video](https://youtu.be/XtreBh7TcyQ) for this section.

## Learning Objectives

In this section, you'll learn:
- How to execute Python code that is saved in a `.py` file

Open Terminal or iTerm and `cd` into your home directory (you can use `~` as shortcut)

```shell
; cd ~
```

Then create a file called `hello_world.py`.

```shell
; touch hello_world.py
```

The file will be inside your home directory – open it up in your text editor, add the following Python code and save the file using `command + s`.

**Below, `print()` is used to print `"Hello world!` to the terminal. We need it here because simply doing `"Hello, World!"` wouldn't result in anything that we can see from the terminal (do try it). You'll find further guidance on when to use `print()` at the end of this section.**

``` python
# in hello_world.py – lines that start with # are comments (you don't need to type them out)
print("Hello World!")
```

Now you can execute the code in that file like this

```shell
; python3 hello_world.py
```

You should see `"Hello, World!` printed to the terminal. If so, mission accomplished. The `python3` command invokes the Python _interpreter_, which is the program that runs your Python code.

> If you see an error message that contains `No such file or directory`, you're probably in the wrong directory in your terminal.

Now use this as a chance to practice some of the things we've covered previously. Be sure to `print()` anything that you would like to see printed to the terminal.

- Create a few more files using `touch`. You might want to create a series of files that contain some notes for yourself. Why not create your own cheat sheet -
    ``` shell
    ; touch cheatsheet.py
    ```
     - Then you may want to write notes as comments about some of the String methods you encountered in earlier sections.
     ``` python
     >>> hamlet_four = "Oh what a rogue and peasant slave am I..."
     >>> print(hamlet_four.upper()) # Here we can see Hamlet's soliloquy being shouted!
     >>> # Perhaps you'd like to ananlyse the individual words:
     >>> hamlet_split = hamlet_four.split(" ")
     >>> for word in hamlet_split:
     ...     print(word)
     >>> # ???
     ```

- Add some more examples of string methods to your file. Remember to add `print()` statements to see the result in the terminal.
- Execute the code using `python3 cheatsheet.py` if, for example, your file is called `cheatsheet.py`
- Or if you'd like to interact with it, `python3 -i cheatsheet.py` to load it into a REPL.

## When do I use `print()`?

Let's imagine the following code:

``` python
>>> word = "python"
>>> uppercase_word = word.upper()
>>> f"{word} upcased is #{uppercase_word}"
```

Should we want to open a REPL to explore some more: 

``` shell
; python 3
```

If we run this in the Python REPL here's what we get:

``` python
>>> word = "python"
>>> word
'python'
>>> uppercase_word = word.upper()
>>> uppercase_word
'PYTHON'
>>> f"{word} upcased is {uppercase_word}"
'python upcased is PYTHON'
>>> 
```

That's nice for us. We get to see all the results in the middle so we can check they are correct. This is very useful and it is what the python REPL is designed for. But users don't want to see all of those results in the middle. They just want the final results! So when we're running Python in a file (like `hello_world.py`) Python keeps all the return values to itself and doesn't show them to the user. To show something to the user, we have to say so explicitly. This is what `print` does. It sends the information to the terminal so the user can see it.

We could do something like this, in a file called `upcase_python.py`

``` python
 # File: upcase_python.py
word = "python"
uppercase_word = word.upper()
print(f"{word} upcased is {uppercase_word}")
```

And then execute the code...

```shell
; python3 upcase_python.py
```

To see this in the terminal...

```shell
python upcased is PYTHON
```

Another way to open a Python file is to use the `-i` flag. The `-i` stands for interactive, and will load the file (and the code objects inside) directly into a REPL for you to interact with.

Try it with your `upcase_python.py` file by running:

``` shell
; python3 -i upcase_python.py
```

### Printing Aside...

It is worth noting that while printing information to the terminal is absolutely invaluable, it is predominantly a debugging tool, and not used at production level Software Development for the access to our program. 

Throughout the next few modules, we will be using `print()` a lot to investigate and interrogate our programs and the information we are manipulating inside them. However, do bear in mind as we move forward through the course that in modern applications, Graphical User Interfaces, Web Applications and the like are the norm for interfacing with our programs.


To signal that we're showing something to the user and rather than storing a value for later use, `print()` doesn't return anything. To demonstrate this, we can have a sneak preview of making a function. Look:

``` python
>>> def greeter():
...     print("Hi there!")
... 
>>> greeter()
Hi there!
>>> print(greeter())
Hi there!
None 

```

When we send the value of the `greeter()` function to the terminal with `print()` we get two values back, the first is the String we ask the function to print `"Hi There"`, and the second which is `None` - this tells us the function is more than able to execute the code we want it to, namely sending our greeting to the terminal, but it has no return value.

This will become important when we move onto Functions & Methods, as we need to specify whether or not a Function or Method `return`s a value.

Here's a rule of thumb:
1. Is this something you want to show the user right now with no further
processing? If so, use `print()`.
2. Is this something the program will need to do some further work with before it's ready for the user? If so, don't use `print()`.

## Reflect and Review

In this section, you learned a second way of executing Python code – this time from a file.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
- How to execute Python code that is written in a file
- What happens when you try to execute code from a file that doesn't exist
- The pros and cons of this new approach to code execution

## Try some extra exercises

Put your understanding to the test!

1. What happens if you change the first `greeting` to something else? Say for example, `potato`?

    ```Python
    >>> potato = print("Hello")
    Hello
    >>> greeting
    # ???
    >>> 
    ```

2. What happens if you change the second `greeting` to something else? Say for example, `bamboo`?

    ``` python
    >>> potato = print("Hello")
    Hello
    >>> for letter in bamboo:
    >>>     print(letter)
    #???
    ```
3. Take a look at the command you need to run your code:

    ```shell
    ; python upcase_python.py
    ```

    If you were to guess at one part of that line being the _parameter_, which would it be?
    

[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=09_executing_python_files.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F10_defining_functions.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
