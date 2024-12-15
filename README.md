# update-checker

This Python program monitors a specified website for updates. If a change is detected, it sends a notification through a Discord webhook.

# setup

Start by cloning the repository and navigating to the project folder.

Configure the `data.json` file, with the URL of the website you want to monitor and the CSS selector for the content you want to track:

```json
{
    "url": "WEBSITE_URL",
    "selector": "CSS_SELECTOR",
    "webhook_url": "WEBHOOK_URL"
}
```

_Example:_

```json
{
    "url": "https://en.wikipedia.org/wiki/Kangaroo",
    "selector": "main",
    "webhook_url": "WEBHOOK_URL"
}
```

This will monitor the `main` tag of the [Wikipedia page about kangaroos](https://en.wikipedia.org/wiki/Kangaroo).

> [!WARNING]
> Complex selectors aren't supported. Use only tags, classes and ids.
>
> These are supported:
> - `body`
> - `div.flex`
> - `h1#header`
>
> These are not:
> - `div>p`
> - `:is(.a, .b)`
> - `article:has(>*>b)`

Create a [Discord webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) on your Discord server, and copy the link.

Paste it in the `data.json` file.

Now, the program is configured and will send the following message to the channel of your choice, every time the website is updated:

> ### Update detected!

<br>

> [!NOTE]
> The program doesn't run in the background. You have to execute it every time you want to check or automate the process (e.g. use Linux crontab)
