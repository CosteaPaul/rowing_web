<template>
  <div class='layout'>
  <Layout>
    <Header>
    </Header>
    <Content>
      <table style="width:100%">
        <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
        </colgroup>
        <tr>
      <td>
      <Scroll>
        <Card style="width:100%">
          <p slot="title">
                Available boats
          </p>
          <div v-for="boat_type in boat_types">
            <img :src = "getImgUrl(boat_type.img)"/>
            <table class="hoverTable" width="100%">
              <tr v-for="boat in boats" v-if="boat.type === boat_type.type" width="100%">
                <td>{{ boat.name }}</td>
              </tr>
            </table>
          </div>
        </Card>
      </Scroll>
    </td>
    <td>
      <div style="text-align:center">
        Buttons
      </div>
    </td>
    <td>
    <Scroll>
      <Card style="width:100%">
        <p slot="title">
              On the water
        </p>
        <div v-for="boat_type in boat_types">
          <img :src = "getImgUrl(boat_type.img)"/>
          <table class="hoverTable" width="100%">
            <tr v-for="boat in boats" v-if="boat.type === boat_type.type" width="100%">
              <td>{{ boat.name }}</td>
            </tr>
          </table>
        </div>
      </Card>
    </Scroll>
    </td>
    </tr></table>
    </Content>
    <Footer>
      <Card style="width:100%">
      <a href="https://www.accuweather.com/en/us/new-york-ny/10007/current-weather/349727" class="aw-widget-legal">
      </a><div id="awtd1535057240168" class="aw-widget-36hour"  data-locationkey="" data-unit="c" data-language="en-us" data-useip="true" data-uid="awtd1535057240168" data-editlocation="true"></div>
      </Card>
      <img src="https://www.hvz.baden-wuerttemberg.de/gifs/09021-140.GIF" style="max-width:1000px; max-height: 1000px;"/>
    </Footer>
  </Layout>
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
      boat_types: [
        {type:'1x', img:'1.png'},
        {type:'2x', img:'2x.png'},
        {type:'4x', img:'4x.png'}
      ],
      boats: [
          { type: '1x', name: "Max" },
          { type: '1x', name: "Fischerboot" },
          { type: '1x', name: "Jakob" },
          { type: '1x', name: "Frishling" },
          { type: '1x', name: "Klusi" },
          { type: '2x', name: "Wild thing" },
          { type: '2x', name: "Rudolph Wild" },
          { type: '2x', name: "Wild II" },
          { type: '4x', name: "Warstiner" },
          { type: '4x', name: "Cambridge" },
          { type: '4x', name: "Heidelberg"}
        ]
      }
    },
    mounted() {
      let recaptchaScript = document.createElement('script')
      recaptchaScript.setAttribute('src', 'https://oap.accuweather.com/launch.js')
      document.head.appendChild(recaptchaScript)
    },
    methods: {
      getImgUrl: function(boat) {
        return require('../assets/'+boat)
      }
    }
}
</script>

<style>
  .hoverTable tr:hover {
    background: #ffff99;
  }

  img {
    max-width: 100px;
    max-height: 200px;
  }
</style>
