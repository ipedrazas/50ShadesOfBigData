# MapReduce - First Example
## MR Simple

We have two scripts that will execute each of the two steps of the MapReduce operation:

   * mapper.py: Receives the std in and it process it line by line. Each line is splitted in words and every word is weighed to 1. The result is returned through the std. out.
   * reducer.py: Receives a text through  the Std. In, It's processed line by line and returns the addition of all the words
   * input.txt: this will be our dataset. File located at ../../Data/input.txt




The we will run the following command:

	python mapper.py < ../../Data/input.txt | sort | python reducer.py
	python mapper.py < ../../Data/input.txt | sort | python reducer_inv.py

