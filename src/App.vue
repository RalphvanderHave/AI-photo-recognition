<template>
  <div class="app">
    <Navigation />
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import Navigation from './components/Navigation.vue'
</script>

<style scoped>
.app {
  min-height: 100vh;
  background-color: var(--background-color);
}

main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
</style> 