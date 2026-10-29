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

const getData = async () => {
  try {
    const response = await fetch(
      'https://jsonplaceholder.typicode.com/posts/1'
    );

    if (!response.ok) {
      throw new Error('Something went wrong');
    }
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.log(error);
  }
};
getData();
