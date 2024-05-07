import kue from 'kue';

// Create a job queue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, world!'
};

const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        } else {
            console.error(`Error creating notification job: ${err}`);
        }
    });

job.on('complete', () => {
    console.log('Notification job completed');
});
job.on('failed', () => {
    console.log('Notification job failed');
});
