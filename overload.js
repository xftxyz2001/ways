/**
 * JS 实现函数重载
 * @returns {Function} overload
 * 
 * @example
 * const fn = createOverload();
 * fn.register('string', 'number', function (str, num) {
 *    console.log('string, number');
 * });
 * fn.register('number', 'string', function (num, str) {
 *   console.log('number, string');
 * });
 * fn.register('string', 'string', function (str1, str2) {
 *  console.log('string, string');
 * });
 * 
 * fn('string', 1); // string, number
 * fn(1, 'string'); // number, string
 * fn('string', 'string'); // string, string
 */
function createOverload() {
    const callMap = new Map();
    function overload(...args) {
        const key = args.map(arg => typeof arg).join(',');
        const fn = callMap.get(key);
        if (!fn) {
            throw new Error('no matching function');

        } return fn.apply(this, args);
    }
    overload.register = function (...args) {
        const fn = args.pop();
        if (typeof fn !== 'function') {
            throw new Error('last argument must be a function');
        }
        const types = args;
        callMap.set(types.join(','), fn);
    }
    return overload;
}

export default createOverload;
