# WeChat-Steps-Modification

这个项目旨在帮助你定期运行 Python 脚本，以便在需要时修改特定账号的步数。脚本运行失败时，会通过 Telegram 向你发送通知，以便你可以及时采取行动。以下是关于如何使用和配置该项目的详细说明。
![image](https://github.com/ymyuuu/WeChat-Steps-Modification/assets/135582157/7325fabb-f20d-4835-8e71-5ce0fc3d22d3)

## 使用方法

### 1. Fork 本仓库

首先，点击本仓库右上角的 "Fork" 按钮，将项目复制到你自己的 GitHub 账户下。

### 2. 配置 Secrets

在你的 GitHub 仓库中，点击上方菜单中的 "Settings"，然后选择 "Secrets" 选项卡。你需要添加以下几个 Secrets 以便项目正常工作：

- `TELEGRAM_API_TOKEN`: 你的 Telegram 机器人 API Token。你可以从 [BotFather](https://core.telegram.org/bots#botfather) 获取它。

- `TELEGRAM_CHAT_ID`: 你希望接收通知的 Telegram 聊天 ID。你可以从 [userinfobot](https://core.telegram.org/bots#usernames-and-telegram-ids) 获取它。

- `ACCOUNTS_AND_PASSWORDS`: 你想要修改步数的账号和密码对，以分号分隔。每个对之间使用逗号分隔。例如，`username1,password1;username2,password2`。请确保保密这个 Secrets 以保护你的账号信息。

- `SEND_TELEGRAM_MESSAGE`: 设置为 `true` 或 `false`，以控制是否发送 Telegram 消息。如果设置为 `false`，脚本将不会发送 Telegram 消息，否则会发送。

### 3. 自定义脚本

在本仓库中，你可以找到一个名为 `py.py` 的 Python 脚本文件。这个脚本用于修改账号的步数。你可以根据自己的需求修改这个脚本，例如更改最小和最大步数，修改 API 请求的 URL 等。

### 4. 自定义运行时间

默认情况下，脚本会在 UTC 时间的上午10点6分运行（每天一次）。如果你想要更改运行时间，可以编辑 `.github/workflows/main.yml` 文件中的 `schedule` 部分。按照 [Cron 表达式](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#onschedule) 的格式来配置。

### 5. 自定义最小和最大步数

在脚本的 `__main__` 部分，你可以找到 `min_steps` 和 `max_steps` 变量。你可以根据需要更改这些值，以定义修改步数的范围。

## 注意事项

- **Telegram 通知**：脚本会在运行失败时向你的 Telegram 账号发送通知。如果脚本成功运行，不会发送通知。

- **默认设置**：脚本默认使用了最小步数为 50000，最大步数为 80000 的设置，以及在 UTC 时间上午10点6分运行的计划。你可以根据需要进行自定义。

- **账号信息**：请务必保护好你的账号信息，特别是 `ACCOUNTS_AND_PASSWORDS` Secret。不要将这些信息公开。

- **定期检查**：定期检查项目是否正常运行，以确保你的账号步数得到及时更新。

通过遵循以上步骤，你可以轻松使用这个项目来定期修改特定账号的步数并接收通知。如果你有任何问题或需要进一步的帮助，欢迎提出问题或提出建议。

## 许可证

本项目采用 MIT 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。

感谢你的使用！如果你对这个项目有任何改进或建议，也欢迎贡献代码或提出问题。
