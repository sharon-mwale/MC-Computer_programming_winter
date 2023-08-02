class Person {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }
  
    introduce() {
      return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
  }
  
  const person = new Person("Neria", 25);
  console.log(person.introduce());
  
  
  