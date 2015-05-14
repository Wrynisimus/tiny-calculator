# tiny-calculator
This is a calculator that is really small and that should make; multiplying, dividing, squaring, adding, and subtracting easier from a terminal emulator.

The only dependency that you should need is an up to date version of python, (python 2.7+), and that's it!!

To make execution of this calculator I recommend that you write a shell script to /usr/bin named something like "calculator", then instead of typing "python3 /home/USERNAME/tiny-calculator/calculator.py" you just type calculator.

To do this you can write; 
    #!/bin/bash 
    cd /PATH/TO/CACLULATOR 
    python3 ./calculator.py 
and thats it!!

I may add more features as more time progresses throughout the year, but for now I hope it helps you be more productive in a terminal.

Adding and subtracting supports 3 numbers while the other options support two, so to add 2 numbers with the addition command it would look like;
    Enter your first number: 100 
    Enter your second number: 100 
    Enter your third number: 0 
    Your result is... 100 + 100 + 0 = 200

I may add more features as more time progresses throughout the year, but for now I hope it helps you be more productive in a terminal.
