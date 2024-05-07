import kue from 'kue';

// Create a job queue
const queue = kue.createQueue();

// Function to send notification
const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
    // Extract phone number and message from job data
    const { phoneNumber, message } = job.data;

    sendNotification(phoneNumber, message);
    done();
});
