from newspaper import Article

def lambda_function_01(event, context):

	url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
	article = Article(url)
	article.download()
	article.text
	return "Gonzalo Rocks"