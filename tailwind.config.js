/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
    "./static/**/*.html"
  ],
  theme: {
    extend: {
      colors: {
        mainColor: '#050C2A'
      },
      padding: {
        PadBig: '50px'
      }
    },
  },
  plugins: [],
}

