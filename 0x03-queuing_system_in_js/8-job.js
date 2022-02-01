const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const jb = queue.create('push_notification_code_3', job);

    jb.save((err) => {
      if (!err) console.log(`Notification job created: ${jb.id}`);
    });

    jb.on('complete', () => {
      console.log(`Notification job ${jb.id} completed`);
    });

    jb.on('failed', (err) => {
      console.log(`Notification job ${jb.id} failed: ${err}`);
    });

    jb.on('progress', (progress) => {
      console.log(`Notification job ${jb.id} ${progress}% complete`);
    });
  });
};

export default createPushNotificationsJobs;
