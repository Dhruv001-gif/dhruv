import os

def chat_bot():
    print('hello! this is chatbot. how may i assist you.')

    while True:

        chatbot_name = "AV"

        user_input = input("you : ").lower()
        if "hello" in user_input:

            print('hello! what could i do for you.')


        elif "what is your name." in user_input:

             print(chatbot_name)


        elif "bye" in user_input:

          print("bye! have a nice day.")
          break
      
  
      
        else:

           print("invalid command!")

chat_bot() 
