<template>
  <div id="app">
    <Boat_avatar title="Available boats"/>
    <Login/>
  </div>
</template>

<script>
import Login from './components/Login'
import Boat_avatar from './components/Boat_avatar'

export default {
  name: 'App',
  components: {
    Login,
    Boat_avatar
  }
}
</script>

<style>

</style>
