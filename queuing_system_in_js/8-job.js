export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
      throw Error('Jobs is not an array');
    }
    jobs.forEach(element => {
      const job = queue.create('push_notification_code_3', element)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`)
        } else {
          console.log(`Notification job ${job.id} failed: ${err}`)
        }
      })
  
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`)
      })
  
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
    });
  }