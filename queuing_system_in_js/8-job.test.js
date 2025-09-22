import kue from 'kue';
import { expect } from 'chai';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('test the createPushNotificationsJobs function', function() {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', function() {
    const jobs = "12";
    expect(() => createPushNotificationsJobs(jobs, queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue for a valid array', function() {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '0987654321', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
