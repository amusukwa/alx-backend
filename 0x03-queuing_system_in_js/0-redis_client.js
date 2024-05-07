import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle Redis connection event
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle Redis error event
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});
