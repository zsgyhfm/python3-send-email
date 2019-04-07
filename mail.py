import smtplib
from email.header import Header
from email.mime.text import MIMEText

# smtp服务器
mail_host = "smtp.163.com"
# 邮箱账户
mail_account = "xxx"
# 授权码
pwd = "xxx"
# 接收邮箱
receive = 'xxx'

# 邮件内容
context = """
<html>  
  <head></head>  
  <body>  
    <p>
      大隋

    李唐大军兵临城下，张百仁手握诛仙剑，静静的站在紫禁城上，默不作声。

    “先生，萧皇后朕就托付给你了！”隋炀帝看着张百仁，一只手紧紧攥着萧皇后，满脸的依依不舍。

    “陛下放心，皇后德才兼备，温柔大方，有母仪天下之姿，道士定会照顾好皇后娘娘的。”
    </p> 
  </body>  
</html>  
"""
message = MIMEText(context, 'html', 'utf-8')  # subtype 默认是plain ，可选 text  html 类型
message["From"] = mail_account
message["To"] = receive
message["Subject"] = "牧神"

try:
    # 最初使用25端口 非ssl端口 总是链接超时
    smtp_obj = smtplib.SMTP_SSL(mail_host, 465, timeout=30)
    res = smtp_obj.login(mail_account, pwd)  # res = (235, b'Authentication successful')
    smtp_obj.sendmail(mail_account, receive, message.as_string())
    print("发送成功")
    smtp_obj.quit()
except smtplib.SMTPException as e:
    print("异常信息：", e)
