
email_one = open('text_files/email_one.txt').read()
email_two = open('text_files/email_two.txt').read()
email_three = open('text_files/email_three.txt').read()
email_four = open('text_files/email_four.txt').read()

# Task 2
def learning_censor(email):
    censored_email = email.replace('learning algorithms', '---')
    return censored_email


# Task 3
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def list_censor(email, censor_terms):
    for word in censor_terms:
        censored_word = ''
        for i in range(0, len(word)):
            if word[i] == ' ':
                censored_word += ' '
            else:
                censored_word += 'X'
        email = email.replace(word, censored_word)
    return email
            


print(list_censor(email_two, proprietary_terms))
