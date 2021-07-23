import json, re

input("Please place your \"manifest.json\" inside of the \"Testing\" folder.\nPress enter to start check.")

print("\nReading manifest...")
try:
    with open("Testing\manifest.json", "r+") as f:
        json_data = json.load(f)
except:
    input("Failed to find file")
    quit()

print("\nVerifying \"name\"...")
try:
    testString = "".join(re.findall("[a-zA-Z_0-9]", json_data["name"]))
    if not testString == json_data["name"]:
        print("Your \"name\" is incorrectly formatted, please change it to follow the regex of:")
        print("\"a-z\", \"A-Z\", \"0-9\", \"_\"")
    else:
        print("Verified")
except:
    input("Failed to find \"name\" field, make sure it is present in your manifest.")

print("\nVerifying \"version_number\"...")
try:
    testList = json_data["version_number"].split(".")
    if not len(testList) == 3:
        print("\"version_number\" does not have the correct size, make sure that the format follows:")
        print("\"x.x.x\", where each \'x\' is a number.")
    else:
        print("Verified")
except:
    input("Failed to find \"version_number\" field, make sure it is present in your manifest.")

print("\nVerifying \"description\"...")
try:
    testList = json_data["description"].split(".")
    if not len(testList) <= 250:
        print("\"description\" does not have the correct size, make sure that the format follows:")
        print("Less than 250 characters.")
    else:
        print("Verified")
except:
    input("Failed to find \"description\" field, make sure it is present in your manifest.")

print("\nVerifying \"website_url\"...")
try:
    testString = json_data["website_url"]
    print("Verified")
except:
    input("Failed to find \"website_url\" field, make sure it is present in your manifest.")

print("\nVerifying \"dependencies\"...")
try:
    if not isinstance(json_data["dependencies"], list):
        raise Exception("TypeError")
    else:
        print("Verified")
except:
    print("Failed to find or confirm validity \"dependencies\" field, make sure it is present in your manifest and follows correct format:")
    input("Is a list (\'[\' and \']\' encapsulate your object), and dependency strings are seperated by commas.")