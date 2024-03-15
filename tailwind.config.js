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
          [
            'InterVariable',
            'Helvetica',
            'Helvetica Neue',
            'Arial',
            ...defaultTheme.fontFamily.sans
          ],
          {
            fontFeatureSettings: '"cv11", "ss01"',
            fontVariationSettings: '"opsz" 32'
          },
        ]
      },
      textDecorationThickness: {
        3: '3px'
      },
      textUnderlineOffset: {
        3: '3px'
      },
      typography: ({ theme }) => ({
        // Add a custom prose color theme that is heavily based on the "neutral" theme.
        // https://tailwindcss.com/docs/typography-plugin#adding-custom-color-themes
        'neutral-500': {
          css: {
            '--tw-prose-body': theme('colors.neutral.500'),
            ...theme('css')
          }
        }
      })
    }
  },
  plugins: [
    require('@tailwindcss/typography')
  ]
}
