const assert = require('assert')
const calculateNumber = require('./1-calcul');

describe('The calculateNumber function', function () {
  it('should return an error if the first argument is incorrect', function () {
    assert.equal(calculateNumber("TEST", 1.5, 2.0), "Error");
  });

  it('should return an error if the first argument is not capitalized correctly', function () {
    assert.equal(calculateNumber("Sum", 1.5, 2.0), "Error");
  });

  it('should return an error if the first argument is not a string', function () {
    assert.equal(calculateNumber(1, 1.5, 2.0), "Error");
  });
});

describe('The calculateNumber function', function() {
  it('should round the numbers and return their sum when using "SUM" as the first argument', function() {
    const result = calculateNumber("SUM", 1.5, 2.3);
    assert.equal(result, 4);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUM", 1.5, 2);
    assert.equal(result, 4);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUM", 1, 2.5);
    assert.equal(result, 4);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUM", 1.1, 2);
    assert.equal(result, 3);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUM", 1, 2.1);
    assert.equal(result, 3);
  });

  it('should work with integer values', function() {
    const result = calculateNumber("SUM", 1, 4);
    assert.equal(result, 5);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber("SUM", 0, 0);
    assert.equal(result, 0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("SUM", -1, -32);
    assert.equal(result, -33);
  });

  it('should work with very large values', function() {
    const result = calculateNumber("SUM", Number.MAX_SAFE_INTEGER, 0.2);
    assert.equal(result, Number.MAX_SAFE_INTEGER);
  });
});

describe('The calculateNumber function', function() {
  it('should round the numbers and return their difference when using \
  "SUBTRACT" as the first argument', function() {
    const result = calculateNumber("SUBTRACT", 1.5, 2.3);
    assert.equal(result, 0);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUBTRACT", 1.5, 2);
    assert.equal(result, 0);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUBTRACT", 1, 2.5);
    assert.equal(result, -2);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUBTRACT", 1.1, 2);
    assert.equal(result, -1);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUBTRACT", 1, 2.1);
    assert.equal(result, -1);
  });

  it('should work with integer values', function() {
    const result = calculateNumber("SUBTRACT", 1, 4);
    assert.equal(result, -3);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber("SUBTRACT", 0, 0);
    assert.equal(result, 0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("SUBTRACT", -1, -32);
    assert.equal(result, 31);
  });

  it('should work with very large values', function() {
    const result = calculateNumber("SUBTRACT", Number.MAX_SAFE_INTEGER, 0.2);
    assert.equal(result, Number.MAX_SAFE_INTEGER);
  });
});

describe('The calculateNumber function', function() {
  it('should round the numbers and return their division when using "DIVIDE" \
  as the first argument', function() {
    const result = calculateNumber("DIVIDE", 1.5, 2.3);
    assert.equal(result, 1.0);
  });

  it('should round first number', function() {
    const result = calculateNumber("DIVIDE", 8.3, 2);
    assert.equal(result, 4.0);
  });

  it('should round second number', function() {
    const result = calculateNumber("DIVIDE", 1, 2.5);
    assert.equal(result, 1 / 3);
  });

  it('should round first number', function() {
    const result = calculateNumber("DIVIDE", 1.1, 2);
    assert.equal(result, 0.5);
  });

  it('should round second number', function() {
    const result = calculateNumber("DIVIDE", 1, 2.1);
    assert.equal(result, 0.5);
  });

  it('should work with integer values', function() {
    const result = calculateNumber("DIVIDE", 1, 4);
    assert.equal(result, 0.25);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber("DIVIDE", 0, 0);
    assert.equal(result, "Error");
  });

  it('should work with negative values', function() {
    const result = calculateNumber("DIVIDE", -16.2, -7.9);
    assert.equal(result, 2.0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("DIVIDE", -16.2, 7.9);
    assert.equal(result, -2.0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("DIVIDE", 16.2, -7.9);
    assert.equal(result, -2.0);
  });

  it('should work with very large values', function() {
    const result = calculateNumber("DIVIDE", Number.MAX_SAFE_INTEGER, 0.9);
    assert.equal(result, Number.MAX_SAFE_INTEGER);
  });
});