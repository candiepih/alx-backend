import redis, {
  createClient,
} from 'redis';
import util from 'util';

const client = createClient();
client.get = util.promisify(client.get);

(async () => {
  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
})();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  const value = await client.get(schoolName);
  console.log(value);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
