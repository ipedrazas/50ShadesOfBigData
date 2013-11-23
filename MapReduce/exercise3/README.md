# MapReduce - Third Example
## MR Simple, Sorted

In this case, we will sort the words using the sort method of a python list.

As usual, to run the scripts we have to chmod them

    chmod +x mapper.py
    chmod +x reducer.py

    ./mapper.py | sort | ./reducer.py

 If you want to double check which method takes longer you can use the time instruction.

    time ./mapper.py | sort | ./reducer.py

In case you want to save the resuts in a file, the easiest way is, again, to use a pipe to redirect the standard output to a file.

    ./mapper.py | sort | ./reducer.py > results.txt

Then, if you want to find out the occurrences of a word... again, we will use our friend the command line, in this case __grep__

    grep sex results.txt
    -> % grep sexo results.txt
    sexo was found 157 times
