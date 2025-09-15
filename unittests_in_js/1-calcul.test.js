const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
    describe('SUM operation', function() {
        it('should return the sum of two rounded numbers', function() {
            assert.strictEqual(calculateNumber('SUM', 1.4, 2.6), 4);
            assert.strictEqual(calculateNumber('SUM', 1.5, 2.5), 5);
            assert.strictEqual(calculateNumber('SUM', 1.2, 2.8), 4);
            assert.strictEqual(calculateNumber('SUM', 0.1, 0.2), 0);
            assert.strictEqual(calculateNumber('SUM', -1.4, -2.6), -4);
        });
    });

    describe('SUBTRACT operation', function() {
        it('should return the difference of two rounded numbers', function() {
            assert.strictEqual(calculateNumber('SUBTRACT', 5.4, 2.6), 2);
            assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 2.5), -1);
            assert.strictEqual(calculateNumber('SUBTRACT', 3.2, 1.8), 1);
            assert.strictEqual(calculateNumber('SUBTRACT', 0.1, 0.2), 0);
            assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -2.6), 2);
        });
    });

    describe('DIVIDE operation', function() {
        it('should return the division of two rounded numbers', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 6.4, 2.6), 2);
            assert.strictEqual(calculateNumber('DIVIDE', 1.5, 2.5), 0.6666666666666666);
            assert.strictEqual(calculateNumber('DIVIDE', 3.2, 1.8), 1.5);
            assert.strictEqual(calculateNumber('DIVIDE', 8.4, 2.6), 2.6666666666666665);
        });

        it('should return "Error" when dividing by zero', function() {
            assert.strictEqual(calculateNumber('DIVIDE', 5.4, 0.4), 'Error');
            assert.strictEqual(calculateNumber('DIVIDE', 1.5, 0.2), 'Error');
            assert.strictEqual(calculateNumber('DIVIDE', 3.2, 0.1), 'Error');
            assert.strictEqual(calculateNumber('DIVIDE', 8.4, 0.3), 'Error');
        });
    });

    describe('Invalid operation type', function() {
        it('should return undefined for invalid operation types', function() {
            assert.strictEqual(calculateNumber('MULTIPLY', 1.4, 2.6), undefined);
            assert.strictEqual(calculateNumber('INVALID', 1.5, 2.5), undefined);
            assert.strictEqual(calculateNumber('', 3.2, 1.8), undefined);
            assert.strictEqual(calculateNumber(null, 8.4, 2.6), undefined);
        });
    });

    describe('Edge cases', function() {
        it('should handle negative numbers correctly', function() {
            assert.strictEqual(calculateNumber('SUM', -1.4, -2.6), -4);
            assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -2.6), 2);
            assert.strictEqual(calculateNumber('DIVIDE', -6.4, 2.6), -2);
        });

        it('should handle zero values correctly', function() {
            assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
            assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
            assert.strictEqual(calculateNumber('DIVIDE', 0, 1.4), 0);
        });

        it('should round numbers correctly', function() {
            assert.strictEqual(calculateNumber('SUM', 1.49, 2.49), 3);
            assert.strictEqual(calculateNumber('SUM', 1.51, 2.51), 5);
            assert.strictEqual(calculateNumber('SUBTRACT', 3.49, 1.49), 2);
            assert.strictEqual(calculateNumber('SUBTRACT', 3.51, 1.51), 2);
        });
    });
});
