// Main entry point
import * as Sentry from '@sentry/browser'
import { BrowserTracing } from '@sentry/tracing'

function main () {
  setUpSentry()
}

function setUpSentry () {
  const sentrySettings = getSentrySettings()
  Sentry.init({
    dsn: sentrySettings.SENTRY_DSN,
    integrations: [new BrowserTracing()],
    tracesSampleRate: sentrySettings.SENTRY_SAMPLE_RATE,
    environment: sentrySettings.SENTRY_ENVIRONMENT,
    release: sentrySettings.HEROKU_RELEASE_VERSION
  })
  if (sentrySettings.SENTRY_TEST) {
    // This is calling a non existing function to test the error monitoring.
    nonExistentFunction() // eslint-disable-line no-undef
  }
}

function getSentrySettings () {
  const sentrySettingsElement = document.querySelector('#sentry-settings')
  const sentrySettings = JSON.parse(sentrySettingsElement.textContent)
  return sentrySettings
}

(function () { main() })()
