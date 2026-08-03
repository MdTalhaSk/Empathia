import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")


if not api_key:
    raise Exception("GOOGLE_API_KEY missing")


client = genai.Client(
    api_key=api_key
)



config = types.GenerateContentConfig(

    temperature=0,

    top_p=0.95,

    top_k=64,

    max_output_tokens=8192,

    system_instruction="""

You are Empathia.

You provide emotional support and mental wellness guidance
to students.

Be:
- empathetic
- supportive
- calm
- encouraging

Help students with:
- exam stress
- anxiety
- loneliness
- emotional difficulties

Do not diagnose medical conditions.
Encourage professional help when necessary.

"""

)



history = []



def get_response(user_message):

    try:

        history.append({

            "role":"user",

            "parts":[
                {
                    "text":user_message
                }
            ]

        })


        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=history,

            config=config

        )


        bot_reply = response.text



        history.append({

            "role":"model",

            "parts":[
                {
                    "text":bot_reply
                }
            ]

        })


        return bot_reply



    except Exception as e:

        print("Gemini Error:", e)


        return (
            "I'm currently unable to respond. "
            "Please try again after a moment."
        )