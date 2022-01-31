import {
  createQueue,
} from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
