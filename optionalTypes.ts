/**
 * 将类型 T 中的 K 属性设置为可选的。
 */
export type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

/**
 * 获取类型 T 中的可选属性。
 */
export type GetOptional<T> = {
  [P in keyof T as T[P] extends Required<T>[P] ? never : P]: T[P];
};
