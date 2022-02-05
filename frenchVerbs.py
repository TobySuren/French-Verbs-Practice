from random import randint #used to pick a random verb

conEndings = ["ais", "ais", "ait", "ions", "iez", "aient"] #all the endings and stems generalised for verbs
simpleEndings = ["ai", "as", "a", "ons", "ez", "ont"]
nearStems = ["Je vais ", "Tu vas ", "Il va ", "Nous allons ", "Vous allez ", "Ils vont "]
frenchForms = ["Je ", "Tu ", "Il ", "Nous ", "Vous ", "Ils "]
haveStem = ["J'ai ", "Tu as ", "Il a ", "Nous avons ", "Vous avez ", "Ils ont "]
amStem = ["Je suis ", "Tu es ", "Il est ", "Nous sommes ", "Vous êtes ", "Ils sont "]
erEnd = ["e", "es", "e", "ons", "ez", "ent"]
irEnd = ["is", "is", "it", "issons", "issez", "issent"]
reEnd = ["s", "s", "", "ons", "ez" "ent"]


def startup(): #loads up the verbs 2d array
    try:
        verbsFile = open("verbs.txt", "r", encoding = "utf-8") #opens the file and converts into a list
        verbsText = verbsFile.read()
        verbsLines = verbsText.split("\n")
        verbsFile.close()
        if len(verbsLines) > 0 and verbsLines[0] != "":
            if verbsLines[len(verbsLines)-1] == "":
                verbsLines.pop()
            global verbs
            verbs = [None] * len(verbsLines)
            for i in range(len(verbsLines)):
                verbs[i] = verbsLines[i].split(", ")
                for i2 in range(len(verbs[i])):
                    if verbs[i][i2] == "True":
                        verbs[i][i2] = True
                    elif verbs[i][i2] == "False":
                        verbs[i][i2] = False

            try:
                main()

            except: #error messages
                print("Error: verbs.txt could not be read. Please make sure the correct format is used.")  
        else:
            print("Error: verbs.txt is empty.")     
    except:
        print("Error: verbs.txt was not found. Make sure the file exists and is in the same folder as this python file. A verbs.txt has been created.")
        open("verbs.txt", "w").close()

forms = ["I", "you (singular)", "he", "we", "you (plural)", "they"] #all verb forms
tenses = ["past perfect", "past imperfect", "present", "near future", "future simple", "conditional"] #all tenses


def perf(verb, form): #past perfect tense
    if verbs[verb][7]:
        output = amStem[form]
    else:
        output = haveStem[form]

    output += verbs[verb][6]
    return output

def imperf(verb, form): #past imperfect tense
    if form == 0 and verbs[verb][5]:
        output = "J'"
    else:
        output = frenchForms[form]
    output += verbs[verb][4]

    if (verbs[verb][1])[-2:] == "ger" and form != 3 and form != 4: #special case for -ger verbs e.g. manger
        output += "e"
    output += conEndings[form]
    return output

def present(verb, form): #present tense
    if form == 0 and verbs[verb][8]:
        output = "J'"
    else:
        output = frenchForms[form]

    if verbs[verb][9]: #irregular
        output += verbs[verb][form + 10]
    
    else: #regular
        output += (verbs[verb][1])[:-2]
        if (verbs[verb][1])[-2:] == "ger" and form == 3: #special case for -ger verbs e.g. manger
            output += "e"
        ending = (verbs[verb][1])[-2:]
        output += eval(ending+"End["+str(form)+"]")
    return output
            
        
def near(verb, form): #near future
    output = nearStems[form]
    output += verbs[verb][1]
    return output

def simple(verb, form): #simple future
    if form == 0 and verbs[verb][3]:
        output = "J'"
    else:
        output = frenchForms[form]

    output += verbs[verb][2]
    output += simpleEndings[form]
    return output

def cond(verb, form): #conditional
    if form == 0 and verbs[verb][3]:
        output = "J'"
    else:
        output = frenchForms[form]

    output += verbs[verb][2]
    output += conEndings[form]
    return output

functions = ["perf", "imperf", "present", "near", "simple", "cond"] #a list of all functions

    
def main(): #the main playing loop
    playing = ""
    while playing != "done":
        verbNo = randint(0, len(verbs)-1)
        verb = verbs[verbNo][0]
        formNo = randint(0, len(forms)-1)
        form = forms[formNo]
        tenseNo = randint(0, len(tenses)-1)
        tense = tenses[tenseNo]
        
        answer = input("Translate \"" +verb+ "\" in the \"" +form+ "\" form and in the " +tense+ " tense.\n") #asks for player translation

        french = eval(functions[tenseNo]+"(verbNo, formNo)") #uses the respective function to translate
        if answer.upper() == french.upper():
            print("\nCorrect!")

        else:
            answer = input("\nIncorrect! The correct answer is \"" +french+ "\". Please type the correct answer:\n")
            while answer.upper() != french.upper():
                answer = input("That is not the correct answer. The correct answer is \"" +french+ "\". Please type the correct answer:\n")
        playing = input("Press enter to try another verb or type \"done\" to end.\n")

startup()

#ADD TO README: the verbs should be written as a table each in verbs.txt: english name, infinitive, conditional & simple stem, if they start with a vowel in conditional & simple, imperfect stem, if they start with a vowel in imperfect, perfect verb, if the perfect tense uses "to be", if the present tense starts with a vowel, if the present tense is irregular
