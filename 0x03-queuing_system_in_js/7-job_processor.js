import { createQueue } from 'kue';

const queue = createQueue();
const blacklist = ['4153518780', '4153518781'];

let progress = 0;
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress((progress += 1), 100);
  if (blacklist.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  if (progress >= 50) done();
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

queue.on('error', (err) => {
  console.log('Oops... ', err);
});
