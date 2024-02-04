import { ref, Ref } from "vue";

/**
 * 创建一个引用（Ref）到给定组件的实例。
 *
 * @param _comp 一个组件的构造函数。
 * @returns 一个 Ref 对象，其值为给定组件的实例，如果组件尚未实例化，则为 undefined。
 */
export function useCompRef<T extends abstract new (...args: any) => any>(
  _comp: T
): Ref<InstanceType<T> | undefined> {
  return ref<InstanceType<T>>();
}

// import { ElForm } from "element-plus";
// const formRef = useCompRef(ElForm);
// formRef.value?.validate();
