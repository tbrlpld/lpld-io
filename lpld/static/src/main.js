// Main entry point


function main(){
    const sentrySettings = getSentrySettings()
}


function getSentrySettings() {
    const sentrySettingsElement = document.querySelector('#sentry-settings')
    const sentrySettings = JSON.parse(sentrySettingsElement.textContent)
    return sentrySettings
}


(function(){main()})()
