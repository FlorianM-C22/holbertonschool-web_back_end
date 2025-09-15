const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
    it('should stub Utils.calculateNumber and spy on console.log', function() {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const spy = sinon.spy(console, 'log');
        
        sendPaymentRequestToApi(100, 20);
        
        expect(stub.calledWith('SUM', 100, 20)).to.be.true;
        expect(spy.calledWith('The total is: 10')).to.be.true;
        
        stub.restore();
        spy.restore();
    });
});
