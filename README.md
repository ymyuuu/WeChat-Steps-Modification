# WeChat-Steps-Modification

这个项目是一个 GitHub Actions 自动化工作流，可以定期或在代码推送到主分支时运行你的 Python 脚本。它还支持 Telegram 推送，仅在脚本执行失败时才会发送通知。以下是关于项目的详细介绍和使用方法。

## 项目简介

这个项目旨在帮助你自动运行 Python 脚本，并使用 GitHub Actions 进行调度。你可以定期运行脚本，也可以在代码推送到主分支时触发脚本的运行。如果脚本执行失败，你将收到 Telegram 推送通知，以便及时处理问题。
<img width="876" alt="image" src="https://github.com/ymyuuu/WeChat-Steps-Modification/assets/135582157/2034a3bc-4052-4394-b4ac-0891329984a9">


## 如何使用

### 步骤 1: Fork 该项目

首先，你需要 Fork 这个项目到你自己的 GitHub 仓库。点击页面右上角的 "Fork" 按钮来复制项目到你的账户下。

### 步骤 2: 设置 Telegram 推送

在项目设置中，你需要设置以下的 Secrets，以便项目可以发送 Telegram 推送通知。

- `TELEGRAM_API_TOKEN`：你的 Telegram Bot API Token。
- `TELEGRAM_CHAT_ID`：你的 Telegram 聊天 ID，可以是个人聊天或群组聊天的 ID。

### 步骤 3: 设置运行时间

默认情况下，该工作流默认会在每天的UTC时间上午10点6分运行一次。你可以根据自己的需求修改运行时间，编辑 `.github/workflows/main.yml` 文件中的 `schedule` 部分。有关如何配置 Cron 表达式的详细信息，请参考 [Cron 表达式生成器](https://crontab.guru/)。

### 步骤 4: 自定义步数修改

Python 脚本中包含了一个步数修改函数 `modify_steps`，它用于随机生成指定账号的步数并进行修改。你可以根据需要修改步数的最小值和最大值。

### 步骤 5: 自定义默认值

在 Python 脚本中，有一些默认的设置，包括最小和最大步数、Telegram 推送的条件等。你可以根据需要自定义这些默认值，以满足你的具体需求。

## 注意事项

- Telegram 推送只会在脚本执行失败时发送通知，成功修改步数不会触发推送。
- 默认的最小和最大步数为 500000 到 80000 步，你可以根据需要进行自定义。
- 默认的运行时间为每天的UTC时间上午10点6分，你可以在工作流文件中自定义。

## 感谢使用

感谢使用这个自动化工作流项目！如果你有任何问题或建议，欢迎提交 Issue 或 Pull Request 来改进项目。祝你的 Python 脚本顺利运行！
