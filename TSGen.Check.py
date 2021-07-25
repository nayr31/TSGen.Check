import json, re
from os import error
from packaging.version import Version
from PIL import Image

print("Starting checks...\n---------------------------------------")

# Manifest check ----------------------------
print("Reading manifest...")
try:
    with open("manifest.json", "r+") as f:
        json_data = json.load(f)
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
            testString = json_data["version_number"]
            try:
                Version(json_data["version_number"])
                print("Verified")
            except:
                print("Version number invalid, make sure it follows the \"x.x.x\" semantic versioning.")
        except:
            input("Failed to find \"version_number\" field, make sure it is present in your manifest.")
        print("\nVerifying \"description\"...")
        try:
            testString = json_data["description"]
            if not len(testString) <= 250:
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
except:
    input("Failed to find manifest, make sure it is called \"manifest.json\".")

# Icon check ----------------------------
print("---------------------------------------\nChecking icon...")
try:
    img = Image.open("icon.png").size
    if img[0] != 256 or img[1] != 256:
        input("Icon is not correct resolution, please make sure it is 256x256")
    else:
        print("Verified")
except:
    input("Could not find icon. Please make sure it is called \"icon.png\".")

# Readme check ----------------------------
print("---------------------------------------\nChecking readme...")
try:
    with open("README.md", "r+") as j:
        print("Verified.")
except:
    input("Could not find file, make sure you have a file called \"README.md\".")

input("---------------------------------------\nAll checks completed.")