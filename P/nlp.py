from ckiptagger import data_utils, construct_dictionary, WS, POS, NER


def nlp(sent):

    ws = WS("./data")
    pos = POS("./data")
    ner = NER("./data")


    sentence_list=[]
    sentence_list.append(sent)

    word_list = ws(sentence_list)

    pos_list = pos(word_list)

    entity_list = ner(word_list,pos_list)

    return_list=[]



    flat_list=[]
    for word_sent in word_list:
        for word in word_sent:           
            flat_list.append(word)      
    word_list=[]
    word_list=flat_list

    flat_list=[]
    for pos_sent in pos_list:
        for pos in pos_sent:           
            flat_list.append(pos)                 
    pos_list=[]
    pos_list=flat_list

    words_and_pos=dict(zip(word_list,pos_list))

    return_list.append(words_and_pos)
    return_list.append(entity_list)

    return return_list



