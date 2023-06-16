<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<style>
nav {
  background: #f1f1f1;
  padding: 10px;
  margin-bottom: 20px;
}

nav a {
  margin-right: 10px;
}
</style>
