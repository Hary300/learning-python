// const getData = () => {
//   fetch('https://jsonplaceholder.typicode.com/posts/1')
//     .then((response) => {
//       if (!response.ok) {
//         throw Error('Something went wrong');
//       }
//       return response.json();
//     })
//     .then((data) => {
//       console.log(data);
//     })
//     .catch((error) => console.log(error));
// };

// const getData = async () => {
//   try {
//     const response = await fetch(
//       'https://jsonplaceholder.typicode.com/posts/1'
//     );

//     if (!response.ok) {
//       throw new Error('Something went wrong');
//     }
//     const data = await response.json();
//     console.log(data);
//     return data;
//   } catch (error) {
//     console.log(error);
//   }
// };
// getData();

// OOP
class Money {
  constructor(amount) {
    this.amount = amount;
  }
  valueOf() {
    return this.amount;
  }
  toString() {
    return `${this.amount} USD`;
  }
}

const money1 = new Money(100);
const money2 = new Money(250);
console.log(money1 + money2);
console.log(String(money1));
console.log(String(money2));
