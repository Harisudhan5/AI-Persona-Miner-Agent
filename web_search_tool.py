from googlesearch import search

query = "Walter L. Kuehnlein Managing Advisor terra.blue"
result = search(query, num_results=1, safe = None, lang="en")

url_array = []

for url in result:
    url_array.append(url)

print("List of URL's : ",url_array)