/**
 * Given a list of numbers, find the indices
 * of each local minimum and maximum
 */

function findLocalMinMax(input) {
    const arr = [];

    // keep track of the direction: down vs up
    var direction = 0;
    var prevEqual;

    // if 0th != 1st, 0th is a local min / max
    if (input[0] !== input[1]) {
        arr.push(0);
        if (input[0] == input[1]) {
            direction = 0;
        }
        if (a < b) {
            direction = -1;
        }
        else{
            direction = 1;
        }
        prevEqual = false;
    }

    // loop through other numbers
    for (let i = 0; i < input.length - 1; i++) {
        // compare this to next
        const next = 1;
        if (input[i] == input[i+1]) {
            next = 0;
        }
        if (input[i] < input[i+1]) {
            next = -1;
        }
        else{
            next = 1;
        }

        if (next !== 0) {
            if (next !== direction) {
                direction = next;

                if (!prevEqual) {
                    arr.push(i);
                }
            }
            prevEqual = false;
        } else if (!prevEqual) {
            // if the previous value is different and the next are equal
            // then we've found a min/max
            prevEqual = true;
            arr.push(i);
        }
    }

    return arr;
}

// The review
/*1. Use of var vs let/const:
Problem: The variable direction and prevEqual are declared using var, which can lead to issues with scope in JavaScript. Instead, we should use let or const because var is function-scoped, while let and const are block-scoped.
Fix: Replace var with let or const where appropriate.
Recommendation:

javascript
Copy code
let direction = 0;
let prevEqual = false;
2. Incorrect Use of Undefined Variables:
Problem: The variables a and b are used without being defined in this section of code:
javascript
Copy code
if (a < b) {
    direction = -1;
} else {
    direction = 1;
}
These should be replaced with input[0] and input[1] to correctly compare the first two elements.
Fix:

javascript
Copy code
if (input[0] < input[1]) {
    direction = -1;
} else {
    direction = 1;
}
3. Incorrect Initial Indexing:
Problem: The loop over the array should start from i = 1 because the first element is already handled outside of the loop. Starting from i = 0 will cause an unnecessary comparison of input[0] with input[1] again.
Fix: Start the loop from index 1 to avoid redundancy:
javascript
Copy code
for (let i = 1; i < input.length - 1; i++) {
4. Incorrect Initialization of next Variable:
Problem: In the line const next = 1;, the variable next is initially set to 1, but this is overwritten by the following conditional statements, so the assignment is unnecessary. Also, assigning next a constant value within the loop creates confusion because it makes it harder to understand what next really represents.
Fix: Initialize next as let and modify the conditional logic appropriately.

javascript
Copy code
let next;
5. Unnecessary Condition:
Problem: This part of the code doesn't make sense:
javascript
Copy code
if (input[0] == input[1]) {
    direction = 0;
}
Since this condition is within an if (input[0] !== input[1]) block, this check is redundant. It will never be true since it's already guaranteed that input[0] != input[1].
Fix: Remove the redundant check:
javascript
Copy code
// Remove this block of code
6. Clarifying the Logic for prevEqual and Direction Changes:
Problem: The logic for detecting local minima and maxima is somewhat convoluted, especially with how prevEqual is handled.
Fix: Make the conditions more straightforward. Instead of using prevEqual, we can simply track when the direction changes.
Recommendation:

javascript
Copy code
if (next !== direction) {
    arr.push(i);
    direction = next;
}
7. Handling Edge Cases:
Problem: The code assumes that the input will always have at least two elements, but what if the input has only one element or is empty?
Fix: Add a check at the start to handle such cases.
Recommendation:

javascript
Copy code
if (input.length < 2) {
    return [];  // No local min/max possible with less than 2 elements
}
8. Add Comments for Clarity:
Recommendation: Add comments to make the logic more readable and maintainable. Comments explaining why certain things are being done would make it easier for another developer to understand the code.
*/
// Final code
/**
 * Given a list of numbers, find the indices
 * of each local minimum and maximum
 */
function findLocalMinMax(input) {
    const arr = [];

    // Handle edge case where input has less than two elements
    if (input.length < 2) {
        return arr;  // No local min/max possible with less than 2 elements
    }

    // Keep track of the direction: -1 for down, 1 for up
    let direction = 0;
    
    // If 0th != 1st, 0th is a local min/max
    if (input[0] !== input[1]) {
        arr.push(0);
        if (input[0] < input[1]) {
            direction = -1;
        } else {
            direction = 1;
        }
    }

    // Loop through the rest of the numbers
    for (let i = 1; i < input.length - 1; i++) {
        let next;
        
        if (input[i] === input[i + 1]) {
            next = 0;  // Equal values mean no direction change
        } else if (input[i] < input[i + 1]) {
            next = -1;  // Upward slope
        } else {
            next = 1;   // Downward slope
        }

        // If the direction changes, add the index as a local min/max
        if (next !== 0 && next !== direction) {
            arr.push(i);
            direction = next;
        }
    }

    return arr;
}


// their final code
/*
* Given a list of numbers, find the indices
* of each local minimum and maximum (x1, x2, x3, x4)
* If the first point or last point in the graph are not equal to their neighbor,
* they are a local min or max
* Saddle points are a min/max, but the middle values in a series of equal numbers
* are not mins/maxes
*/
function findLocalMinMax(inputArr) {
    const minsAndMaxes = [];
 
    // keep track of the direction: down vs up
    let currDirection, nextDirection, prevEqual;
    if(inputArr.length < 2){
        return inputArr;
    }
 
    currDirection = determineDirection(inputArr[0], inputArr[1]);
 
    // if 0th != 1st, 0th is a local min / max
    if (currDirection !== Direction.FLAT) {
        minsAndMaxes.push(0);
        prevEqual = false;
    }
 
    // loop through other numbers
    for (let i = 1; i < inputArr.length - 1; i++) {
        // compare this to next to determine direction of next item
        nextDirection = determineDirection(inputArr[i], inputArr[i+1])
 
        if (nextDirection !=== currDirection) {
            minsAndMaxes.push(i);
        }
    }
 
    // Determine if last element is local min/max
    if (nextDirection !== Direction.FLAT)
        minsAndMaxes.push(i)
    }
 
    return minsAndMaxes;
 }
 
 function determineDirection(a, b) {
    return (a === b ? Direction.FLAT :
        a < b ? Direction.INCREASING : Direction.DECREASING;
 }
 
 
 
 const Direction = Object.freeze({
    INCREASING: 1,
    FLAT: 0,
    DECREASING: -1,
 });

