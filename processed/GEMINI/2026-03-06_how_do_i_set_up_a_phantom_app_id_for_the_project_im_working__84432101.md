---
id: 094707
source: GEMINI
date: 2026-03-06
tags: ['phantom-wallet', 'app-id', 'mcp-configuration', 'defi-agent']
category: crypto-web3
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
summary: Bryan was trying to set up a Phantom app ID for his self-sustaining agent project's MCP integration.
---
# how do i set up a phantom app id for the project im working on? 

### USER
how do i set up a phantom app id for the project im working on? 

### GEMINI
To set up a Phantom App ID, you need to use the Phantom Developer Portal. This ID is a unique identifier required for integrating Phantom's SDKs (especially for "Phantom Connect" and embedded wallet features) into your web or mobile project. Follow these steps to generate and configure it: 1. Register Your App Navigate to phantom.com/portal. Sign in with your wallet or developer credentials. Click Create App (or "Add New App"). Enter your project details: App Name: The name users will see during the connection prompt. App Icon: Upload a high-quality logo (crucial for user trust). 2. Configure Your Environment Once the app is created, you must whitelist your domains and redirect URIs to prevent unauthorized use of your App ID. Allowed Origins: Add your development URL (e.g., http://localhost:3000) and your production domain (e.g., https://yourdomain.com). Redirect URLs: If you are building a mobile app or using OAuth-style flows (Google/Apple sign-in), you must specify the URI where Phantom should send users back to after they authenticate. 3. Retrieve the App ID In the Portal’s left navigation, select your app. Go to the Set Up or Settings page. Your App ID will be displayed at the top. Copy this string. 4. Implementation Example Depending on your stack, you will pass this ID into the SDK initialization. For Web (React/JavaScript): import { BrowserSDK } from "@phantom/browser-sdk"; const sdk = new BrowserSDK({ appId: "YOUR_PHANTOM_APP_ID", // Paste your ID here providers: ["google", "apple", "injected", "deeplink"], }); For Mobile (React Native): <PhantomProvider config={{ appId: "YOUR_PHANTOM_APP_ID", scheme: "your-app-scheme", // e.g., 'myapp' addressTypes: ['solana'], }} > <App /> </PhantomProvider> Strategic Tips Security: While the App ID is safe to include in client-side code, never commit your .env file containing other sensitive keys to version control. App Status: New apps in the Portal may start in a "Limited" or "Development" mode. Ensure you move to Public mode in the Portal settings before your official launch so users can find you in the Phantom "Explore" tab. Would you like me to walk through the specific deep-linking configuration for an iOS or Android build?
