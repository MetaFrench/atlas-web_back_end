const { expect } = require('chai');
const sinon = require("sinon")
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  it('should use Utils.calculateNumber to calculate the total', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;
    spy.restore();
  });

  it('should log the correct output to the console', function () {
    const consoleSpy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    result = Utils.calculateNumber('SUM', 100, 20);
    expect(consoleSpy.calledWith(`The total is: ${result}`)).to.be.true;
    consoleSpy.restore();
  });

  it('should handle the result of Utils.calculateNumber correctly', function () {
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber');
    calculateNumberStub.returns(10);

    const consoleSpy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWith("The total is: 10")).to.be.true;
    calculateNumberStub.restore();
    consoleSpy.restore();
  });
});