sentence="Hello iam from hyderabad"
# for word in snetence.split():
#     print(word)
result={word:len(word) for word in sentence.split()}
print(result)