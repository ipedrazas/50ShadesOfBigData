# 50 Shades Of BigData

##PyConEs 2013

###Requirements

All the code used during this workshop can be cloned from the Git Repository hosted at [ClinkerHQ](http://clinkerhq.com)

We will be using a Vagrant box with all the software installed so to be able to participate you only need to have Vagrant installed and execute

    vagrant init 50Shades http://127biscuits.com/50ShadesOfBigData.box
    vagrant up

In case you prefer to work on your own laptop without using our Vagrant box you can find the dependencies in the list below. Just note that we provide a requirtements.txt file with our code, so, perhaps it's better if you just clone our repo and install the dependencies.

  * requests
  * selenium
  * lxml
  * PyMongo
  * elasticsearch
  * gevent
  * greenlet
  * grequests
  * cssselect


### Installing Vagrant

Vagrant has a great [documentation](http://docs.vagrantup.com/v2/installation/) where you will find all what you need to run your Vagrant boxes.

You can [download](http://downloads.vagrantup.com/tags/v1.3.5) the install from [this link](http://downloads.vagrantup.com/tags/v1.3.5)

With Vagrant you can use different providers like VirtualBox or VMWare. We use [VirtualBox](https://www.virtualbox.org/wiki/Downloads) but feel free to use whichever takes your fancy.


## Workshop

During the workshop we will analyse a few datasets. There are exercises that will help you to understand the concepts

### Exercises

* [Exercise 0](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise0/README.md): The ___"Hello World"___ of Big Data is Word Count... so, let's count the words of a file the python way.
* [Exercise 1](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise1/README.md): Let's repeat the previous exercise using MapReduce. We will create two scripts a Mapper and a Reducer.
* [Exercise 2](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise2/README.md): We will improve the MapReduce sripts and will sort the map results before reduction using the sort unix utility.
* [Exercise 3](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise3/README.md): PyCon is for Python, let's see what happens when we sort the map results with python.
* [Exercise 4](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise4/README.md): We introduce a library that will help us with the data conditioning. Results of the Reduce job will be stored on a MongoDB collection.
* [Exercise 5](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise5/README.md): In this exercise will get the text files, add them to MongoDB. We will define a Map function and a reduce function using the MongoDB MapReduce features.
* [Exercise 6](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise6/README.md): This is the exercise where we will cover the whole Big Data cycle. We will go from fetching raw data to condition, clean up and analyse that data. Finally we will draw some conclusions from our analysis.
* [Exercise 7](https://github.com/ipedrazas/50ShadesOfBigData/blob/master/MapReduce/exercise7/README.md): In this exercise we want to get the best 10 stories. How do you define "The best" is going to shift the selection towards a different dataset. During this exercise we will investigate the different approaches you can have to solve this problem.


    We have a dataset, we want to see what the data can tell us. We will create (yet-another) MapReduce that will help us to analyse data in a monthly and yearly basis. Results will be displayed using a D3 calling an EndPoint built on Flask.

## Resources

* [Google Refine](http://code.google.com/p/google-refine/)
* [Open Refine](http://openrefine.org/)
* [Example of word count using python and git commits](https://gist.github.com/hjwp/7542608)

