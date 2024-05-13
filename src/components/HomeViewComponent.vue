<template>
  <div class="macbook-air-LIGHT">
    <div class="overlap">
      <div class="overlap-group">
        <div :class="['HEADER', HEADERClassName]">
          <div class="div">
            <div class="rectangle" />
            <div class="rectangle-2" />
            <div class="rectangle-3" />
            <div class="rectangle-4" />
            <div class="text-wrapper">ART HISTORY</div>
          </div>
        </div>
        <div class="FRAME">
          <div class="rectangle-wrapper">
            <div class="rectangle-5" />
          </div>
        </div>
        <div class="element-CENTURY">
          <div class="CLASSICISM-GROUP">
            <div class="CLASSICISM-t">
              <div class="div-wrapper">
                <div class="text-wrapper-2">XX CENTURY</div>
              </div>
            </div>
          </div>
        </div>
        <div class="element-th-CENTURY">
          <div class="CLASSICISM-GROUP">
            <div class="CLASSICISM-t">
              <div class="div-wrapper">
                <div class="text-wrapper-3">XIX CENTURY</div>
              </div>
            </div>
          </div>
        </div>
        <div class="NEOCLASSICISM-t">
          <div class="CLASSICISM-GROUP">
            <div class="overlap-group-wrapper">
              <div class="overlap-group-2">
                <div class="rectangle-6" />
                <div class="text-wrapper-4">NEOCLASSICISM</div>
              </div>
            </div>
          </div>
        </div>
        <div class="MEDIEVAL-t">
          <div class="CLASSICISM-GROUP">
            <div class="CLASSICISM-t">
              <div class="div-wrapper">
                <div class="text-wrapper-5">MEDIEVAL</div>
              </div>
            </div>
          </div>
        </div>
        <div class="CLASSICISM-GROUP-wrapper">
          <div class="CLASSICISM-GROUP">
            <div class="CLASSICISM-t">
              <div class="div-wrapper">
                <div class="text-wrapper-6">CLASSICISM</div>
              </div>
            </div>
          </div>
        </div>
        <div class="year">
          <div class="ellipse" />
          <div class="text-wrapper-7">500 BC</div>
        </div>
        <div class="year-2">
          <div class="ellipse" />
          <div class="text-wrapper-8">1400 AC</div>
        </div>
        <div class="year-3">
          <div class="ellipse" />
          <div class="text-wrapper-9">1800 AC</div>
        </div>
        <div class="year-4">
          <div class="ellipse" />
          <div class="text-wrapper-10">1900 AC</div>
        </div>
        <div class="year-5">
          <div class="ellipse" />
          <div class="text-wrapper-7">2000 AC</div>
        </div>
        <img class="line" alt="Line" src="line-1.svg" />
      </div>
      <img class="image" alt="Image" src="image-2.png" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "MacbookAirLight",
  props: {
    HEADERClassName: {
      type: String,
      default: "",
    },
  },
});
</script>

<style>
.macbook-air-LIGHT {
  background-color: #ffffff;
  height: 832px;
  width: 1280px;
}

.macbook-air-LIGHT .overlap {
  height: 832px;
  left: 7px;
  position: relative;
  width: 1273px;
}

.macbook-air-LIGHT .overlap-group {
  height: 832px;
  left: 0;
  position: absolute;
  top: 0;
  width: 1273px;
}

.macbook-air-LIGHT .HEADER {
  height: 329px;
  left: 0;
  position: absolute;
  top: 13px;
  width: 648px;
}

.macbook-air-LIGHT .div {
  height: 329px;
  position: relative;
  width: 646px;
}

.macbook-air-LIGHT .rectangle {
  background-color: #322c2c;
  height: 329px;
  left: 0;
  position: absolute;
  top: 0;
  width: 621px;
}

.macbook-air-LIGHT .rectangle-2 {
  background-color: #fffafa;
  height: 306px;
  left: 11px;
  position: absolute;
  top: 12px;
  width: 597px;
}

.macbook-air-LIGHT .rectangle-3 {
  background-color: #322c2c;
  height: 286px;
  left: 20px;
  position: absolute;
  top: 22px;
  width: 579px;
}

.macbook-air-LIGHT .rectangle-4 {
  background-color: #fffafa;
  height: 263px;
  left: 31px;
  position: absolute;
  top: 32px;
  width: 557px;
}

.macbook-air-LIGHT .text-wrapper {
  color: #322c2c;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 128px;
  font-weight: 700;
  left: 32px;
  letter-spacing: 3.84px;
  line-height: 150.7px;
  position: absolute;
  top: 15px;
  width: 614px;
}

.macbook-air-LIGHT .FRAME {
  background-color: #322c2c;
  height: 832px;
  left: 631px;
  position: absolute;
  top: 0;
  width: 642px;
}

.macbook-air-LIGHT .rectangle-wrapper {
  background-color: #fffafa;
  height: 805px;
  left: 22px;
  position: relative;
  top: 13px;
  width: 603px;
}

.macbook-air-LIGHT .rectangle-5 {
  background-color: #322c2c;
  height: 782px;
  left: 12px;
  position: relative;
  top: 10px;
  width: 578px;
}

.macbook-air-LIGHT .element-CENTURY {
  height: 92px;
  left: 694px;
  position: absolute;
  top: 638px;
  width: 272px;
}

.macbook-air-LIGHT .CLASSICISM-GROUP {
  height: 92px;
}

.macbook-air-LIGHT .CLASSICISM-t {
  height: 92px;
  width: 274px;
}

