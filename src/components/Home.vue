<template>
  <div class="home">
    <h2>Welcome to Dashboard Portal</h2>
    <p class="welcome-text">
      Access our analytics tools and AI services
    </p>
    <div class="features">
      <div class="feature-card">
        <h3>Power BI Analytics</h3>
        <p>View detailed analytics and insights through our Power BI integration</p>
        <RouterLink to="/dashboard" class="cta-button">View Dashboard</RouterLink>
      </div>
      <div class="feature-card">
        <h3>Photo Analysis</h3>
        <p>Upload and analyze photos with our AI model</p>
        <RouterLink to="/photo-analysis" class="cta-button">Try It Now</RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 40px 20px;
}

.welcome-text {
  font-size: 1.2rem;
  color: var(--secondary-color);
  margin-bottom: 40px;
}

.features {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 40px;
}

.feature-card {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
}

.cta-button {
  display: inline-block;
  background-color: var(--primary-color);
  color: white;
  padding: 12px 24px;
  border-radius: 6px;
  text-decoration: none;
  margin-top: 20px;
  transition: background-color 0.3s;
}

.cta-button:hover {
  background-color: #3aa876;
}
</style> 