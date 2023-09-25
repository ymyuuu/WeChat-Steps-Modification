import os
import requests
import base64
import random

# 从 Secrets 中读取 Telegram API Token 和聊天 ID
telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

# 从 Secrets 中读取账号和密码
accounts_and_passwords = os.environ['ACCOUNTS_AND_PASSWORDS']
account_password_pairs = [pair.split(',') for pair in accounts_and_passwords.split(';')]

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    data = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    response = requests.post(telegram_url, data=data)

def modify_steps(account, password, min_steps=None, max_steps=None):
    try:
        encoded_url = 'aHR0cDovL2JzLnN2di5pbmsvaW5kZXgucGhw'
        url = base64.b64decode(encoded_url).decode('utf-8')
        steps = random.randint(min_steps, max_steps)
        data = {
            'account': account,
            'password': password,
            'steps': steps
        }

        response = requests.post(url, data=data)
        result = response.json()

        # 检查响应是否不是"success"，然后发送Telegram消息
        if result.get('message') != 'success':
            telegram_message = f"<b>Steps_modifier</b>\n\n账号： {account}\n响应： {result.get('message', 'No message found in response')}"
            send_telegram_message(telegram_message)

        return {
            'account': account,
            'response': result.get('message', 'No message found in response')
        }
    except Exception as e:
        telegram_message = f"<b>Steps_modifier</b>\n\n账号： {account}\n错误： {str(e)}"
        send_telegram_message(telegram_message)
        return {
            'account': account,
            'response': str(e)
        }

# def modify_steps(account, password, min_steps=None, max_steps=None):
#     encoded_url = 'aHR0cDovL2JzLnN2di5pbmsvaW5kZXgucGhw'
#     url = base64.b64decode(encoded_url).decode('utf-8')
#     steps = random.randint(min_steps, max_steps)
#     data = {
#         'account': account,
#         'password': password,
#         'steps': steps
#     }

#     response = requests.post(url, data=data)
#     result = response.json()
    
#     # 检查响应是否不是"success"，然后发送Telegram消息
#     if result.get('message') != 'success':
#         telegram_message = f"<b>Steps_modifier</b>\n\n账号: {account}\n响应: {result.get('message', 'No message found in response')}"
#         send_telegram_message(telegram_message)

#     return {
#         'account': account,
#         'response': result.get('message', 'No message found in response')
#     }
    
# 默认使用了最小步数为50000，最大步数为80000
if __name__ == "__main__":
    min_steps = 50000
    max_steps = 80000

    for account, password in account_password_pairs:
        result = modify_steps(account, password, min_steps, max_steps)
        # 隐藏账号的中间部分
        hidden_account = account[:3] + '*' * (len(account) - 6) + account[-3:]

        print("账号:", hidden_account)
        print("响应:", result['response'])
