const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
    describe('SUM operation', function() {
        it('should return the sum of two rounded numbers', function() {
            expect(calculateNumber('SUM', 1.4, 2.6)).to.equal(4);
            expect(calculateNumber('SUM', 1.5, 2.5)).to.equal(5);
            expect(calculateNumber('SUM', 1.2, 2.8)).to.equal(4);
            expect(calculateNumber('SUM', 0.1, 0.2)).to.equal(0);
            expect(calculateNumber('SUM', -1.4, -2.6)).to.equal(-4);
        });
    });

    describe('SUBTRACT operation', function() {
        it('should return the difference of two rounded numbers', function() {
            expect(calculateNumber('SUBTRACT', 5.4, 2.6)).to.equal(2);
            expect(calculateNumber('SUBTRACT', 1.5, 2.5)).to.equal(-1);
            expect(calculateNumber('SUBTRACT', 3.2, 1.8)).to.equal(1);
            expect(calculateNumber('SUBTRACT', 0.1, 0.2)).to.equal(0);
            expect(calculateNumber('SUBTRACT', -1.4, -2.6)).to.equal(2);
        });
    });

    describe('DIVIDE operation', function() {
        it('should return the division of two rounded numbers', function() {
            expect(calculateNumber('DIVIDE', 6.4, 2.6)).to.equal(2);
            expect(calculateNumber('DIVIDE', 1.5, 2.5)).to.equal(0.6666666666666666);
            expect(calculateNumber('DIVIDE', 3.2, 1.8)).to.equal(1.5);
            expect(calculateNumber('DIVIDE', 8.4, 2.6)).to.equal(2.6666666666666665);
        });

        it('should return "Error" when dividing by zero', function() {
            expect(calculateNumber('DIVIDE', 5.4, 0.4)).to.equal('Error');
            expect(calculateNumber('DIVIDE', 1.5, 0.2)).to.equal('Error');
            expect(calculateNumber('DIVIDE', 3.2, 0.1)).to.equal('Error');
            expect(calculateNumber('DIVIDE', 8.4, 0.3)).to.equal('Error');
        });
    });

    describe('Invalid operation type', function() {
        it('should return undefined for invalid operation types', function() {
            expect(calculateNumber('MULTIPLY', 1.4, 2.6)).to.be.undefined;
            expect(calculateNumber('INVALID', 1.5, 2.5)).to.be.undefined;
            expect(calculateNumber('', 3.2, 1.8)).to.be.undefined;
            expect(calculateNumber(null, 8.4, 2.6)).to.be.undefined;
        });
    });

    describe('Edge cases', function() {
        it('should handle negative numbers correctly', function() {
            expect(calculateNumber('SUM', -1.4, -2.6)).to.equal(-4);
            expect(calculateNumber('SUBTRACT', -1.4, -2.6)).to.equal(2);
            expect(calculateNumber('DIVIDE', -6.4, 2.6)).to.equal(-2);
        });

        it('should handle zero values correctly', function() {
            expect(calculateNumber('SUM', 0, 0)).to.equal(0);
            expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
            expect(calculateNumber('DIVIDE', 0, 1.4)).to.equal(0);
        });

        it('should round numbers correctly', function() {
            expect(calculateNumber('SUM', 1.49, 2.49)).to.equal(3);
            expect(calculateNumber('SUM', 1.51, 2.51)).to.equal(5);
            expect(calculateNumber('SUBTRACT', 3.49, 1.49)).to.equal(2);
            expect(calculateNumber('SUBTRACT', 3.51, 1.51)).to.equal(2);
        });
    });
});