.macbook-air-LIGHT .div-wrapper {
  background-color: #fffafa;
  border: 6px solid;
  border-color: #322c2c;
  height: 92px;
  position: relative;
  width: 272px;
}

.macbook-air-LIGHT .text-wrapper-2 {
  color: #322c2c;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 40px;
  font-weight: 700;
  left: 7px;
  letter-spacing: 0;
  line-height: 47.1px;
  position: absolute;
  top: 22px;
  white-space: nowrap;
  width: 240px;
}

.macbook-air-LIGHT .element-th-CENTURY {
  height: 92px;
  left: 694px;
  position: absolute;
  top: 494px;
  width: 272px;
}

.macbook-air-LIGHT .text-wrapper-3 {
  color: #322c2c;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 40px;
  font-weight: 700;
  left: 12px;
  letter-spacing: -1.2px;
  line-height: 47.1px;
  position: absolute;
  top: 17px;
  white-space: nowrap;
  width: 240px;
}

.macbook-air-LIGHT .NEOCLASSICISM-t {
  height: 92px;
  left: 694px;
  position: absolute;
  top: 350px;
  width: 277px;
}

.macbook-air-LIGHT .overlap-group-wrapper {
  height: 92px;
  width: 279px;
}

.macbook-air-LIGHT .overlap-group-2 {
  height: 92px;
  position: relative;
  width: 277px;
}

.macbook-air-LIGHT .rectangle-6 {
  background-color: #fffafa;
  border: 6px solid;
  border-color: #322c2c;
  height: 92px;
  left: 0;
  position: absolute;
  top: 0;
  width: 272px;
}

.macbook-air-LIGHT .text-wrapper-4 {
  color: #322c2c;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 40px;
  font-weight: 700;
  left: 7px;
  letter-spacing: -4.4px;
  line-height: 47.1px;
  position: absolute;
  top: 23px;
  white-space: nowrap;
  width: 270px;
}

.macbook-air-LIGHT .MEDIEVAL-t {
  height: 92px;
  left: 694px;
  position: absolute;
  top: 206px;
  width: 272px;
}

.macbook-air-LIGHT .text-wrapper-5 {
  color: #322c2c;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 40px;
  font-weight: 700;
  left: 10px;
  letter-spacing: 5.6px;
  line-height: 47.1px;
  position: absolute;
  top: 16px;
  white-space: nowrap;
  width: 237px;
}

.macbook-air-LIGHT .CLASSICISM-GROUP-wrapper {
  height: 92px;
  left: 694px;
  position: absolute;
  top: 62px;
  width: 272px;
}

.macbook-air-LIGHT .text-wrapper-6 {
  color: #322c2c;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 40px;
  font-weight: 700;
  left: 12px;
  letter-spacing: -0.4px;
  line-height: 47.1px;
  position: absolute;
  top: 16px;
  white-space: nowrap;
  width: 240px;
}

.macbook-air-LIGHT .year {
  height: 44px;
  left: 1002px;
  position: absolute;
  top: 89px;
  width: 263px;
}

.macbook-air-LIGHT .ellipse {
  background-color: #fffafa;
  border: 6px solid;
  border-color: #322c2c;
  border-radius: 25px;
  height: 50px;
  left: -3px;
  position: absolute;
  top: -3px;
  width: 50px;
}

.macbook-air-LIGHT .text-wrapper-7 {
  color: #fffafa;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 32px;
  font-weight: 700;
  left: 82px;
  letter-spacing: -3.2px;
  line-height: 37.7px;
  position: absolute;
  top: 4px;
  white-space: nowrap;
  width: 179px;
}

.macbook-air-LIGHT .year-2 {
  height: 44px;
  left: 1002px;
  position: absolute;
  top: 228px;
  width: 201px;
}

.macbook-air-LIGHT .text-wrapper-8 {
  color: #fffafa;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 32px;
  font-weight: 700;
  left: 82px;
  letter-spacing: -3.2px;
  line-height: 37.7px;
  position: absolute;
  top: 4px;
  white-space: nowrap;
  width: 117px;
}

.macbook-air-LIGHT .year-3 {
  height: 44px;
  left: 1002px;
  position: absolute;
  top: 376px;
  width: 208px;
}

.macbook-air-LIGHT .text-wrapper-9 {
  color: #fffafa;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 32px;
  font-weight: 700;
  left: 82px;
  letter-spacing: -3.2px;
  line-height: 37.7px;
  position: absolute;
  top: 0;
  white-space: nowrap;
  width: 124px;
}

.macbook-air-LIGHT .year-4 {
  height: 44px;
  left: 1002px;
  position: absolute;
  top: 517px;
  width: 195px;
}

.macbook-air-LIGHT .text-wrapper-10 {
  color: #fffafa;
  font-family: "Roboto-Bold", Helvetica;
  font-size: 32px;
  font-weight: 700;
  left: 82px;
  letter-spacing: -3.2px;
  line-height: 37.7px;
  position: absolute;
  top: 4px;
  white-space: nowrap;
  width: 111px;
}

.macbook-air-LIGHT .year-5 {
  height: 44px;
  left: 1002px;
  position: absolute;
  top: 659px;
  width: 263px;
}

.macbook-air-LIGHT .line {
  height: 792px;
  left: 1019px;
  position: absolute;
  top: 20px;
  width: 15px;
}

.macbook-air-LIGHT .image {
  height: 455px;
  left: 77px;
  object-fit: cover;
  position: absolute;
  top: 350px;
  width: 464px;
}
</style>