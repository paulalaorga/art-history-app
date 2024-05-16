<template>
<div class="header">
    <div class="h-frame1"></div>
    <div class="h-frame2"></div>
    <div class="h-frame3"></div>
    <div class="h-frame4"></div>
    <b class="art-history">ART HISTORY</b>
  </div>
</template>

<script>
export default {
};
</script>

<style>
.header {
  position: absolute;
  top: 13px;
  left: 7px;
  width: 621px;
  height: 329px;
  flex: 1;
}
.h-frame1 {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: #322c2c;
  width: 100%;
  height: 100%;
}
.h-frame2 {
  position: absolute;
  top: calc(50% - 152.2px);
  left: 11px;
  background-color: #fffafa;
  width: 596.8px;
  height: 305.7px;
}
.h-frame3 {
  position: absolute;
  top: 21.77px;
  left: 20.17px;
  background-color: #322c2c;
  width: 579.4px;
  height: 285.8px;
}
.h-frame4 {
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
  width: 70%;
  height: auto;
  font-size: 118px;
}
</style>