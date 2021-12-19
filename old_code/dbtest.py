from old_code.dbwork import create_connection, close_connection, add_user, remove_user, set_demo, minus_launch, get_user, \
	init_table

path = "../sm_app.sqlite"

def test_unit_minus_launch():
	connection = create_connection(path)
	init_table(connection)
	add_user(connection, 1, "kek", "kek@mail.ru", 1)
	add_user(connection, 2, "kok", "kok@mail.ru", 1)
	minus_launch(connection, 2)
	user2 = get_user(connection, 2)
	assert user2[0] == 2
	assert user2[1] == "kok"
	assert user2[2] == "kok@mail.ru"
	assert user2[3] == 1
	assert user2[4] == 4
	close_connection(connection)

def test_unit_remove():
	connection = create_connection(path)
	init_table(connection)
	add_user(connection, 1, "kek", "kek@mail.ru", 1)
	add_user(connection, 2, "kok", "kok@mail.ru", 1)
	remove_user(connection, 2)
	user2 = get_user(connection, 2)
	print(user2)
	assert user2 == None
	close_connection(connection)

def test_set_demo():
	connection = create_connection(path)
	init_table(connection)
	add_user(connection, 1, "kek", "kek@mail.ru", 1)
	add_user(connection, 2, "kok", "kok@mail.ru", 0)
	set_demo(connection, 2)
	user2 = get_user(connection, 2)
	print(user2)
	assert user2[0] == 2
	assert user2[1] == "kok"
	assert user2[2] == "kok@mail.ru"
	assert user2[3] == 1
	assert user2[4] == 5
	close_connection(connection)