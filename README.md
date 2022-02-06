# French Verbs Practice
Helps you to practice French verbs in all different tenses

This program reads the verbs file and then asks you to translate a verb into French in a specific form (I, you singular, he, we, you plural or they) and in a specific tense (passé composé, past imperfect, present, near future, future simple or conditional). It translates the prompt into French and if you enter the correct answer (accents are checked but it's not case specific) then it will tell you. Otherwise, you will be able to see the correct translation and try to type it again. You can continue to translate until you enter "done".

If you come across any inconsistencies, please let me know.

# Verb File Format
When entering new verbs, make sure to give each verb a line and format each variable for the verb accordingly:
- Use ", " to separate variables (none at the start or end of a line)
- A boolean should be written as "True" or "False", with no quotation marks
- Do not use quotation marks when writing strings

Variable order:
- Verb in english e.g. to go (string)
- Infinitive e.g. aller (string)
- If the verb would usually include a reflexive pronoun e.g. je **me** réveiller (boolean)
- The verb's future simple and conditional stem e.g. lir (string)
- The verb's past imperfect stem e.g. lis (string)
- The verb's past participle e.g. allé (string)
- If the verb uses "to be" in the passé composé e.g. Je **suis** allé (boolean)
- If the verb is irregular in the present tense e.g. with aller (boolean)
- IF IRREGULAR: the present tense verb in the I form e.g. vais (string, optional)
- IF IRREGULAR: the present tense verb in the you (singular) form e.g. vas (string, optional)
- IF IRREGULAR: the present tense verb in the he form e.g. va (string, optional)
- IF IRREGULAR: the present tense verb in the we form e.g. allons (string, optional)
- IF IRREGULAR: the present tense verb in the you (plural) form e.g. allez (string, optional)
- IF IRREGULAR: the present tense verb in the they form e.g. vont (string, optional)
