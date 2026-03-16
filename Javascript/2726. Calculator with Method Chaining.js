class Calculator {
  /**
   * @param {number} value
   */
  constructor(value) {
    this.curr = value;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  add(value) {
    this.curr += value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  subtract(value) {
    this.curr -= value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  multiply(value) {
    this.curr *= value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  divide(value) {
    if (value === 0) {
      throw "Division by zero is not allowed";
    }
    this.curr /= value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  power(value) {
    this.curr **= value;
    return this;
  }

  /**
   * @return {number}
   */
  getResult() {
    return this.curr;
  }
}
