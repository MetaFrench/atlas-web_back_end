const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('The calculateNumber function', function () {
  it('should return an error if the first argument is incorrect', function () {
    expect(calculateNumber("TEST", 1.5, 2.0)).to.equal("Error");
  });

  it('should return an error if the first argument is not capitalized correctly', function () {
    expect(calculateNumber("Sum", 1.5, 2.0)).to.equal("Error");
  });

  it('should return an error if the first argument is not a string', function () {
    expect(calculateNumber(1, 1.5, 2.0)).to.equal("Error");
  });
});

describe('The calculateNumber function', function() {
  it('should round the numbers and return their sum when using "SUM" as the first argument', function() {
    const result = calculateNumber("SUM", 1.5, 2.3);
    expect(result).to.equal(4);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUM", 1.5, 2);
    expect(result).to.equal(4);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUM", 1, 2.5);
    expect(result).to.equal(4);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUM", 1.1, 2);
    expect(result).to.equal(3);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUM", 1, 2.1);
    expect(result).to.equal(3);
  });

  it('should work with integer values', function() {
    const result = calculateNumber("SUM", 1, 4);
    expect(result).to.equal(5);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber("SUM", 0, 0);
    expect(result).to.equal(0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("SUM", -1, -32);
    expect(result).to.equal(-33);
  });

  it('should work with very large values', function() {
    const result = calculateNumber("SUM", Number.MAX_SAFE_INTEGER, 0.2);
    expect(result).to.equal(Number.MAX_SAFE_INTEGER);
  });
});

describe('The calculateNumber function', function() {
  it('should round the numbers and return their difference when using \
  "SUBTRACT" as the first argument', function() {
    const result = calculateNumber("SUBTRACT", 1.5, 2.3);
    expect(result).to.equal(0);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUBTRACT", 1.5, 2);
    expect(result).to.equal(0);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUBTRACT", 1, 2.5);
    expect(result).to.equal(-2);
  });

  it('should round first number', function() {
    const result = calculateNumber("SUBTRACT", 1.1, 2);
    expect(result).to.equal(-1);
  });

  it('should round second number', function() {
    const result = calculateNumber("SUBTRACT", 1, 2.1);
    expect(result).to.equal(-1);
  });

  it('should work with integer values', function() {
    const result = calculateNumber("SUBTRACT", 1, 4);
    expect(result).to.equal(-3);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber("SUBTRACT", 0, 0);
    expect(result).to.equal(0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("SUBTRACT", -1, -32);
    expect(result).to.equal(31);
  });

  it('should work with very large values', function() {
    const result = calculateNumber("SUBTRACT", Number.MAX_SAFE_INTEGER, 0.2);
    expect(result).to.equal(Number.MAX_SAFE_INTEGER);
  });
});

describe('The calculateNumber function', function() {
  it('should round the numbers and return their division when using "DIVIDE" \
  as the first argument', function() {
    const result = calculateNumber("DIVIDE", 1.5, 2.3);
    expect(result).to.equal(1.0);
  });

  it('should round first number', function() {
    const result = calculateNumber("DIVIDE", 8.3, 2);
    expect(result).to.equal(4.0);
  });

  it('should round second number', function() {
    const result = calculateNumber("DIVIDE", 1, 2.5);
    expect(result).to.equal(1 / 3);
  });

  it('should round first number', function() {
    const result = calculateNumber("DIVIDE", 1.1, 2);
    expect(result).to.equal(0.5);
  });

  it('should round second number', function() {
    const result = calculateNumber("DIVIDE", 1, 2.1);
    expect(result).to.equal(0.5);
  });

  it('should work with integer values', function() {
    const result = calculateNumber("DIVIDE", 1, 4);
    expect(result).to.equal(0.25);
  });

  it('should work with 0 values', function() {
    const result = calculateNumber("DIVIDE", 0, 0);
    expect(result).to.equal("Error");
  });

  it('should work with negative values', function() {
    const result = calculateNumber("DIVIDE", -16.2, -7.9);
    expect(result).to.equal(2.0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("DIVIDE", -16.2, 7.9);
    expect(result).to.equal(-2.0);
  });

  it('should work with negative values', function() {
    const result = calculateNumber("DIVIDE", 16.2, -7.9);
    expect(result).to.equal(-2.0);
  });

  it('should work with very large values', function() {
    const result = calculateNumber("DIVIDE", Number.MAX_SAFE_INTEGER, 0.9);
    expect(result).to.equal(Number.MAX_SAFE_INTEGER);
  });
});