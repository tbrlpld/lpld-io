const defaultTheme = require('tailwindcss/defaultTheme')
// const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    './lpld/**/*.{html, js, css}'
  ],
  theme: {
    extend: {
      screens: {
        // Approx. iPhone 5 horizontal orientation
        xs: '560px',
        ...defaultTheme.screens
      },
      fontFamily: {
        sans: [
          'Helvetica',
          'Helvetica Neue',
          'Arial',
          ...defaultTheme.fontFamily.sans
        ]
      },
      textDecorationThickness: {
        3: '3px'
      },
      textUnderlineOffset: {
        3: '3px'
      }
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
  ]
}
