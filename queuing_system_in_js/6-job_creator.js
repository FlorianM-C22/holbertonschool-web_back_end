import { createClient } from 'redis';
import kue from 'kue';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (error) => {
  console.log(`Notification job failed: ${error}`);
});

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

async function main() {
  await client.connect();
}

main();