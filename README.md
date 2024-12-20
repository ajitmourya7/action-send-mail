# SendGrid HTML Email Action

This GitHub Action sends HTML emails using SendGrid.

## Inputs

| Name               | Description                | Required | Default |
|--------------------|----------------------------|----------|---------|
| `sendgrid_api_key` | SendGrid API Key           | Yes      |         |
| `from_email`       | Sender's email address     | Yes      |         |
| `to_email`         | Recipient's email address  | Yes      |         |
| `subject`          | Email subject              | Yes      |         |
| `html_content`     | HTML content of the email  | Yes      |         |

## Example Usage

```yaml
name: Send HTML Email with SendGrid
on:
  push:
    branches:
      - main

jobs:
  send-email:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Send HTML email with SendGrid
        uses: your-username/sendgrid-html-email-action@v1.0.0
        with:
          sendgrid_api_key: '${{ secrets.SENDGRID_API_KEY }}'
          from_email: 'sender@example.com'
          to_email: 'recipient@example.com'
          subject: 'GitHub Action Email'
          html_content: |
            <h1>Hello!</h1>
            <p>This is an <b>HTML</b> email sent by a custom GitHub Action using SendGrid.</p>