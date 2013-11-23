# MapReduce using MongoDB

We are going to repeat our last exercise but we will be adding the words to a MongoDB Collection. Once we have the collection we will run 2 MapReduce jobs. One written in Javascript using MongoDB MapReduce capabilities and another one in pure python.

First, try that you can connect to the MongoDB using:


    python mongo.py

If you get the message "Connected successfully" you are good to go. Do not use the `./mongo.py` form since you will not use the virtualenv libraries.

    time python mapper.py | python reducer.py

We add the time because we want to know how long it takes to run the script:

    time python mapper.py | python reducer.py

        real    8m3.437s
        user   3m34.749s
        sys     1m23.085s

    With filter of words longer than 3 letters:

    time python mapper.py | python reducer.py

        real    5m31.269s
        user   2m23.985s
        sys     0m59.576s




