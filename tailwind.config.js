const defaultTheme = require('tailwindcss/defaultTheme')
// const colors = require('tailwindcss/colors')

const wvLogoBlue = 'hsl(218, 22%, 23%)'
const wvLogoCyan = 'hsl(170, 41%, 43%)'

module.exports = {
    content: [
        './lpld/**/*.{html, js, css}',
    ],
    theme: {
        fontFamily: {
            'sans': ['Moderat', 'Verdana', 'Tahoma', 'sans-serif'],
        },
        extend: {
            screens: {
                // Approx. iPhone 5 horizontal orientation
                "xs": "560px",
                ...defaultTheme.screens,
            },
            colors: {
                wvlogoblue: wvLogoBlue,
                wvblue: {
                    50: 'hsl(218, 72%, 98%)',
                    100: 'hsl(218, 52%, 95%)',
                    200: 'hsl(218, 37%, 83%)',
                    300: 'hsl(218, 30%, 73%)',
                    400: 'hsl(218, 25%, 65%)',
                    500: 'hsl(218, 17%, 53%)',
                    600: 'hsl(218, 20%, 37%)',
                    700: 'hsl(218, 20%, 30%)',
                    800: wvLogoBlue,  // This is the base
                    900: 'hsl(218, 52%, 8%)',
                },
                wvlogocyan: wvLogoCyan,
                wvcyan: {
                    50: 'hsl(170, 61%, 96%)',
                    100: 'hsl(170, 61%, 92%)',
                    200: 'hsl(170, 45%, 87%)',
                    300: 'hsl(170, 45%, 77%)',
                    400: 'hsl(170, 45%, 65%)',
                    500: 'hsl(170, 41%, 53%)',
                    600: wvLogoCyan,  // This is the base
                    700: 'hsl(170, 41%, 27%)',
                    800: 'hsl(170, 67%, 15%)',
                    900: 'hsl(170, 81%, 8%)',
                },
            },
            fontFamily: {
                'sans': ['Helvetica', 'Helvetica Neue', 'Arial', ...defaultTheme.fontFamily.sans],
            },
            textDecorationThickness: {
                3: '3px',
            },
            textUnderlineOffset: {
                3: '3px',
            },
        },
    },
    plugins: [
        // require('@tailwindcss/forms')
    ],
}
