/**
 * 异步替换字符串中所有匹配的模式。
 * @param {string|RegExp} pattern - 要匹配的字符串或正则表达式。
 * @param {string|function} asyncReplacer - 用于替换的字符串或函数。
 * @returns {Promise<string>} 返回一个新的字符串，其中所有匹配的部分都被替换。
 * @throws {TypeError} 如果`asyncReplacer`不是函数或字符串，将抛出错误。
 * @throws {TypeError} 如果`pattern`不是字符串或正则表达式，将抛出错误。
 * @throws {TypeError} 如果`pattern`是一个没有全局标志的正则表达式，将抛出错误。
 */
String.prototype.asyncReplaceAll = async function (pattern, asyncReplacer) {
  // 如果替换器是字符串，则直接使用内置的replace方法
  if (typeof asyncReplacer === "string") {
    return this.replace(pattern, asyncReplacer);
  }
  // 如果替换器不是函数，则抛出错误
  if (typeof asyncReplacer !== "function") {
    throw new TypeError("The second argument must be a function or a string.");
  }
  let reg;
  // 如果模式是字符串，则创建一个新的正则表达式
  if (typeof pattern === "string") {
    reg = new RegExp(pattern.replace(/[.*+\-?^${}()|[\]\\]/g, "\\$&"), "g");
  }
  // 如果模式是正则表达式，但没有全局标志，则抛出错误
  else if (pattern instanceof RegExp) {
    if (!pattern.global) {
      throw new TypeError("The pattern RegExp must have the global flag set.");
    }
    reg = new RegExp(pattern);
  }
  // 如果模式既不是字符串也不是正则表达式，则抛出错误
  else {
    throw new TypeError("The pattern must be a string or a RegExp.");
  }
  // 初始化结果数组
  const result = [];
  let match;
  let lastIndex = 0;
  // 循环查找匹配的部分，并将其替换
  while ((match = reg.exec(this)) !== null) {
    const item = asyncReplacer(match[0]);
    const prefix = this.slice(lastIndex, match.index);
    lastIndex = match.index + match[0].length;
    result.push(prefix, item);
  }
  // 将剩余的部分添加到结果数组
  result.push(this.slice(lastIndex));
  // 等待所有的替换操作完成，然后将结果数组连接成一个字符串
  return (await Promise.all(result)).join("");
};
