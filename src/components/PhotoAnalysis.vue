<template>
  <div class="photo-analysis">
    <h2>Photo Analysis</h2>
    <p class="description">Upload your photo to analyze it with our AI model</p>

    <div class="upload-container">
      <div 
        class="drop-zone"
        @dragover.prevent
        @drop.prevent="handleDrop"
        :class="{ 'drag-over': isDragging }"
        @dragenter.prevent="isDragging = true"
        @dragleave.prevent="isDragging = false"
      >
        <div v-if="!selectedImage" class="upload-prompt">
          <span class="icon">📸</span>
          <p>Drag and drop your image here or</p>
          <label class="upload-button">
            Choose File
            <input 
              type="file" 
              accept="image/*" 
              @change="handleFileSelect" 
              class="hidden"
            >
          </label>
        </div>
        <div v-else class="preview">
          <img :src="imagePreview" alt="Preview" class="preview-image">
          <button class="remove-button" @click="removeImage">Remove</button>
        </div>
      </div>

      <div v-if="selectedImage" class="actions">
        <button 
          class="analyze-button"
          @click="analyzeImage"
          :disabled="isLoading"
        >
          {{ isLoading ? 'Analyzing...' : 'Analyze Image' }}
        </button>
      </div>

      <div v-if="result" class="result-container">
        <h3>Analysis Results</h3>
        <div class="result-card">
          <div class="predictions-grid">
            <div 
              v-for="(probability, label) in result.predicted_labels" 
              :key="label"
              class="prediction-item"
              :class="{ 'significant': probability > 5 }"
            >
              <span class="label">{{ formatLabel(label) }}:</span>
              <span class="probability">{{ probability.toFixed(1) }}%</span>
            </div>
          </div>
        </div>
      </div>

      <div v-if="error" class="error">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface AnalysisResult {
  predicted_labels: Record<string, number>
}

const selectedImage = ref<File | null>(null)
const imagePreview = ref<string>('')
const isDragging = ref(false)
const isLoading = ref(false)
const result = ref<AnalysisResult | null>(null)
const error = ref<string>('')

const handleFileSelect = (event: Event) => {
  const input = event.target as HTMLInputElement
  if (input.files && input.files[0]) {
    processFile(input.files[0])
  }
}

const handleDrop = (event: DragEvent) => {
  isDragging.value = false
  if (event.dataTransfer?.files && event.dataTransfer.files[0]) {
    processFile(event.dataTransfer.files[0])
  }
}

const processFile = (file: File) => {
  if (!file.type.startsWith('image/')) {
    error.value = 'Please upload an image file'
    return
  }
  
  selectedImage.value = file
  const reader = new FileReader()
  reader.onload = (e) => {
    imagePreview.value = e.target?.result as string
  }
  reader.readAsDataURL(file)
  error.value = ''
  result.value = null
}

const removeImage = () => {
  selectedImage.value = null
  imagePreview.value = ''
  result.value = null
  error.value = ''
}

const formatLabel = (label: string): string => {
  return label.replace('_', ' ')
}

const analyzeImage = async () => {
  if (!selectedImage.value) return

  isLoading.value = true
  error.value = ''
  result.value = null

  try {
    const formData = new FormData()
    formData.append('file', selectedImage.value)

    const response = await fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData
    })

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`)
    }

    const data = await response.json()
    
    // Validate the response
    if (!data.predicted_labels || typeof data.predicted_labels !== 'object') {
      throw new Error('Invalid response format')
    }

    result.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'An error occurred during analysis'
    result.value = null
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.photo-analysis {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.description {
  text-align: center;
  margin-bottom: 30px;
}

.upload-container {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.drop-zone {
  border: 2px dashed var(--primary-color);
  border-radius: 8px;
  padding: 40px;
  text-align: center;
  transition: all 0.3s ease;
  background: var(--background-color);
}

.drag-over {
  background: #e8f5e9;
  border-color: #2e7d32;
}

.upload-prompt {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.icon {
  font-size: 48px;
}

.upload-button {
  background: var(--primary-color);
  color: white;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.upload-button:hover {
  background-color: #3aa876;
}

.hidden {
  display: none;
}

.preview {
  position: relative;
}

.preview-image {
  max-width: 100%;
  max-height: 400px;
  border-radius: 4px;
}

.remove-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.actions {
  margin-top: 20px;
  text-align: center;
}

.analyze-button {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1em;
  transition: background-color 0.3s;
}

.analyze-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.result-container {
  margin-top: 30px;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.result-card {
  padding: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  background: #f8f9fa;
}

.predictions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
  padding: 10px;
}

.prediction-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 15px;
  background: white;
  border-radius: 4px;
  border: 1px solid #e0e0e0;
  transition: all 0.3s ease;
}

.prediction-item.significant {
  background-color: #e8f5e9;
  border-color: #81c784;
  font-weight: bold;
}

.label {
  color: var(--secondary-color);
}

.probability {
  font-family: monospace;
  color: #2e7d32;
}

.error {
  margin-top: 20px;
  padding: 15px;
  background-color: #ffebee;
  color: #c62828;
  border-radius: 6px;
  text-align: center;
  border: 1px solid #ffcdd2;
}
</style> 