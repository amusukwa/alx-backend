import redis from 'redis';

// Create a Redis client for publisher
const publisher = redis.createClient();

// Handle Redis connection event for publisher
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle Redis error event for publisher
publisher.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});
const publishMessage = (message, time) => {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school', message);
    }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
