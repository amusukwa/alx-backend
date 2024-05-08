import kue from 'kue';

// Create an array for blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0, 100);

  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    job.failed(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Update progress to 50%
  job.progress(50, 100);

  // Log the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate asynchronous task
  setTimeout(() => {
    // Mark the job as completed
    job.complete();

    // Call the callback function
    done();
  }, 1000); // Simulated delay of 1 second
}

// Create a job queue
const queue = kue.createQueue({
  concurrent: 2 // Process two jobs at a time
});

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('ready', () => {
  console.log('Queue is ready!');
});

queue.on('job remove', (id) => {
  console.log(`Job ${id} has been removed from the queue`);
});

