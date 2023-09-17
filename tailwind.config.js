/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ['node_modules/preline/dist/*.js',
    "./src/**/*.{html,js}",],
  theme: {
    extend: {},
  },
  plugins: [ 
    require('preline/plugin'),
   
  ],
  
}

