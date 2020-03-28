import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("chatbot.xml")
kernel.respond("load aiml b")

while True:
    print(kernel.respond(input("User: ")))