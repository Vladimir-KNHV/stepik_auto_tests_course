# Для переключения на новую вкладку надо явно указать
browser.switch_to.window(window_name)

# метод window_handles, который возвращает массив имён всех вкладок.

new_window = browser.window_handles[1] # выбрали вторую вкладку


# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]

