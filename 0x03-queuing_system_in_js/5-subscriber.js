import redis from 'redis';

// Create a Redis client for subscriber
const subscriber = redis.createClient();

// Handle Redis connection event for subscriber
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle Redis error event for subscriber
subscriber.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

subscriber.subscribe('holberton school');

subscriber.on('message', (channel, message) => {
    console.log(`Message received on channel ${channel}: ${message}`);
    if (message === 'KILL_SERVER') {
        console.log('Unsubscribing and quitting...');
        subscriber.unsubscribe('holberton school');
        subscriber.quit();
    }
});
