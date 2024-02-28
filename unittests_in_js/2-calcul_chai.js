function calculateNumber(type, a, b) {
    // Rounds two numbers and returns the sum, difference, or division
    a = Math.round(a);
    b = Math.round(b);
  
    if (type !== "SUM" && type !== "SUBTRACT" && type !== "DIVIDE")
      return ("Error");
    if (typeof type !== "string")
      return ("Error");
  
    if (type === "SUM")
      return a + b;
    if (type === "SUBTRACT")
      return a - b;
    if (type === "DIVIDE") {
      if (b === 0)
        return ("Error");
      return a / b;
    }
  }
  
  module.exports = calculateNumber;