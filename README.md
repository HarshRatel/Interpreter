https://ruslanspivak.com/lsbasi-part1/

PART 1

    *DONE* Modify the code to allow multiple-digit integers in the input, for example “12+3”

    *DONE* Add a method that skips whitespace characters so that your calculator can handle inputs with whitespace characters like ” 12 + 3”

    *DONE* Modify the code and instead of ‘+’ handle ‘-‘ to evaluate subtractions like “7-5”

PART 2

    *DONE* Extend the calculator to handle multiplication of two integers

    *DONE* Extend the calculator to handle division of two integers

    *DONE* Modify the code to interpret expressions containing an arbitrary number of additions and subtractions, for example “9 - 5 + 3 + 11”

PART 3

    *DONE* Draw a syntax diagram for arithmetic expressions that contain only multiplication and division, for example “7 * 4 / 2 * 3”. Seriously, just grab a pen or a pencil and try to draw one.
    
    *DONE* Modify the source code of the calculator to interpret arithmetic expressions that contain only multiplication and division, for example “7 * 4 / 2 * 3”.

    *DONE* Write an interpreter that handles arithmetic expressions like “7 - 3 + 2 - 1” from scratch. Use any programming language you’re comfortable with and write it off the top of your head without looking at the examples. When you do that, think about components involved: a lexer that takes an input and converts it into a stream of tokens, a parser that feeds off the stream of the tokens provided by the lexer and tries to recognize a structure in that stream, and an interpreter that generates results after the parser has successfully parsed (recognized) a valid arithmetic expression. String those pieces together. Spend some time translating the knowledge you’ve acquired into a working interpreter for arithmetic expressions.

PART 4

    *DONE* Write a grammar that describes arithmetic expressions containing any number of +, -, *, or / operators. With the grammar you should be able to derive expressions like “2 + 7 * 4”, “7 - 8 / 4”, “14 + 2 * 3 - 6 / 2”, and so on.

    *DONE* Using the grammar, write an interpreter that can evaluate arithmetic expressions containing any number of +, -, *, or / operators. Your interpreter should be able to handle expressions like “2 + 7 * 4”, “7 - 8 / 4”, “14 + 2 * 3 - 6 / 2”, and so on.
    If you’ve finished the above exercises, relax and enjoy :)

http://www.jayconrod.com/posts/39/