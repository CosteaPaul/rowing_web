<template>
  <Card style="width:30%">
    <p slot="title">
          {{title}}
    </p>
    <p v-for="boat in boats">
      <Avatar/>
      {{ boat.name }}
    </p>
  </Card>
</template>

<script>
export default {
  name: 'Boat_avatar',
  props: {
    title: {
      type: String,
      default: "No title"
    }
  },
  data () {
    return {
      boats: [
          { type: 'Foo', name: "Max" },
          { type: 'Bar', name: "Heidelberg"}
        ]
      }
    }
}
</script>

<style>
</style>
