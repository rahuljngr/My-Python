def sentence_maker(phrase):
    introgatives = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(introgatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True :
    user_input = input("say somthings: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))