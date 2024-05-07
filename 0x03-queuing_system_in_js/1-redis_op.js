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

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

// Function to display the value for a given school name
const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.error(`Error retrieving value for ${schoolName}: ${err}`);
        } else {
            console.log(`Value for ${schoolName}: ${value}`);
        }
    });
};
