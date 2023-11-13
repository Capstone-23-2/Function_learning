from common.vars import model, basic_prompt
from datetime import datetime
import google.generativeai as palm
import logging
import os


def get_reply(user_id, sentence):
    if sentence[:7] == '<start>':
        chr_name = sentence[7:]
        start_conversation(user_id, chr_name)
        return 'Success'
    else:
        write_log(user_id, sentence, 'Child')
        res = get_palm_result(user_id, sentence)
        return res


def get_palm_result(user_id, sentence):
    palm.configure(api_key=os.getenv('palm_api_key'))
    prompt = basic_prompt + get_context(user_id) + '\nResponse: '
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=1.0,
        max_output_tokens=100,
        safety_settings=[{"category": "HARM_CATEGORY_DEROGATORY", "threshold": 4}, {"category": "HARM_CATEGORY_TOXICITY", "threshold": 4}, {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 4}, {
            "category": "HARM_CATEGORY_SEXUAL", "threshold": 4}, {"category": "HARM_CATEGORY_MEDICAL", "threshold": 4}, {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 4}],

    )
    res = completion.result
    if res == None:
        logging.error(
            'Following prompt could not generate any response\n'+prompt)
        for filter in completion.filters:
            print(filter['reason'])
        res = 'I can\'t understand. Please try again.'
    write_log(user_id, res, 'Teacher')
    return res


def get_context(user_id):
    with open(get_log_path(user_id), 'r') as f:
        dialogue = f.readlines()
    context = ''.join(dialogue)
    return context


def write_log(user_id, res, speaker):
    with open(get_log_path(user_id), 'a') as f:
        f.write(res + '\n')


def start_conversation(user_id, chr_name):
    if user_id+'.log' in os.listdir('logs'):
        end_conversation(user_id)
    sentence = "Hi. I'm "+chr_name + ". Nice to meet you!! What's your name?"
    #write_log(user_id, sentence, 'Teacher')
    write_log(user_id, '', 'Teacher')
    return


def end_conversation(user_id):
    os.rename(get_log_path(user_id), 'logs/' +
              user_id+'_'+str(datetime.now())+'.log')


def get_log_path(user_id):
    return 'logs/'+user_id+'.log'
