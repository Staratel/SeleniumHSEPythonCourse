import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

URL = "https://learnonline.hse.ru/"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
username = ''
pwd = ''


def task_6_1():
	print("\n\ntask_6_1")
	with open("task_6_1") as f:
		text = f.read()
		codes = text.split("|")
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558919")  # Неделя 6 Задачи на линейный поиск
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)

	elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')
	for i in range(len(elements)):
		print(elements[i])
		id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
		question = driver.find_element(By.ID, id_code)
		pyperclip.copy(codes[i])  # Переделать на флаги для других заданий с множеством кодов
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
		question.find_element(By.CLASS_NAME, "btn-secondary").click()
		time.sleep(2)
		if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
				'class'):
			btn = driver.find_element(By.XPATH,
									  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
			ActionChains(driver).click(btn).perform()
			print('good')
		else:
			print('bad')
	time.sleep(10)


def task_6_2():
	print("\n\ntask_6_2")
	with open("task_6_2") as f:
		text = f.read()
		codes = text.split("|")
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558922")  # Неделя 6 Простые задачи на сортировку
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)

	elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')
	for i in range(len(elements)):
		id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
		question = driver.find_element(By.ID, id_code)
		pyperclip.copy(codes[i])  # Переделать на флаги для других заданий с множеством кодов
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
		question.find_element(By.CLASS_NAME, "btn-secondary").click()
		print("click precheck")
		time.sleep(2)
		if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
				'class'):
			btn = driver.find_element(By.XPATH,
									  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
			ActionChains(driver).click(btn).perform()
			print("click check")
			print('good')
		else:
			print('bad')
	time.sleep(10)


def task_6_3():
	print("\n\ntask_6_3")
	with open("task_6_3") as f:
		text = f.read()
		codes = text.split('|')
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558933")  # Неделя 6 Простые задачи на сортировку
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)

	elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')
	for i in range(len(elements)):
		id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
		question = driver.find_element(By.ID, id_code)
		pyperclip.copy(codes[i])  # Переделать на флаги для других заданий с множеством кодов
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
		question.find_element(By.CLASS_NAME, "btn-secondary").click()
		print("click precheck")
		time.sleep(2)
		if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
				'class'):
			btn = driver.find_element(By.XPATH,
									  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
			ActionChains(driver).click(btn).perform()
			print("click check")
			print('good')
		else:
			print('bad')
	time.sleep(10)


def task_6_4():
	print("\n\ntask_6_4")
	with open("task_6_4") as f:
		text = f.read()
		codes = text.split('|')
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558936")  # Неделя 6 Простые задачи на сортировку
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)
	flag_file = 0
	for j in range(2):

		elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')
		for i in range(len(elements)):
			id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
			question = driver.find_element(By.ID, id_code)
			pyperclip.copy(codes[flag_file])  # Переделать на флаги для других заданий с множеством кодов
			question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
			question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
			question.find_element(By.CLASS_NAME, "btn-secondary").click()
			print("click precheck for", flag_file + 1)
			time.sleep(2)
			if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
					'class'):
				btn = driver.find_element(By.XPATH,
										  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
				ActionChains(driver).click(btn).perform()
				print("click check")
				print('good')
			else:
				print('bad')
			flag_file += 1
		btn = driver.find_element(By.CLASS_NAME, 'mod_quiz-next-nav')
		if btn.get_attribute('value') == 'Следующий вопрос':
			ActionChains(driver).click(btn).perform()
	time.sleep(10)


def task_7_1():
	print("\n\ntask_7_1")
	with open("task_7_1") as f:
		text = f.read()
		codes = text.split('|')
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558946")  # Неделя 7 Простые задачи на сортировку
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)
	flag_file = 0
	for j in range(2):

		elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')

		for i in range(len(elements)):
			id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
			question = driver.find_element(By.ID, id_code)
			pyperclip.copy(codes[flag_file])  # Переделать на флаги для других заданий с множеством кодов
			question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
			question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
			question.find_element(By.CLASS_NAME, "btn-secondary").click()
			print("\nclick precheck for", flag_file + 1)
			time.sleep(2)
			try:
				if 'good' in driver.find_element(By.XPATH,
												 f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
						'class'):
					btn = driver.find_element(By.XPATH,
											  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
					ActionChains(driver).click(btn).perform()
					print("click check")
					print('good')
				else:
					print('bad')
			except:
				print("Ошибка, не нашёл кнопку")
				flag_file += 1
				continue
			flag_file += 1

		btn = driver.find_element(By.CLASS_NAME, 'mod_quiz-next-nav')
		if btn.get_attribute('value') == 'Следующий вопрос':
			ActionChains(driver).click(btn).perform()
	time.sleep(5)


def task_7_2():
	with open("task_7_2") as f:
		text = f.read()
		codes = text.split('|')
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558955")  # Неделя 7 2
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)
	flag_file = 0
	for j in range(2):

		elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')

		for i in range(len(elements)):
			id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
			question = driver.find_element(By.ID, id_code)
			pyperclip.copy(codes[flag_file])
			question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
			question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
			question.find_element(By.CLASS_NAME, "btn-secondary").click()
			print("\nclick precheck for", flag_file + 1)
			time.sleep(2)
			try:
				if 'good' in driver.find_element(By.XPATH,
												 f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
						'class'):
					btn = driver.find_element(By.XPATH,
											  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
					ActionChains(driver).click(btn).perform()
					print("click check")
					print('good')
				else:
					print('bad')
			except:
				print("Ошибка")
				continue
			flag_file += 1

		time.sleep(2)
		btn = driver.find_element(By.CLASS_NAME, 'mod_quiz-next-nav')
		if btn.get_attribute('value') == 'Следующий вопрос':
			print("Перешёл на другую страницу")
			ActionChains(driver).click(btn).perform()
	time.sleep(5)


def task_8_1():
	with open("task_8_1") as f:
		text = f.read()
		codes = text.split('|')
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558969")  # Неделя 8 1
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)
	flag_file = 0

	elements = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')

	for i in range(len(elements)):
		print(elements[i])
		id_code = driver.find_elements(By.CLASS_NAME, 'adaptive_adapted_for_coderunner')[i].get_attribute('id')
		question = driver.find_element(By.ID, id_code)
		pyperclip.copy(codes[flag_file])
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
		question.find_element(By.CLASS_NAME, "btn-secondary").click()
		print("click precheck")
		time.sleep(2)
		try:
			if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
					'class'):
				btn = driver.find_element(By.XPATH,
										  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[{i + 1}]/div[2]/div[1]/div[4]/div/input[2]')
				ActionChains(driver).click(btn).perform()
				print("click check")
				print('good')
			else:
				print('bad')
		except:
			print("Ошибка")
			continue
		flag_file += 1
	time.sleep(5)


def task_9_1():
	with open("task_9_1") as f:
		text = f.read()
		codes = text.split('|')
	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558978")  # Неделя 9 1
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)

	id_code = driver.find_element(By.CLASS_NAME, 'adaptive_adapted_for_coderunner').get_attribute('id')
	question = driver.find_element(By.ID, id_code)
	pyperclip.copy(codes[0])
	question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
	question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
	question.find_element(By.CLASS_NAME, "btn-secondary").click()
	print("click precheck")
	time.sleep(2)
	try:
		if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
				'class'):
			btn = driver.find_element(By.XPATH,
									  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[1]/div[2]/div[1]/div[4]/div/input[2]')
			ActionChains(driver).click(btn).perform()
			print("click check")
			print('good')
		else:
			print('bad')
	except:
		print("Ошибка")
	time.sleep(1)

	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558981")  # Неделя 9 2
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)

	id_code = driver.find_element(By.CLASS_NAME, 'adaptive_adapted_for_coderunner').get_attribute('id')
	question = driver.find_element(By.ID, id_code)
	pyperclip.copy(codes[1])
	question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
	question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
	question.find_element(By.CLASS_NAME, "btn-secondary").click()
	print("click precheck")
	time.sleep(2)
	try:
		if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
				'class'):
			btn = driver.find_element(By.XPATH,
									  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[1]/div[2]/div[1]/div[4]/div/input[2]')
			ActionChains(driver).click(btn).perform()
			print("click check")
			print('good')
		else:
			print('bad')
	except:
		print("Ошибка")
	time.sleep(1)

	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558986")  # Неделя 9 3
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)
	flag_file = 2

	for i in range(2):
		id_code = driver.find_element(By.CLASS_NAME, 'adaptive_adapted_for_coderunner').get_attribute('id')
		question = driver.find_element(By.ID, id_code)
		pyperclip.copy(codes[flag_file])
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
		question.find_element(By.CLASS_NAME, "btn-secondary").click()
		print("click precheck")
		time.sleep(2)
		try:
			if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
					'class'):
				btn = driver.find_element(By.XPATH,
										  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[1]/div[2]/div[1]/div[4]/div/input[2]')
				ActionChains(driver).click(btn).perform()
				print("click check")
				print('good')
			else:
				print('bad')
		except:
			print("Ошибка")
			continue
		flag_file += 1
		btn = driver.find_element(By.CLASS_NAME, 'mod_quiz-next-nav')
		if btn.get_attribute('value') == 'Следующий вопрос':
			ActionChains(driver).click(btn).perform()

	driver.get(url="https://learnonline.hse.ru/mod/quiz/view.php?id=558989")  # Неделя 9 4
	driver.find_element(By.CLASS_NAME, "btn-secondary").click()  # Для захода на первую попытку или продолжение попытки
	time.sleep(2)
	flag_file = 4

	for i in range(2):
		id_code = driver.find_element(By.CLASS_NAME, 'adaptive_adapted_for_coderunner').get_attribute('id')
		question = driver.find_element(By.ID, id_code)
		pyperclip.copy(codes[flag_file])
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'a')
		question.find_element(By.CLASS_NAME, "ace_text-input").send_keys(Keys.CONTROL, 'v')
		question.find_element(By.CLASS_NAME, "btn-secondary").click()
		print("click precheck")
		time.sleep(2)
		try:
			if 'good' in driver.find_element(By.XPATH, f'//*[@id="{id_code}"]/div[2]/div[2]/div/div/div').get_attribute(
					'class'):
				btn = driver.find_element(By.XPATH,
										  f'/html/body/div[2]/div[3]/div/div[1]/section/div[1]/div/div/form/div/div[1]/div[2]/div[1]/div[4]/div/input[2]')
				ActionChains(driver).click(btn).perform()
				print("click check")
				print('good')
			else:
				print('bad')
		except:
			print("Ошибка")
			continue
		flag_file += 1
		btn = driver.find_element(By.CLASS_NAME, 'mod_quiz-next-nav')
		if btn.get_attribute('value') == 'Следующий вопрос':
			ActionChains(driver).click(btn).perform()
	time.sleep(1)


if __name__ == '__main__':
	try:
		driver.get(url=URL)
		time.sleep(1)
		driver.find_element(By.CLASS_NAME, "btn-login-top").click()  # Переход на страницу логина и пароля

		# Для OpenEdu логина
		# driver.get(url='https://learnonline.hse.ru/auth/openedu/')
		# time.sleep(2)
		# email_input = driver.find_element(By.NAME, "username")
		# email_input.clear()
		# email_input.send_keys(username)
		#
		# pwd_input = driver.find_element(By.NAME, "password")
		# pwd_input.clear()
		# pwd_input.send_keys(pwd)
		# driver.find_element(By.CLASS_NAME, "btn-submit").click()
		# time.sleep(5)

		email_input = driver.find_element(By.ID, "username")
		email_input.clear()
		email_input.send_keys(username)

		pwd_input = driver.find_element(By.ID, "password")
		pwd_input.clear()
		pwd_input.send_keys(pwd)
		driver.find_element(By.ID, "loginbtn").click()

		task_6_1()
		task_6_2()
		task_6_3()
		task_6_4()
		task_7_1()
		task_7_2()
		task_8_1()
		task_9_1()

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

