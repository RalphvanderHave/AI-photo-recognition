<template>
  <nav class="nav">
    <RouterLink to="/" class="nav-brand">Dashboard Portal</RouterLink>
    <div class="nav-links">
      <RouterLink to="/" class="nav-link">Home</RouterLink>
      <RouterLink to="/dashboard" class="nav-link">Dashboard</RouterLink>
      <RouterLink to="/photo-analysis" class="nav-link">Photo Analysis</RouterLink>
    </div>
  </nav>
</template>

<style scoped>
.nav {
  background-color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-brand {
  font-size: 1.5rem;
  color: var(--primary-color);
  text-decoration: none;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-link {
  color: var(--secondary-color);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: var(--background-color);
}

.router-link-active {
  color: var(--primary-color);
  font-weight: bold;
}
</style> 