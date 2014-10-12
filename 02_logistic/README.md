tonight we will be combining two of your favorite topics...beer and logistic regression

here are some interactive data exploration cmds to run on the beer dataset
before we get down to modeling

(some notation: $ denotes a unix command, >>> denotes a python command)

the beer dataset we'll use lives here:  
http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt

first of all let's pull the data down locally & have a look

    $ wget http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt
    $ head beer.txt
    $ wc -l beer.txt
    $ less beer.txt

notice that the data appears to be tab-delimited (Q: how could you verify this?)

now let's fire up python...the first thing to do is to import the beer dataset
into python as a (pandas) dataframe

    >>> import pandas as pd
    >>> beer = pd.read_csv(input_url, sep='\t')

now have a look around

    >>> beer.head()
    >>> beer.tail()
    >>> len(beer)
    >>> beer = beer.dropna()    # drop recs w/ missing fields (not in place)
    >>> len(beer)
    >>> beer.describe()
    >>> beer.dtypes
    >>> beer.columns    # shows col labels
    >>> beer.index      # shows row labels

now here's our modeling problem:

    we want to build a model that will predict whether a beer is "good"

this problem statment is okay for a start, but it leaves us with the following questions:

    1. what does "good" mean?
    2. how can we use this data to build a model?
    3. how will we know if we're successful?

answering question 1 is equivalent to making our problem more well-defined
(NOTE this is the most important step! why?)

let's take a look at the data again...there are two columns (`Rank` & `WR`, which
is a rating) that can be regarded as "dependent variables" (meaning they depend
on the values of the other variables, which we call independent variables or
"features")

let's take `Rank` to be our target variable (eg, the dep variable that we want to
predict). now we can firm up our problem statement as follows:

    we want to build a model to predict whether a beer will score in the top
    half of the rankings

now that we've quantified our prediction goal, the problem is well-defined

once we know what question we're trying to answer, we can begin to build
our model

but before we do, let's have a look at the modeling infrastructure that we'll
use

    >>> from sklearn.linear_models import LogisticRegression as LR
    >>> model = LR()    # model is now an instance of the class we imported
    >>> help(model)

okay time to try this out!
