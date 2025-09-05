const { expect } = require('chai');
const request = require('request');
const sinon = require('sinon');
const app = require('./api');

describe('API Integration test', function() {
    const baseUrl = 'http://localhost:7865';

    it('should return correct response for GET /', function(done) {
        request.get(baseUrl, function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });

    it('should handle 404 for non-existent routes', function(done) {
        request.get(`${baseUrl}/nonexistent`, function(error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});
