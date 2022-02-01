import {
  createClient,
} from 'redis';
import util from 'util';
import {
  createQueue,
} from 'kue';
import express from 'express';
import bodyParser from 'body-parser';

// Redis client
const client = createClient();
client.get = util.promisify(client.get);

(async () => {
  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
})();

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const promise = await client.get('available_seats');
  return promise;
};

reserveSeat(50);
let reservationEnabled = true;

// Kue queue
const queue = createQueue();

const createReservationJob = (res) => {
  const job = queue.create('reserve_seat', {
    numberOfSeats: 1,
  }).save((err) => {
    if (err) {
      res.send({
        "status": "Reservation failed"
      });
    } else {
      res.send({
        "status": "Reservation in process"
      });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (msg) => {
    console.log(`Seat reservation job ${job.id} failed: ${msg}`);
  });
}

// Express server
const app = express();
app.use(bodyParser.json());
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.send({
    "numberOfAvailableSeats": availableSeats,
  });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.status(404).send({
      "status": "Reservation are blocked"
    });
  } else {
    createReservationJob(res);
  }
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    const numberOfSeats = job.data.numberOfSeats;
    let seats = parseInt(availableSeats);
    seats -= numberOfSeats;
    reserveSeat(seats);
    if (seats === 0) {
      reservationEnabled = false;
    }
    if (seats >= 0) {
      done();
    } else {
      done(Error('Not enough seats available'));
    }
  });
  res.send({
    "status": "Queue processing"
  });
});

app.listen(port);
