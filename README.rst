cmpGen is deprecated.
Please just use the "key" parameter of sort/sorted instead.
It is better in every conceivable way (faster, simpler, more legible, etc.)

For example, here is the example below, but entirely using "key" instead:

l=[3,0,1,-2,4,3,-5]
l.sort(key=abs)
l now is [0,1,-2,3,3,4,-5]

This pakage is now here just to support legacy version of packages that used this.
Again, please don't use this package :)


Old README for reference:
-------------------------

cmpGen is a very simple utility to aid in sorting.
Basically, I often want to sort a list based on a specific property
or more generically a function of the values in the list.
cmpGen acts as a middle layer to make this process simple.

Usage:
l is a list
l.sort(cmpGen(someFunctionThatActsOnListElements))

Example 1: Sort a list of 2-integer pairs based on second element in the pair:
l=[[3,3],[1,6],[0,12],[1,1],[7,4],[6,7]]
l.sort(cmpGen(lambda x: x[1]))
l is now [[1, 1], [3, 3], [7, 4], [1, 6], [6, 7], [0, 12]]

Example 2: Sort based on the absolute value of list elements:
l=[3,0,1,-2,4,3,-5]
l.sort(cmpGen(abs))
l now is [0,1,-2,3,3,4,-5]

