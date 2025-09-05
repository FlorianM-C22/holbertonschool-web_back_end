const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return 4 when adding 1 and 3', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 when adding 1 and 3.7', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 when adding 1.2 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 when adding 1.5 and 3.7', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
    assert.strictEqual(calculateNumber(-1.5, -3.7), -5);
  });

  it('should handle zero values', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(0.4, 0.4), 0);
    assert.strictEqual(calculateNumber(0.5, 0.5), 2);
  });

  it('should handle large numbers', function() {
    assert.strictEqual(calculateNumber(1000000.4, 2000000.4), 3000000);
    assert.strictEqual(calculateNumber(1000000.5, 2000000.5), 3000002);
  });

  it('should handle decimal rounding correctly', function() {
    assert.strictEqual(calculateNumber(1.1, 2.1), 3);
    assert.strictEqual(calculateNumber(1.9, 2.9), 5);
    assert.strictEqual(calculateNumber(1.4, 2.4), 3);
    assert.strictEqual(calculateNumber(1.6, 2.6), 5);
  });
});
