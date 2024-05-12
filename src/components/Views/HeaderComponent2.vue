<template>
  <header :class="{ 'dark-theme': themeSettings.dark }">
    <h1>Art History App</h1>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/about">About</router-link></li>
        <li><router-link to="/contact">Contact</router-link></li>
      </ul>
    </nav>
  </header>
</template>

  
  <script>
import { reactive } from 'vue'

const themeSettings = reactive({
  dark: false
})

export default {
  name: 'HeaderComponent',
  setup() {
    // This function will expose reactive properties to the template
    return {
      themeSettings
    };
  }
}
</script>

  
  <style>
/*  Set the body background and base styles  */ 
body {
  margin: 0;
  padding: 0;
  background-color: #fdfbfb; /* Bright red background */
  font-family: Arial, sans-serif; /* Simplistic and widely available font */
  color: #000000; /* Black color for the text */
}

/* Full-width sections with text alignment */
.full-width-section {
  width: 100%;
  text-align: center; /* Center-align the text */
  padding: 50px 0; /* Padding for spacing */
}

/* Styling for main headings using bold and impactful sizing */
.huge-text {
  font-size: 10vw; /* Responsive font size based on viewport width */
  font-weight: bold; /* Bold font for emphasis */
  line-height: 1.2; /* Tight line spacing */
  letter-spacing: -2px; /* Negative letter-spacing for a compact look */
}

/* Navigation and other links */
nav {
  position: absolute;
  top: 0;
  width: 100%;
  padding: 20px 0;
  font-size: 1.5vw; /* Smaller responsive font size */
}

nav ul {
  list-style-type: none; /* Remove list bullets */
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-around; /* Even spacing of nav items */
}

nav ul li {
  display: inline;
}

nav ul li a {
  text-decoration: none; /* No underlines on links */
  color: #000; /* Black text for contrast */
  font-weight: bold; /* Bold text for readability */
}

.footer-links {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 20px 0;
  font-size: 1.2vw; /* Slightly larger font for footer links */
  display: flex;
  justify-content: space-between; /* Space out links on either side */
  padding: 0 10%; /* Padding on the sides */
}

.footer-links a {
  text-decoration: none;
  color: #000; /* Consistent black color for footer links */
}


</style>

 
  