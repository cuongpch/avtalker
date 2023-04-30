from argparse import ArgumentParser
import os
import openai
openai.api_key = "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"


def _completion(txt):
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": txt}
  ])
  #print(completion.choices[0].message.content)

def main(args):
    msg=args.msg
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": msg}
    ])
    print(completion.choices[0].message.content)
if __name__ == '__main__':
    parser = ArgumentParser()  
    parser.add_argument("--msg", default='Hello', help="some messsage")
    args = parser.parse_args()
    main(args)
