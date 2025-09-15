const expect = require('chai').expect;
const request = require('request');
const app = require('./api');

describe('api',  () => {
  it('respond with the message Welcome to the payment system', function (done) {
    request.get('http://localhost:7865', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    })
  });

  it('respond with the message Welcome to the payment system', function (done) {
    request.get('http://localhost:7865', (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    })
  });
});