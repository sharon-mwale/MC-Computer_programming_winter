//A
PI = 3.14159

//B
const pi = 3.14159;

const calculateArea = (radius) => {
  return pi * radius * radius;
};

const radius = 5;
const area = calculateArea(radius);
console.log("Area of the circle:", area);

//C
const name = "John Doe";
const studentId = "2023001";

const infoString = `
Name: ${name}
Student ID: ${studentId}
`;

console.log(infoString);



//D
function greetUser(name = "Guest", age = 0) {
   const greeting = `Hello, ${name}! You are ${age} years old.`;
   return greeting;
 }
 
 // Example usage:
 console.log(greetUser("Neria", 25));
 console.log(greetUser("Ethel"));
 console.log(greetUser());
 

