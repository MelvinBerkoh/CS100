// Complete the sort function so that it returns the items passed into it in alphanumerical order. Conveniently enough, the standard array sort method has been disabled for you so that you are forced to create your own.

// Example:

// sort([1,3,2])  should return [1,2,3]
function sort(items){
  // since this is going to be done by index we are going have a iterator variable 
  let it = 0
// while the iterator is less than the length of array since we start at 0 the index of the last number in the list is always going to be less that the length of the list 
  while(it < items.length){
    // temp variable to hold the literal value of the part we are on
    currentNumber = items[it]
    nextNumber = items[it+1]
    // now we will compare the value of temp to the literal value of item at index of i + 1 which is the next value in the array
    if(currentNumber > nextNumber){
      // if the value of previous number is greater than the value of the next value we have to switch
     currentNumber = nextNumber  // the current index  becomes the next value
     nextNumber = currentNumber // the next index becomes thats the current value
    }
    it++
  }
  return items
}
console.log(sort([ 1, 2, 3, 3, 1, 4]))
