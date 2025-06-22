// Ask user for a number
const input = prompt(
  "Enter a number to calculate the sum from 1 to that number:"
);
const n = parseInt(input);

// Validate and compute sum using formula
if (!isNaN(n) && n > 0) {
  const sum = (n * (n + 1)) / 2;
  document.getElementById(
    "title"
  ).textContent = `Sum of Numbers from 1 to ${n}`;
  document.getElementById(
    "result"
  ).textContent = `The sum from 1 to ${n} is: ${sum}`;
} else {
  document.getElementById("title").textContent = "Invalid Input";
  document.getElementById("result").textContent =
    "Please enter a valid positive number.";
}
