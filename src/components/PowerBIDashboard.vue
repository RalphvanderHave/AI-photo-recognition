<template>
  <div class="dashboard-container">
    <h2>Power BI Dashboard</h2>
    <div class="dashboard-frame">
      <!-- Power BI embed -->
      <iframe
        :src="dashboardUrl"
        frameborder="0"
        allowFullScreen="true"
      ></iframe>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

//  Power BI embed URL
const dashboardUrl = ref('https://app.powerbi.com/view?r=eyJrIjoiNDBkMTcwYTUtMDZkYy00NGVhLTliZjYtMjM3NmEyOGM2MDFmIiwidCI6ImEyNTg2YjliLWY4NjctNGIzYy05MzYzLTViNDM1YzVkYmM0NSIsImMiOjh9')
</script>

<style scoped>
.dashboard-container {
  width: 100%;
  padding: 20px;
}

.dashboard-frame {
  width: 100%;
  height: 700px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

iframe {
  width: 100%;
  height: 100%;
}

h2 {
  margin-bottom: 20px;
  color: #2c3e50;
}
</style> 