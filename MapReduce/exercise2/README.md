# MapReduce - Second Example
## MR Simple, without sorting

In this case, we will sort the words using the sort command. Pipes are very handy to test assumption

As usual, to run the scripts we have to chmod them

    chmod +x mapper.py
    chmod +x reducer.py

    ./mapper.py | sort | ./reducer.py

