import express from 'express';

const app = express();
const PORT = 1245;
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Data access
const getItemById = (id) => {
  return listProducts.find(product => product.itemId === id);
};

// Server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Product detail
app.get('/list_products/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const currentQuantity = getCurrentReservedStockById(itemId);
    res.json({ ...product, currentQuantity });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const currentQuantity = getCurrentReservedStockById(itemId);
    if (currentQuantity >= 1) {
      res.json({ status: 'Not enough stock available', itemId });
    } else {
      reserveStockById(itemId, 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  }
});

const reservedStock = {};

const reserveStockById = (itemId, stock) => {
  reservedStock[itemId] = reservedStock[itemId] ? reservedStock[itemId] + stock : stock;
};

const getCurrentReservedStockById = (itemId) => {
  return reservedStock[itemId] || 0;
};

