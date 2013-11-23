# MapReduce using MongoDB

Time is our biggest enemy when dealing with Big Data. Let's try to minimise it as much as possible.

We are going to do something a bit bold. We are going to read the books again, and we will create a dictionary with two entries: file name and text.

We will save these 3 objects in MongoDB and will run a Map Reduce job there.


    python books.py

Once the script is finished loading the books into MongoDB, we create the MapReduce Job using [MongoDB MR funcionality](http://docs.mongodb.org/manual/core/map-reduce/).

If you get the message "Connected successfully" you are good to go. Do not use the `./mongo.py` form since you will not use the virtualenv libraries.

    > res = db.books.mapReduce(map, reduce, {out: 'book_word_count'});
    {
        "result" : "book_word_count",
        "timeMillis" : 11482,
        "counts" : {
            "input" : 3,
            "emit" : 330862,
            "reduce" : 19208,
            "output" : 60841
        },
        "ok" : 1,
    }
