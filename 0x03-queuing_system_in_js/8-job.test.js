import {
  createQueue,
} from 'kue';
import {
  expect,
} from 'chai';
import createPushNotificationsJobs from './8-job';
import sinon from 'sinon';

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  it('display a error message if jobs is not an array', () => {
    const list = 'not an array';
    expect(() => createPushNotificationsJobs(list, queue)).to.throw();
  });

  it('create two new jobs to the queue', () => {
    const list = [{
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '35235242423',
        message: 'This is the code 4242 to verify your account',
      },
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('display correct message when a job is created', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    }];
    const spy = sinon.spy(console, 'log');
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];
    expect(spy.calledWith(`Notification job created: ${job.id}`)).to.equal(true);
    spy.restore();
  });

  it('display correct message when a job is completed', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];

    const spy = sinon.spy(console, 'log');
    job._events.complete();
    expect(spy.calledWith(`Notification job ${job.id} completed`)).to.equal(true);
    spy.restore();
  });

  it('display correct message when a job is failed with error', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];

    const spy = sinon.spy(console, 'log');
    const err = 'I am the error message';
    job._events.failed(err);
    expect(spy.calledWith(`Notification job ${job.id} failed: ${err}`)).to.equal(true);
    spy.restore();
  });

  it('display correct message for job progress', () => {
    const list = [{
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    }];
    createPushNotificationsJobs(list, queue);
    const job = queue.testMode.jobs[0];

    const spy = sinon.spy(console, 'log');
    const progress = 50;
    job._events.progress(progress);
    expect(spy.calledWith(`Notification job ${job.id} ${progress}% complete`)).to.equal(true);
    spy.restore();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });
});
