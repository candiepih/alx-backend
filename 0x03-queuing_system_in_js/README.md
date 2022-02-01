# Queuing System in JS

The aim of this project was to understand the following the following concepts:-

* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

## Files

[package.json](./package.json) - The package.json file containing the dependencies and the scripts to run the project

[.babelrc](./.babelrc) - The babel configuration file

[dump.rdb](./dump.rdb) - The Redis dump file

[0-redis_client.js](./0-redis_client.js)

Script that connect's to the Redis server running on your machine.

[1-redis_op.js](./1-redis_op.js)

Script that connect's to the Redis server running on your machine and has following methods:-

* `setNewSchool` - It accepts two arguments `schoolName`, and `value` and set in Redis the value for the key `schoolName`
* `displaySchoolValue` - It accepts one argument `schoolName` and log to the console the value for the key passed as argument

[2-redis_op_async.js](./2-redis_op_async.js)

Using `promisify`, modify the function `displaySchoolValue` to use ES6 `async` / `await`

[4-redis_advanced_op.js](./4-redis_advanced_op.js)

Uses Redis client to store a hash value with following keys and values:-

* Portland=50
* Seattle=80
* New York=20
* Bogota=20
* Cali=40
* Paris=2

[5-subscriber.js](./5-subscriber.js))

connects to redis server and subscribes to the channel `holberton school channel` and prints the message received from the channel

[5-publisher.js](./5-publisher.js)

connects to redis server and publishes the message `holberton school channel`

[6-job_creator.js](./6-job_creator.js)

Creates a queue named `push_notification_code`, and create a job with the following object

```js
{
  phoneNumber: string,
  message: string,
}
```

[6-job_processor.js](./6-job_processor.js)

Creates a queue process that will listen to new jobs on `push_notification_code`

[7-job_creator.js](./7-job_creator.js)

Creates an array kue queue jobs.

[7-job_processor.js](./7-job_processor.js)

Creates a queue process that process job of the queue `push_notification_code_2` with two jobs at a time.

[8-job.js](./8-job.js)

method: `createPushNotificationsJobs`

* It takes into argument `jobs` (array of objects), and `queue` (`Kue` queue)
* If `jobs` is not an array, it should throw an `Error` with message: `Jobs is not an array`
* For each job in `jobs`, create a job in the queue `push_notification_code_3`
* When a job is created, it should log to the console `Notification job created: JOB_ID`
* When a job is complete, it should log to the console `Notification job JOB_ID completed`
* When a job is failed, it should log to the console `Notification job JOB_ID failed: ERROR`
* When a job is making progress, it should log to the console `Notification job JOB_ID PERCENT% complete`

[8-job.test.js](./8-job.test.js)

Test suite for the `createPushNotificationsJobs` function in [8-job.js](./8-job.js).

[9-stock.js](./9-stock.js)

Contains stock data(array of objects) an express server to handle the requests for the stock API and a Redis client to store and track the stock data.

[100-seat.js](./100-seat.js)

Contains redis client to store and track the seat data and queue `kue` jobs and an express server to handle the requests for the seat API.
