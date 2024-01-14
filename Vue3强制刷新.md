## 需求
Vue3中实现类似Vue2中$forceUpdate()的强制刷新


## 方案
使用 key 属性来强制重新渲染组件。通过更新 key 值，Vue 会认为这是一个新的组件实例，从而触发强制刷新的效果。

```vue
<template>
  <div>
    <button @click="updateKey">刷新组件</button>
    <p :key="componentKey">{{ data }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const componentKey = ref(0)
const data = ref('Initial Value')

const updateKey = () => {
  // 更新 key 值，触发重新渲染
  componentKey.value++
}
</script>
```

---
- [Vue3中实现类似Vue2中$forceUpdate()的强制刷新 - 掘金](https://juejin.cn/post/7257307209720807482)
