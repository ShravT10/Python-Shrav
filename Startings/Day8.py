alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
task=input("What you wanna do? Encode/Decode , E/D")

def encode_function():
    main_input=input("Enter the message you want to encode:")
    shift=int(input("Tell shift: "))
    encode=""
    for i in main_input:
        index1=alphabet.index(i)
        shift1=index1+shift
        decode1=alphabet[shift1]
        encode+=decode1
    print(f"Encoded message is {encode}")

def decode_function():
    decoded=input("Enter the encoded message: ")
    shift2=int(input("Enter the amount of shifting done :"))
    decode=""
    for i in decoded:
        index2=alphabet.index(i)
        shift3=index2-shift2
        decode2=alphabet[shift3]
        decode+=decode2
    print(f"Decoded message is {decode}")

if task=='e' or task=='E':
    encode_function()
elif task=='d' or task=='D':
    decode_function()
else:
    print("enter a valid choice")