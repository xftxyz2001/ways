import { computed } from "vue";

/**
 * 自定义钩子，用于创建一个带有缓存功能的计算属性。
 * @param {Function} fn - 用于计算结果的函数。
 * @returns {Function} - 返回一个新的函数，该函数接受任意数量的参数，并尝试从缓存中获取结果。如果缓存中没有结果，它会计算结果并将其存入缓存。
 */
export function useComputed(fn) {
  const cache = new Map();

  /**
   * 比较两个参数数组是否相等。
   * @param {Array} args1 - 第一个参数数组。
   * @param {Array} args2 - 第二个参数数组。
   * @returns {boolean} - 如果两个参数数组相等，返回 true，否则返回 false。
   */
  function compare(args1, args2) {
    return (
      args1.length === args2.length &&
      args1.every((arg, index) => Object.is(arg, args2[index]))
    );
  }

  /**
   * 从缓存中获取结果。
   * @param {Array} args - 用于获取结果的参数数组。
   * @returns {any} - 返回缓存中的结果，如果没有找到结果，返回 undefined。
   */
  function getCache(args) {
    const keys = [...cache.keys()];
    const key = keys.find((key) => compare(key, args));
    if (key) {
      return cache.get(key);
    }
  }

  return function (...args) {
    const cachedResult = getCache(args);
    if (cachedResult) {
      return cachedResult.value;
    }
    const result = computed(() => fn(...args));
    cache.set(args, result);
    return result.value;
  };
}
