import pywhatkit as pwk

# Get user input for mobile number and message
number = input("Enter the mobile number (without +91): ")
number = "+91" + number  # Add country code

message = input("Enter the message you want to send: ")

try:
    # Try sending the message
    pwk.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True, close_time=3)
    print(f"✅ Message sent successfully to {number}.\nMessage: {message}")
except Exception as e:
    print(f"❌ Failed to send the message. Error: {e}")
