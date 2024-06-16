import re
from nltk.chat.util import Chat

pairs = [
    [
        r"(what|how|)(.*)(menu)(.*)(list|price|)",
        "We have \n- Adult All You Can Eat (60 minutes) Rp. 148k++\n- Adult All You Can Eat(120 minutes) Rp. 207k++\n- Children All You Can Eat Rp. 74k++\n- Elderly All You Can Eat Rp. 74k++",
    ],
    [
        r"(where|)(.*)(restaurant|store)(.*)(location|position|)(.*)",
        "You can find our restaurant at Lippo Mall Puri - Jakarta at 1st floor near Starbucks or using this google map direction https://maps.app.goo.gl/9KkNBm1JE87GhcXs9",
    ],
    [
        r"(what)(.*)(is|of|)(.*)(fogo|history)(.*)",
        "Fogo is 90 Minutes Brazilian BBQ Eat All You Can Halal MUI Certified Jakarta Bogor Depok",
    ],
    [
        r"(can|)(.*)(reservation|booking|book)(.*)(for)(.*)(people)",
        "We will try to make a booking for %6 people. We will contact you immedietly",
    ],
    [
        r"(is|is threre|any|)(.*)(room|place|lounge|smoking|smoke)(.*)(smoking|smoke|room|place|lounge|)(.*)",
        "Yes, we have seperate room for smoking and non smoking customer",
    ],
    [
        r"(.*)(halal)(.*)",
        "100% halal, we have MUI Certificate and we dont serve pork, lard, or alcohol",
    ],
    [r"(.*)(ask|file|create|would|would like)(.*)(complain)(.*)", "COMPLAIN"],
    [
        r"(.*)quit(.*)",
        "Thankyou for using Fogo Brazillian BBQ AI Customer Service - Test",
    ],
]

chat = Chat(pairs)
print(
    "Welcome to Fogo Brazillian BBQ AI Customer Service - Test, how i can help you today?"
)
user_input = ""

while user_input != "quit":
    try:
        user_input = input(">")
    except EOFError:
        print(user_input)

    if user_input:
        found = False

        for pattern, response in pairs:
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                if response == "COMPLAIN":
                    print("please sumbit your email:")
                    email = input(">")
                    print("please submit your complain:")
                    complain = input(">")
                    print(
                        "\n\nYour complain ticket has created with ticket no TICK-XX-XXX"
                    )
                    print("with email address: " + email)
                    print(complain)
                    print("we will reply to your email shortly, thankyou")
                    found = True
                    break

                pos = response.find("%")
                while pos >= 0:
                    try:
                        num = int(response[pos + 1 : pos + 2])
                        response = (
                            response[:pos] + match.group(num) + response[pos + 2 :]
                        )
                    except Exception:
                        break
                    pos = response.find("%")

                response = response.replace("  ", " ")
                print(response)
                found = True
                break

        if found == False:
            print(
                "Sorry we don't have an answer to your question. We will redirect you to our customer service"
            )
