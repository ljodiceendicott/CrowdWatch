<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div> -->

    <h1>Inventory System</h1>
  </header>

  <main>
    
    <!-- <TheWelcome /> -->
    <h3>Items</h3>
    Item Name
    Item #:
    <div>
    <button>
      Previous Item</button>
    <button @click='log'>Next Item</button>
    </div>
  </main>
  <div>
  <button>Add Item</button>
  <button>Delete Item</button>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
h1{
  text-align: center;
}
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  main {
    margin : 0 auto;
    text-align: center;
  }
}
</style>
