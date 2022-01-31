import { createQueue } from 'kue';

const queue = createQueue();
const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  const { progress } = job;

  if (blacklist.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else if (progress === 50) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
};

queue.process('notify', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

queue.on('error', (err) => {
  console.log('Oops... ', err);
});
