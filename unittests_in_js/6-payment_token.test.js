const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
    it('should return a successful response when success is true', function(done) {
        getPaymentTokenFromAPI(true)
            .then((response) => {
                expect(response).to.have.property('data');
                expect(response.data).to.equal('Successful response from the API');
                done();
            })
            .catch((error) => {
                done(error);
            });
    });

    it('should return undefined when success is false', function(done) {
        const result = getPaymentTokenFromAPI(false);
        expect(result).to.be.undefined;
        done();
    });

    it('should return undefined when success is not provided', function(done) {
        const result = getPaymentTokenFromAPI();
        expect(result).to.be.undefined;
        done();
    });
});
