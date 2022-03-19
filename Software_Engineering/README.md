[Write Better Python Functions - Jeff Knupp](https://medium.com/hackernoon/write-better-python-functions-c3a9a36382a6) these are language agnostic guidelines
  
**Language Fatures**:
  * Python: 
    * [list comprehension](https://www.youtube.com/watch?v=belS2Ek4-ow)
    * [Using Python's Type Annotations](https://dev.to/dstarner/using-pythons-type-annotations-4cfe)
    * [Data Classes in Python 3.7+ (Guide)](https://realpython.com/python-data-classes/)
          
Readibility:
  * [How do you write readable code?: 13 Principles - Peter Hurford](https://gist.github.com/peterhurford/3ad9f48071bd2665a8af)
  * Use a style guide:
    * Python:
      * [How to write Python code with PEP8 - realpython](https://realpython.com/python-pep8/)
    * R:
      * [tidyverse](https://style.tidyverse.org/)
  * Method Chaining
    * Allows operations to be read from left to right like you would read a book rather than inside to outside
    * Python
      * [The Unreasonable Effectiveness of Method Chaining in Pandas](https://towardsdatascience.com/the-unreasonable-effectiveness-of-method-chaining-in-pandas-15c2109e3c69)
      * [Tom Augspurger method chaining](https://tomaugspurger.github.io/method-chaining)
    * R
      * [pipes](https://r4ds.had.co.nz/pipes.html)

Debugging:
  * Python:
    * [How to read Python Stack Traces Video](https://www.youtube.com/watch?v=3p3p6kp39to)
    * [Reading Python tracebacks video](https://www.youtube.com/watch?v=g9O9j34Vxww)
      * Start from bottom up : )     
    * [Understanding the Python Traceback](https://realpython.com/python-traceback/)
  * R:

Perfomance:
  * Python:
    * [Array programming with NumPy](https://www.nature.com/articles/s41586-020-2649-2)
    * [Examining runtime with timeit - DataCamp](https://campus.datacamp.com/courses/writing-efficient-python-code/timing-and-profiling-code?ex=1)

Commandline & Bash
  * [List of Command-Line Tools](https://datascienceatthecommandline.com/2e/list-of-command-line-tools.html) from [Data Science at the Command Line](https://datascienceatthecommandline.com/2e/chapter-1-introduction.html) by Jeroen Janssens
  * [The Art of Command Line - Josh Levy](https://github.com/jlevy/the-art-of-command-line#basics)

Tools:
  * Notebooks:
    * Using Colab in R
      * Shorthand: `colab.to/r`. Longer: `link://colab.research.google.com/notebook#create=true&language=r` . [Stack Overflow](https://stackoverflow.com/questions/54595285/how-to-use-r-with-google-colaboratory). 
      * Or `%load_ext rpy2.ipython` and use `%%R` for R cells
    * [Playing Videos on Google Colab](https://stackoverflow.com/questions/52050860/playing-videos-on-google-colab) 
      * `from IPython.display import YouTubeVideo; YouTubeVideo('-ncJV0tMAjE')` <- After the `watch?v=` 
