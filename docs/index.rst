.. Dowell Permutation Function documentation master file, created by
   sphinx-quickstart on Tue Jun 20 22:06:41 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Dowell Permutation Function's documentation!
=======================================================

Welcome to the Permutation API! The Permutation API is a comprehensive tool that enables users to generate permutations of a set of items efficiently. It provides a reliable and high-performance solution for permutation calculations, making it ideal for a wide range of applications such as combinatorial optimization, data analysis, and algorithm design.


------------------------
Permutation Function API
------------------------

Features
--------

The Permutation API offers the following key features:

- ``Total Number of Permutations Possible`` : this feature calculates the precise count of all the potential permutations based on the provided values of ``'n'`` and ``'r'``.
- ```Exact Permutations``` : this feature allows users to find the precise permutations for any given range of ``'n'`` and ``'r'``. This feature utilizes a specially designed algorithm that ensures accurate and efficient permutation generation.

``Note`` : ``'n'`` is total number of items present and ``'r'`` is the total number of items to be selected from ``'r'``.


Example
-------

Here is an example of how you can use the Permutation API Python Library:

1. Imagine you have a set of 5 letters: A, B, C, D, and E. You want to generate all possible permutations of these letters by selecting 3 letters.
2. You can use the Permutations API and provide ``'n'`` as 5 and ``'r'`` as 3 and the letter with which you want start calculating the permutations.

   .. code-block:: python

          # import the package and instantiate an object
          from permutation import Permutation
          perm = Permutation()

          # call the find function
          result = perm.find(5,3, 'A')


3. Once the request is made, the API will process the data and return a response in JSON format. The response will include the total number of possible permutations, along with the generated permutations.

   .. code-block:: javascript

         // Sample Output
         {"eventId": "FB1010000000000000000000003004",
          "n": 5,
          "r": 3,
          "numberOfPermutations": 60,
          "permutationsVariables": ["A"],
          "inserted_id": "649351296046997800e2a35b"
          }
4. You will now need to select one permuation from the generated permutations and call the API again by providing the next letter that you want to include in the permutation.
5. Repeat the steps until the 3 letters are selected and permutation for 3 letters is generated.



.. toctree::
   :maxdepth: 2

   source/api/permutation




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`