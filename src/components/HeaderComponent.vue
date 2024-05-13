<template>
  <div class="macbook-air-light">
    <div class="header">
      <div class="header-child"></div>
      <div class="header-item"></div>
      <div class="header-inner"></div>
      <div class="rectangle-div"></div>
      <b class="art-history">ART HISTORY</b>
    </div>
    <div class="frame">
      <div class="frame-child"></div>
      <div class="frame-item"></div>
      <div class="frame-inner"></div>
    <v-timeline>
      <v-timeline-item class="classicism-group">
        <template v-slot:icon>
          <b class="classicism">CLASSICISM</b>
          <div class="year">
            <b class="bc">500 BC</b>
          </div>
        </template>
      </v-timeline-item>
      </v-timeline>
    </div>
  </div>
</template>




<script>  
  
  export default {
      name: "HeaderComponent"}

</script>

<style scoped>

      .header-child {
      position: absolute;
      top: 0px;
      left: 0px;
      background-color: #322c2c;
      width: 621px;
      height: 329px;
  }
      .header-item {
          position: absolute;
          top: calc(50% - 152.2px);
          left: 11px;
          background-color: #fffafa;
          width: 596.8px;
          height: 305.7px;
      }
      .header-inner {
          position: absolute;
          top: 21.77px;
          left: 20.17px;
          background-color: #322c2c;
          width: 579.4px;
          height: 285.8px;
      }
      .rectangle-div {
          position: absolute;
          top: calc(50% - 132.5px);
          left: 31px;
          background-color: #fffafa;
          width: 557px;
          height: 263px;
      }
      .art-history {
          position: absolute;
          top: 23px;
          left: 31px;
          letter-spacing: 0.03em;
          line-height: 117.77%;
          display: inline-block;
          width: 557px;
          height: 263px;
      }
      .header {
          position: absolute;
          top: 13px;
          left: 7px;
          width: 621px;
          height: 329px;
          font-size: 128px;
      }
      .frame-child {
          position: absolute;
          top: 0px;
          left: 0px;
          background-color: #322c2c;
          width: 642px;
          height: 832px;
      }
      .frame-item {
          position: absolute;
          top: calc(50% - 403px);
          left: 21.62px;
          background-color: #fffafa;
          width: 603.1px;
          height: 805px;
      }
      .frame-inner {
          position: absolute;
          top: 23px;
          left: 33.51px;
          background-color: #322c2c;
          width: 578.2px;
          height: 782px;
      }
      .frame {
          position: absolute;
          top: 0px;
          left: 638px;
          width: 642px;
          height: 832px;
      }
      .classicism-t-child {
          position: absolute;
          top: calc(50% - 46px);
          left: 0px;
          background-color: #fffafa;
          border: 6px solid #322c2c;
          box-sizing: border-box;
          width: 272px;
          height: 92px;
      }
      .xx-century {
          position: absolute;
          top: 28px;
          left: 13px;
          line-height: 117.77%;
          display: inline-block;
          width: 240px;
          height: 49px;
      }
      .classicism-group {
          position: absolute;
          top: calc(50% - 46px);
          left: 0px;
          width: 272px;
          height: 92px;
      }
      .th-century {
          position: absolute;
          top: calc(50% + 222px);
          left: 701px;
          width: 272px;
          height: 92px;
      }
      .xix-century {
          position: absolute;
          top: 23px;
          left: 18px;
          letter-spacing: -0.03em;
          line-height: 117.77%;
          display: inline-block;
          width: 240px;
          height: 49px;
      }
      .th-century1 {
          position: absolute;
          top: calc(50% + 78px);
          left: 701px;
          width: 272px;
          height: 92px;
      }
      .neoclassicism {
          position: absolute;
          top: 23px;
          left: 7px;
          letter-spacing: -0.11em;
          line-height: 117.77%;
          display: inline-block;
          width: 270px;
          height: 47px;
      }
      .classicism-group2 {
          position: absolute;
          top: calc(50% - 46px);
          left: 0px;
          width: 277px;
          height: 92px;
      }
      .neoclassicism-t {
          position: absolute;
          top: calc(50% - 66px);
          left: 701px;
          width: 277px;
          height: 92px;
      }
      .medieval {
          position: absolute;
          top: 22px;
          left: 16px;
          letter-spacing: 0.14em;
          line-height: 117.77%;
          display: inline-block;
          width: 237px;
          height: 44px;
      }
      .medieval-t {
          position: absolute;
          top: calc(50% - 210px);
          left: 701px;
          width: 272px;
          height: 92px;
      }
      .classicism {
          position: absolute;
          top: 22px;
          left: 18px;
          letter-spacing: -0.01em;
          line-height: 117.77%;
          display: inline-block;
          width: 240px;
          height: 49px;
      }
      .classicism-t4 {
          position: absolute;
          top: calc(50% - 354px);
          left: 701px;
          width: 272px;
          height: 92px;
      }
      .year-child {
          position: absolute;
          top: -3px;
          left: -3px;
          border-radius: 50%;
          background-color: #fffafa;
          border: 6px solid #322c2c;
          box-sizing: border-box;
          width: 50px;
          height: 50px;
      }
      .bc {
          position: absolute;
          top: 4px;
          left: 82px;
          letter-spacing: -0.1em;
          line-height: 117.77%;
          display: inline-block;
          width: 179px;
          height: 40px;
      }
      .year {
          position: absolute;
          top: 89px;
          left: 1009px;
          width: 261px;
          height: 44px;
          font-size: 32px;
          color: #fffafa;
      }
      .ac {
          position: absolute;
          top: 4px;
          left: 82px;
          letter-spacing: -0.1em;
          line-height: 117.77%;
          display: inline-block;
          width: 117px;
          height: 40px;
      }
      .year1 {
          position: absolute;
          top: 228px;
          left: 1009px;
          width: 199px;
          height: 44px;
          font-size: 32px;
          color: #fffafa;
      }
      .ac1 {
          position: absolute;
          top: 0px;
          left: 82px;
          letter-spacing: -0.1em;
          line-height: 117.77%;
          display: inline-block;
          width: 124px;
          height: 40px;
      }
      .year2 {
          position: absolute;
          top: 376px;
          left: 1009px;
          width: 206px;
          height: 44px;
          font-size: 32px;
          color: #fffafa;
      }
      .ac2 {
          position: absolute;
          top: 4px;
          left: 82px;
          letter-spacing: -0.1em;
          line-height: 117.77%;
          display: inline-block;
          width: 111px;
          height: 40px;
      }
      .year3 {
          position: absolute;
          top: 517px;
          left: 1009px;
          width: 193px;
          height: 44px;
          font-size: 32px;
          color: #fffafa;
      }
      .year4 {
          position: absolute;
          top: 659px;
          left: 1009px;
          width: 261px;
          height: 44px;
          font-size: 32px;
          color: #fffafa;
      }
      /* .macbook-air-light-child {
          position: absolute;
          top: 20px;
          left: 1026px;
          width: 5px;
          height: 792px;
          object-fit: contain;
      } */
       .image-2-icon {
width: 792.02px;
height: 0px;
top: 20px;
left: 1026px;
gap: 0px;
border: 10px 0px 0px 0px;
opacity: 0px;
angle: -89.64 deg;
border: 10px solid #FFFFFF
      } 
      .macbook-air-light {
          width: 100%;
          position: relative;
          background-color: #fff;
          height: 832px;
          overflow: hidden;
          text-align: left;
          font-size: 40px;
          color: #322c2c;
          font-family: Roboto;
      }
  
  </style>