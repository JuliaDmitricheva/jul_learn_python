question = "привет"
dict_answers  = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def get_answer(question, dict_answers):
	return dict_answers.get(question.lower(), 'мммм....')

question = input(" > ")
get_answer(question, dict_answers)