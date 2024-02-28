const { expect } = require('chai');
const request = require('request');

describe('Index page', function () {
  it('should return the correct status code and result', function (done) {
    request('http://localhost:7865', function (error, response, body) {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  it('should return the correct status code and result', function (done) {
    request('http://localhost:7865/cart/12', function (error, response, body) {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal(`Payment methods for cart 12`);
      done();
    });
  });

  it('should return the correct status code and result', function (done) {
    request('http://localhost:7865/cart/test', function (error, response, body) {
      if (error) return done(error);
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});