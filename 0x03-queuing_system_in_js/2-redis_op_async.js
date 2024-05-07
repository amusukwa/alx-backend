import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Handle Redis connection event
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = async (schoolName, value) => {
    await setAsync(schoolName, value);
    console.log(`Set value for ${schoolName}: ${value}`);
};

const displaySchoolValue = async (schoolName) => {
    try {
        const value = await getAsync(schoolName);
        console.log(`Value for ${schoolName}: ${value}`);
    } catch (error) {
        console.error(`Error retrieving value for ${schoolName}: ${error}`);
    }
};

// Call the functions
(async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();


