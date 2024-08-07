const connectToDB = () => {
  const dummyPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Connected to the database...');
      console.log('Connected to the database promise resolved...');
    }, 1000);
  });

  return dummyPromise;
};

export default connectToDB;
