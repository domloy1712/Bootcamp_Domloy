const express = require('express');
const cors = require('cors');
require('dotenv').config({ path: '../.env' });  // Si .env está un nivel arriba

const app = express();
app.use(cors());
app.use(express.json());

app.use('/api/auth', require('./routes/auth.routes'));
app.use('/api/categories', require('./routes/category.routes'));

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Mi super servidor https://localhost:4000${PORT}`);
});
