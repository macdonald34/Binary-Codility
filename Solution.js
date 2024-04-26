function solution(N) {
    // Convert N to binary representation
    const binary = N.toString(2);
    
    let maxGap = 0;
    let currentGap = 0;
    let counting = false;

    // Iterate through the binary representation
    for (let i = 0; i < binary.length; i++) {
        if (binary[i] === '1') {
            // Found a '1', check if this ends a gap
            if (counting && currentGap > maxGap) {
                maxGap = currentGap;
            }
            counting = true;
            currentGap = 0;
        } else if (counting) {
            // Found a '0' within a gap
            currentGap++;
        }
    }

    return maxGap;
}

// Test cases
console.log(solution(1041)); // Output: 5
console.log(solution(32));   // Output: 0
