#!/usr/bin/node
// Check if there is enough arguments
if (process.argv.length <= 3) {
  // If not enough arguments, print '0'
  console.log(0);
} else {
  // If enough arguments, proceed to finding the second largest

  // Extract arguments starting from the third one and convert them to numbers
  const numbers = process.argv.slice(2).map(Number);

  // Sort the numbers in descending order using the sort function
  const sortedNumbers = numbers.sort(function (a, b) {
    return b - a; // Sort in descending order
  });
  // Access the second element at index 1 in the sorted array,
  // which is the second largest number in the array
  const secondLargest = sortedNumbers[1];

  // Print the second largest number
  console.log(secondLargest);
}
