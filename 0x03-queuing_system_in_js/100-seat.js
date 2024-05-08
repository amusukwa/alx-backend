import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const PORT = 1245;
const client = redis.createClient();
const queue = kue.createQueue();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize the number of available seats and reservationEnabled
let numberOfAvailableSeats = 50;
let reservationEnabled = true;

// Redis functions
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats);
}

// Kue queue
queue.process('reserve_seat', async (job, done) => {
  // Dummy implementation for demonstration
  const randomSuccess = Math.random() >= 0.5;
  if (randomSuccess) {
    console.log(`Seat reservation job ${job.id} completed`);
    done();
  } else {
    console.error(`Seat reservation job ${job.id} failed`);
    done(new Error('Some error occurred during reservation'));
  }
});

// Server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Routes
app.get('/available_seats', async (req, res) => {
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentSeats = await getCurrentAvailableSeats();
  const availableSeats = currentSeats - 1;

  if (availableSeats === 0) {
    reservationEnabled = false;
  } else if (availableSeats >= 0) {
    await reserveSeat(availableSeats);
  } else {
    throw new Error('Not enough seats available');
  }
});
