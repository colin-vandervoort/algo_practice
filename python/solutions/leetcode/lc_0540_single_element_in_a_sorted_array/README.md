Solutions must make use of the pre-sorted nature of the array in order to find the element in log(N) time

This could potentially be done using a divide-and-conquer approach. Recursively splitting the array up into two parts seems possible, but would require some logic to handle the exact position of the split.

The original array will always have an odd number of elements, so the middle five elements (or ) will need to be inspected in order to determine where to perform the split. Here are the cases for that initial split - sorted arrays with only one or three elements can be handled first as special cases.

1. The single element is immediately detected in the second, third, or fourth positions. It is possible that the element appears in the first or fifth position of this initially inspected window, but that won't be apparent until later. 
  - examples
    - [1, **1**, *2*, **3**, **3**, **4**, 4]
    - [**1**, **1**, *2*, **3**, **3**]
    - [1, **1**, **2**, **2**, *3*, **4**, 4]
2. The single element is determined to be in the lower part of the original array, due to the second/third and fourth/fifth elements being matched pairs.
3. The single element is determined to be in the upper part of the original array, due to the first/second and third/fourth elements being matched pairs.

For (sub)arrays with an even number of elements, the middle four (4) elements should be inspected.