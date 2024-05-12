<template>
    <div class="MacbookAirLight" :style="{ width: '1280px', height: '832px', position: 'relative', background: 'white' }">
      <div class="Header" :style="{ width: '646px', height: '329px', left: '7px', top: '13px', position: 'absolute' }">
        <!-- Nested divs with styles converted to Vue's :style binding -->
        <div class="Rectangle1" :style="styles.rectangle1"></div>
        <div class="Rectangle2" :style="styles.rectangle2"></div>
        <div class="Rectangle3" :style="styles.rectangle3"></div>
        <div class="Rectangle4" :style="styles.rectangle4"></div>
        <div class="ArtHistory" :style="styles.artHistory">ART HISTORY</div>
      </div>
      <!-- Repeat for other nested components with respective styles -->
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        styles: {
          rectangle1: {
            width: '621px',
            height: '329px',
            position: 'absolute',
            background: '#322C2C'
          },
          rectangle2: {
            width: '596.77px',
            height: '305.66px',
            left: '11px',
            top: '12.30px',
            position: 'absolute',
            background: '#FFFAFA'
          },
          rectangle3: {
            width: '579.35px',
            height: '285.79px',
            left: '20.17px',
            top: '21.77px',
            position: 'absolute',
            background: '#322C2C'
          },
          rectangle4: {
            width: '557px',
            height: '263px',
            left: '31px',
            top: '32px',
            position: 'absolute',
            background: '#FFFAFA'
          },
          artHistory: {
            width: '614.41px',
            height: '285.59px',
            left: '31.59px',
            top: '14.82px',
            position: 'absolute',
            color: '#322C2C',
            fontSize: '128px',
            fontWeight: '700',
            lineHeight: '150.74px',
            letterSpacing: '3.84px',
            wordWrap: 'break-word'
          }
        }
      };
    }
  };
  </script>
  
  <style scoped>
  /* Scoped CSS styles */
  .MacbookAirLight {
    /* additional styles if needed */
  }
  .Header {
    /* additional styles if needed */
  }
  </style>
  