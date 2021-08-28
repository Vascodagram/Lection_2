class Editor:

	def view_document(self):
		pass

	def edit_document(self):
		print('Редактирование документов недоступно для бесплатной версии')


class ProEditor(Editor):

	def edit_document(self):
		print('Редактирование документа')


def main():
	key = input('Введите ключ активации ')
	if key == '123qwe':
		print('Активация пройшла успешно')
		editor = ProEditor()

	else:
		print('Ключ введен неверно, повторите попытку')
		editor = Editor()

	editor.view_document()
	editor.edit_document()


if __name__ == '__main__':
	main()


