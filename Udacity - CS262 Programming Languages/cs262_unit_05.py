# -------------------- CS262 week 5 --------------------
"""
Lexing and parsing deal with the form of an utterance. We now turn our attention to the meaning of an utterance -- we turn our attention to semantics.

A well-formed sentence in a natural language can be "meaningless" or "hard to interpret". Similarly, a syntactically valid program can lead to a run-time error if you try to apply the wrong sort of operation to the wrong sort of thing (e.g., 3 + "hello").

For more information:

    "Colorless green ideas sleep furiously" is a syntactically-valid sentence constructed by linguist and philosopher Noam Chomsky to show that an utterance can be well-formed but have no clear meaning. Thus, syntax and semantics are not the same thing. 
"""

"""
One goal of semantic analysis is to notice and rule out bad programs (i.e., programs that will apply the wrong sort of operation to the wrong sort of object). This is often called "type checking". 
"""

"""
"A type" is a set of similar objects (e.g., number or string or list) with an associated set of valid operations (e.g., addition or length). 
"""

#We can interpret a parse tree by walking down it — traversing it — in a particular order. 

"""
Students wishing to run their browser locally can use the "graphics.py" file used in the course. Please note that generating images successfully requires "pdfTeX", "ImageMagick", and "Ghostscript".
"""

"""
We will write a recursive procedure to interpret JavaScript arithmetic expressions. The procedure will walk over the parse tree of the expression. This is sometimes called "evaluation". 
"""

"""
We need to know the values of variables — the context — to evaluate an expression. The meaning of x+2 depends on the meaning of "x". 
"""

"""
The "state" of a program execution is a mapping from variable names to values. Evaluating an expression requires us to know the current state. 
"""

"""
Python and JavaScript have conditional statements like if — we say that such statements can change "the flow of control" through the program.

Program elements that can change the flow of control, such as if or while or return, are often called "statements". Typically statements contain expressions but not the other way around. 
"""

"""
In languages like Python or JavaScript, functions can be "values" (i.e., evaluating an expression can result in a function). As a result, we must decide how to represent function values. We'll use tuples that include the function body, parameter names, and the relevant environment. 
"""

"""
While most computer languages are equivalent (in that any computation that can be done in one can also be done in another), it is debated whether the same is true for natural languages. 
"""

"""
If tsif halts, then it loops forever. If tsif loops forever, then it halts. Both cases lead to a contradiction. Therefore, halts() cannot exist.

For more information:

    "This sentence is false" is a form of Epimenides paradox of self reference.
    The Barber Paradox is similar. 
"""