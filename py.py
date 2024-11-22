import os
import requests
import random

# 获取环境变量
telegram_api_token = os.environ.get('TELEGRAM_API_TOKEN')
telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
accounts_and_passwords = os.environ.get('ACCOUNTS_AND_PASSWORDS')

# 检查必需的环境变量
if not all([telegram_api_token, telegram_chat_id, accounts_and_passwords]):
    print("Telegram API Token、聊天ID或账户信息未设置，无法继续操作。")
    exit(1)

# 解析账户和密码
account_password_pairs = [pair.split(',') for pair in accounts_and_passwords.split(';')]

# 发送 Telegram 消息
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    data = {'chat_id': telegram_chat_id, 'text': message, 'parse_mode': 'HTML'}
    requests.post(url, data=data)

# 执行步数修改操作
def modify_steps(account, password, min_steps, max_steps, attempts=3, timeout=20):
    for _ in range(attempts):
        steps = random.randint(min_steps, max_steps)
        url = f"https://steps.api.030101.xyz/api?account={account}&password={password}&steps={steps}"
        
        try:
            response = requests.get(url, timeout=timeout)
            result = response.json()
            if result.get('status') == 'success':
                return f"账号 {account[:3]}***{account[-3:]} 修改成功，步数：{steps}"
        except requests.exceptions.RequestException as e:
            print(f"请求失败：{e}")
        
        # 失败三次后发送通知
        if _ == attempts - 1:
            send_telegram_message(f"<b>Steps_modifier</b>\n\n账号：{account}\n连续失败 {attempts} 次")

    return f"账号 {account[:3]}***{account[-3:]} 修改失败"

# 主程序
def main():
    min_steps = 50000
    max_steps = 80000

    for account, password in account_password_pairs:
        result = modify_steps(account, password, min_steps, max_steps)
        print(result)

if __name__ == "__main__":
    main()
