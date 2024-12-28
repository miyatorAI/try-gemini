import configparser
import google.generativeai as gen
import json

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config['KEY-VALUES']['key']
    
    gen.configure(api_key=key)
    model = gen.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("レモンとミカンはどちらのほうがビタミンCが多い?")
    response_text = response.text
    print(response_text)

if __name__ == "__main__":
    main()