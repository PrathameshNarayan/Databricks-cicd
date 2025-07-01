name: Send Email Notification on Push to Main

on:
  push:
    branches:
      - main  # Trigger only when there's a push to the `main` branch

jobs:
  send-email:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install necessary Python packages
        run: |
          pip install smtplib

      - name: Send Email Notification
        run: |
          echo "Sending email notification..."
          python3 send_email.py  # This runs the email script
        env:
          OUTLOOK_EMAIL: ${{ secrets.OUTLOOK_EMAIL }}  # Your Outlook email
          OUTLOOK_PASSWORD: ${{ secrets.OUTLOOK_PASSWORD }}  # Your Outlook password
          MAIN_BRANCH_OWNER_EMAIL: ${{ secrets.MAIN_BRANCH_OWNER_EMAIL }}  # Owner's email address from GitHub secrets
