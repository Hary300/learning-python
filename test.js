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
console.log(money1 - money2);
console.log(String(money1));
console.log(String(money2));

// class BankAccount {
//   constructor(owner, balance) {
//     ((this.owner = owner), (this.balance = balance ?? 0));
//   }

//   deposit(amount) {
//     if (amount <= 0) {
//       console.log('Invalid amount');
//       return;
//     }

//     this.balance += amount;
//     console.log(this.balance);
//     return this.balance;
//   }

//   withdraw(amount) {
//     if (amount > this.balance) {
//       console.log('Insufficient funds');
//       return;
//     }

//     if (amount <= 0) {
//       console.log('Invalid amount');
//       return;
//     }

//     this.balance -= amount;
//     console.log(this.balance);
//     return this.balance;
//   }

//   getBalance() {
//     console.log(this.balance);
//     return this.balance;
//   }
// }

// const account = new BankAccount('John', 100);

// account.deposit(50); // 150
// account.withdraw(30); // 120
// account.getBalance(); // 120

// account.withdraw(200); // "Insufficient funds"
// account.deposit(-10); // "Invalid amount"
