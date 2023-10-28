from key import palm_api_key
import google.generativeai as palm
import logging


def get_reply(user_id, sentence):
    palm.configure(api_key=palm_api_key)
    model = 'models/text-bison-001'
    prompt = """
    You are taking to a child. Reply with simple and easy sentence.
Child: """ + sentence + '\n'
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=1.0,
        max_output_tokens=100,
    )
    res = completion.result
    if res == None:
        logging.error(
            'Following prompt could not generate any response\n'+prompt)
        res = 'Something went wrong'
    return res
