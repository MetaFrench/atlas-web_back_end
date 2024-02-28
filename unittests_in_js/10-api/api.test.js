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

describe('Available payments endpoint', function () {
  it('should return the correct status code and result', function (done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});


describe('Login endpoint', function () {
  it('should return the correct status code and result', function (done) {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: true,
      body: { userName: 'Betty' }
    };
    request(options, function (error, response, body) {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});