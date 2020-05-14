# function to read from template file.
def read_template(link):
    with open('assets/'+link) as template:
        return template.read()

# function to parse template file, change the format, then return a list with body content with right format, and a list of keywords
def parse(link):
    content = read_template(link).strip()
    count=content.count('{')
    keyList=[]
    template = []
    keystart=content.index('{')
    keyEnd=content.index('}')
    bodyStart=0
    bodyEnd=content.index('{')
    for i in range(count):
        key=content[keystart+1:keyEnd].replace(' ','_')
        body=content[bodyStart:bodyEnd+1]+'0['+key+']}'
        keyList.append(key)
        template.append(body)

        if i==count-1:
            break
        bodyStart=keyEnd+1
        keystart=content.index('{',keystart+1)
        keyEnd=content.index('}',keyEnd+1)
        bodyEnd=keystart
    outcome=[''.join(template), keyList]

    return outcome

# function to ask player for input, matching the keywords.
# the two optional arugment is for testing purposes.
def merge(link, keyWord=[], keyIn=[]):
    parsedArray=parse(link)
    template=parsedArray[0]
    keys=parsedArray[1]
    keysArray=keyWord
    userInputArray=keyIn
    if keysArray == [] and userInputArray == [] :
        for i in range(len(keys)):
            if keys[i] not in keysArray:
                keysArray.append(keys[i])
                displayKey=keys[i].replace('_',' ')
                userInput=input(f'Please enter a/an {displayKey}: ')
                userInputArray.append(userInput)

    container=dict(zip(keysArray,userInputArray))
    resultText=template.format(container)

    return resultText

def play_game(link):
    from textwrap import dedent


    thankYou = """
    **************************************************
    ** Thank you for playing Mad Lib with us today! **
    **************************************************
    """


    output=merge(link)

    print(dedent(thankYou))

    print(output,'\n')

    print('**************************************************')

    with open('assets/user_letter.txt', 'w') as letter:
        letter.write(output)


if __name__ == "__main__":
    from textwrap import dedent
    instruction="""
    *************************************************
    ** Welcome to the game of Mad Lib!             **
    ** Please enter a serious of words followed    **
    ** by the instructions and in the end you will **
    ** see a very interesting letter               **
    *************************************************
    """
    print(dedent(instruction))
    selection = '''
    *************************************************
    ** We have two games to play with, plese enter **
    **                  1 or 2                     **
    *************************************************
    '''
    game_select=input(dedent(selection))

    while game_select != '1' and game_select != '2':
        game_select=input(dedent(selection))

    if game_select == '1':
        link = 'template1.txt'
    elif game_select == '2':
        link = 'template2.txt'
    play_game(link)

