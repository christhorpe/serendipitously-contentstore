import yql


def do_yql(query):
	y = yql.Public()
	result = y.execute(query)
	return result


