# 微信运动 Python 脚本自动修改步数

该项目允许你使用 GitHub Actions 在特定时间或通过推送到主分支触发的方式运行一个 Python 脚本，该脚本用于自动修改指定小米运动账户的步数。此 README 将详细介绍如何设置和使用该项目。

## 项目概述

这个项目旨在帮助你自动化修改指定小米运动账户的步数，适用于微信运动步数修改。它使用 GitHub Actions 来调度脚本的运行，并利用 Telegram 来通知你关于步数修改的情况。
<img width="876" alt="image" src="https://github.com/ymyuuu/step/assets/135582157/ff13d0c2-ed20-4d32-b7b8-6b2d7bed886c">



## 项目要求

在开始使用此项目之前，确保你满足以下要求：

- 一个 GitHub 账户和仓库用于托管你的代码。
- 一个 Telegram Bot 的 API Token 用于发送通知消息。
- 一个 Telegram 聊天 ID，指定你希望接收通知消息的聊天。
- 账号和密码的列表，用于访问需要修改步数的应用程序。

## 设置项目

### 1. 创建 Telegram Bot

首先，创建一个 Telegram Bot 并获取其 API Token。你可以通过与 [BotFather](https://core.telegram.org/bots#botfather) 交互来创建一个新的 Telegram Bot，并获取 API Token。

### 2. 获取 Telegram 聊天 ID

为了将通知消息发送到 Telegram，你需要获取你希望接收通知消息的聊天 ID。你可以使用 [userinfobot](https://core.telegram.org/bots#usernames-and-telegram-ids) 来获取自己的 Telegram 聊天 ID。

### 3. 配置 GitHub 仓库 Secrets

在你的 GitHub 仓库中，转到 Settings > Secrets，然后添加以下 Secrets：

- `TELEGRAM_API_TOKEN`：将你的 Telegram Bot 的 API Token 添加为此 Secret。
- `TELEGRAM_CHAT_ID`：将你的 Telegram 聊天 ID 添加为此 Secret。
- `ACCOUNTS_AND_PASSWORDS`：将账号和密码组成的列表添加为此 Secret。列表中每个元素都应该是一个以逗号分隔的字符串，表示一个账号和密码的组合，如 "username1,password1;username2,password2"。

### 4. 修改 Python 脚本

确保 Python 脚本中的以下内容正确设置：

- `telegram_api_token`：应该从 Secrets 中读取 Telegram API Token。
- `telegram_chat_id`：应该从 Secrets 中读取 Telegram 聊天 ID。
- `accounts_and_passwords`：应该从 Secrets 中读取账号和密码。

### 5. 定义步数修改范围（可自定义）

在 Python 脚本中，你可以定义步数的修改范围，即 `min_steps` 和 `max_steps` 变量。这将控制每个账号修改的步数范围。默认情况下，范围为 50000 到 80000 步。

### 6. 定义运行时间（可自定义）

你可以通过编辑 GitHub Actions 工作流程文件中的 `schedule` 部分来自定义脚本的运行时间。默认情况下，脚本将在 UTC 时间上午10点6分运行，但你可以根据需要进行修改。

## 使用方法

一旦设置好项目并配置了 Secrets，你就可以开始使用它了。以下是使用该项目的步骤：

1. 推送到主分支：如果你设置了推送到主分支触发 GitHub Actions 工作流程，只需将代码推送到主分支即可。工作流程将在你定义的时间（默认为 UTC 时间上午10点6分）自动运行。

2. 手动触发工作流程（可选）：如果你没有设置自动触发工作流程，可以在 GitHub 仓库的 Actions 选项卡中手动触发工作流程。选择适当的工作流程并点击 "Run workflow" 按钮。

3. 查看通知（仅在失败时推送到 Telegram）：一旦工作流程运行完成，并且步数修改失败，它将通过 Telegram 向你发送通知消息，告诉你每个账号的步数修改情况。

## 注意事项

- 请注意，默认情况下，通知消息仅在步数修改失败时才会发送到 Telegram。如果成功修改步数，将不会发送通知。
- 此项目仅供学习和测试使用，不建议用于违反应用程序的使用条款或条件。

## 结语

通过本项目，你可以轻松自动化修改指定账户的步数，并通过 Telegram 接收通知消息，以便随时了解步数修改情况。希望你能够充分利用这个项目，如果有任何问题或建议，请随时提出。你可以自定义步数修改范围和运行时间以满足特定需求。
