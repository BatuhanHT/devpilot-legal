# DevPilot Privacy Policy

Last updated: November 26, 2026

DevPilot is an AI assistant for software engineers. This policy explains what data the app handles, who receives it, and how you can delete it.

## Data we collect

- Account data: your email address, display name and engineering role. Your password is handled by our authentication provider and is stored only as a hash.
- Content you create: your chat conversations and messages, saved code snippets (code library), and your projects (name, description, language and linked repository address). Conversation titles, messages, conversation summaries and your code library are encrypted on your device before they are stored (see "How we protect your data").
- Usage records: timestamps of your AI requests, kept only to enforce rate limits and removed automatically after one day.
- Sign-in security records: when you sign in with email and password, we count failed attempts to block password guessing. We store a one-way hash of your email address (not the address itself), the number of failed attempts and, if applicable, when the lock ends. The record is cleared when you next sign in successfully.
- On your device only: your app language choice and, if you add one, your GitHub access token (stored in the iOS Keychain on this device only and never sent to our servers).
- In your iCloud Keychain: the encryption keys that protect your stored conversations. They sync only between your own Apple devices through Apple's end-to-end encrypted iCloud Keychain and are never sent to our servers.

## How AI features use your data

When you chat or analyze code, DevPilot sends your message, your recent conversation history and any code or repository file content you attach to NVIDIA NIM, the AI inference service we use, through our own server. This is the only way answers are generated. This happens only after you give consent, which you can withdraw in Profile → Settings → Privacy & Data.

Before anything is sent, the app scans it on your device for API keys, tokens, private keys and passwords. If it finds one, it asks you first and by default replaces the value with [REDACTED], so the secret is neither sent to the AI service nor stored. Files that typically hold secrets in a linked repository (for example .env files, private keys and certificates) are never sent, and secrets found in other repository files are masked automatically.

## Other services

- Supabase: hosts authentication and our database.
- NVIDIA NIM: generates AI responses (see above).
- GitHub: if you link a repository, the app reads its files from GitHub. Private repositories are accessed with your own token, directly from your device. If you choose to commit an edited file, the app sends that file's content, your commit message and your GitHub token directly from your device to GitHub; none of it passes through our servers. Commits are made under your GitHub account and are subject to GitHub's own privacy terms.

## How we protect your data

- Conversation titles, messages, conversation summaries and your code library are encrypted on your device with AES-256-GCM before they reach our database. Only your devices hold the keys, so neither we nor anyone with access to our database or backups can read this content. To answer you, the AI service still receives the text you send in readable form, as described above.
- Project names, descriptions and repository addresses are stored without this extra encryption so they can be listed.
- All traffic uses encrypted connections (HTTPS), and access to your data in our database is limited to your own account.
- After 3 failed password attempts within 15 minutes, email sign-in to that account is locked for 15 minutes. Sign in with Apple and Google are not affected.
- Code you copy in the app stays on this device (it is not shared with your other devices through Universal Clipboard) and is cleared from the clipboard after 2 minutes. The app hides its contents from the app switcher.

## What we do not do

We do not show ads, do not track you across other companies' apps or websites, do not sell your data and do not use analytics or advertising SDKs.

## Retention and deletion

Your data is kept until you delete it. You can delete your account in Profile → Settings → Privacy & Data → Delete Account. This permanently removes your account, conversations, messages, code library, projects and profile from our servers, and deletes your encryption keys from your iCloud Keychain, so any copy that might remain in a backup can no longer be read. Deleting the app removes the data stored on your device.

## Children

DevPilot is not intended for children under 13.

## Changes

We may update this policy. The date above shows the latest version.

## Contact

You can reach us at btemelbusiness@outlook.com.
