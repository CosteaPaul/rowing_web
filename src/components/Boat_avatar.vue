<template>
  <div>
  <Card style="width:20%">
    <p slot="title">
          {{title}}
    </p>
    <img src="../assets/1.png"/>
    <table class="hoverTable" width="100%">
      <tr v-for="boat in boats" width="100%">
        <td>{{ boat.name }}</td>
      </tr>
    </table>
    <img src="../assets/2x.png"/>
    <table class="hoverTable" width="100%">
      <tr v-for="boat in boats" width="100%">
        <td>{{ boat.name }}</td>
      </tr>
    </table>
  </Card>
  <a href="https://www.accuweather.com/en/us/new-york-ny/10007/current-weather/349727" class="aw-widget-legal">
  </a><div id="awtd1535057240168" class="aw-widget-36hour"  data-locationkey="" data-unit="c" data-language="en-us" data-useip="true" data-uid="awtd1535057240168" data-editlocation="true"></div>
  </div>
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
    },
    mounted() {
      let recaptchaScript = document.createElement('script')
      recaptchaScript.setAttribute('src', 'https://oap.accuweather.com/launch.js')
      document.head.appendChild(recaptchaScript)
    }
}
</script>

<style>
  .hoverTable tr:hover {
    background: #ffff99;
  }

  img {
    max-width: 80px;
    max-height: 200px;
  }
</style>
