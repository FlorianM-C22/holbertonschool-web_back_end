import { createClient } from "redis";
const express = require('express');
const util = require('util');
const app = express();
const port = 1245;

const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);

const listProducts = [
  { "id": 1, "name": "Suitcase 250", "price": 50, "stock": 4 },
  { "id": 2, "name": "Suitcase 450", "price": 100, "stock": 10 },
  { "id": 3, "name": "Suitcase 650", "price": 350, "stock": 2 },
  { "id": 4, "name": "Suitcase 1050", "price": 550, "stock": 5 }
];

app.get('/list_products', (_req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = listProducts.find(item => item.id === itemId);

  if (!product) {
    return res.status(404).json({status: 'Product not found' });
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentStock = product.stock - reservedStock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentStock
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = listProducts.find(item => item.id === itemId);

  if (!product) {
    return res.status(404).json({status: 'Product not found' });
  }

  let reservedStock = await getCurrentReservedStockById(itemId);
  const currentStock = product.stock - reservedStock;

  if (currentStock <= 0) {
    return res.status(400).json({status: "Not enough stock available", "itemId": itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);
  res.status(202).json({status: "Reservation confirmed", "itemId": itemId });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock.toString());
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}