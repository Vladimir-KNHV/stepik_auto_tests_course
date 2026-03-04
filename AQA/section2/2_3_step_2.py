# принять алерт
alert = browser.switch_to.alert
alert.accept()

# получить текст из алерт
alert = browser.switch_to.alert
alert_text = alert.text

# окно конфирм согласие\отказ
confirm = browser.switch_to.alert
confirm.accept()

confirm.dismiss()


# окно промт

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

prompt.dismiss()