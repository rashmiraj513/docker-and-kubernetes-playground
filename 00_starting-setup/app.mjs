import express from 'express';
import connectToDB from './helpers.mjs';

const app = express();

app.get('/', (req, res) => {
  res.send('<h1>Hello, World!</h1>');
});

await connectToDB();

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}...`);
});
