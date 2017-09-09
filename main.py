# -*- coding: utf-8 -*-
from flask import Flask
import yagmail
import logging
import sys
from flask import request

reload(sys)
sys.setdefaultencoding('utf-8')

# change here

mail_user = "15759260592@163.com"
mail_pass = "A15759260592"
smtp_host = "smtp.163.com"
smtp_port = '994'
# end change

app = Flask(__name__)


@app.route("/send", methods=["POST"])
def send():
    logging.info(request.form['content'])
    lines = str(request.form['content']).split("||")
    content = dict()
    for line in lines:
        content[line.split("=")[0]] = line.split("=")[1]
    user = content["user"]
    subject = content.get("subject", "send by my self mail service.")
    content = content["content"]
    if user is None or user == '':
        logging.error("user is empty! %s" % request.form['content'])
        return
    # new instance ever once for smtp server may drop the connection
    yag = yagmail.SMTP(user=mail_user, password=mail_pass, host=smtp_host, port=smtp_port)
    yag.send(to=user, subject=subject, contents=content)
    return "send mail successfully!"

if __name__ == '__main__':
    app.run()
