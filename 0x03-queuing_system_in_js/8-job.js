function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    // Create a job in the queue push_notification_code_3
    const job = queue.create('push_notification_code_3', jobData);

    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // When a job fails
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // When a job is making progress
    job.on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
}

export default createPushNotificationsJobs;
