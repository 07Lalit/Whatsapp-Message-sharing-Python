"""
                      pywhatkit
                      ----------


=>  Python offers numerous inbuilt libraries to ease our work.
    Among them pywhatkit is a Python library for sending WhatsApp
    messages at a certain time, it has several other features too.

    Following are some features of pywhatkit module:

1)Send WhatsApp messages.
2)Play a YouTube video.
3)Perform a Google Search.
4)Get information on a particular topic.
5)The pywhatkit module can also be used for converting text into handwritten text images.
"""
import pywhatkit

print(f"               Welcome{chr(128513)}           ")
print("               -----------           ")

try:
    mobile=input("\n\nEnter a mobile number whom you send a message: ")
    mobile = "+91"+mobile
    message= input("Enter a message you want to send: ")
    time = int(input("Enter a time in (24 hrs) format ex(2pm as 14)not include(am or pm): "))
    minutes = int(input("Enter minutes of the scheduled time for the meassage(00-59): "))

    pywhatkit.sendwhatmsg(mobile,message,time,minutes)
    print(f"\n\nMessage will send successfully{chr(128512)}")

except:
    print("An Unexpected Error!")

# import pywhatkit
#
# # Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)
#
# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)
#
# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
#
# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
#
# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
#
# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
#
# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")