//Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

function createPhoneNumber(numbers) {
    // Ensure the input is an array of 10 digits
    if (!Array.isArray(numbers) || numbers.length !== 10 || numbers.some(n => n < 0 || n > 9)) {
        throw new Error("Input must be an array of 10 integers between 0 and 9.");
    }

    const areaCode = numbers.slice(0, 3).join('');
    const firstPart = numbers.slice(3, 6).join('');
    const secondPart = numbers.slice(6).join('');

    return `(${areaCode}) ${firstPart}-${secondPart}`;
}