import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value, callback) {
  try {
    const reply = await client.set(schoolName, value);
    console.log(`Reply: ${reply}`);
    if (callback) callback(null, reply);
  } catch (err) {
    if (callback) callback(err, null);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await client.get(schoolName);
    console.log(reply);
    return reply;
  } catch (err) {
    throw err;
  }
}

async function main() {
  await client.connect();
  
  displaySchoolValue('Holberton', (err, result) => {
    if (err) console.error('Error:', err);
  });
  
  setNewSchool('HolbertonSanFrancisco', '100', (err, result) => {
    if (err) console.error('Error:', err);
  });
  
  displaySchoolValue('HolbertonSanFrancisco', (err, result) => {
    if (err) console.error('Error:', err);
  });
}

main();